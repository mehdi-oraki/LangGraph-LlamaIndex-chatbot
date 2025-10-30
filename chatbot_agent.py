import os
from typing import TypedDict, Optional
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from llama_index.llms.huggingface import HuggingFaceLLM

load_dotenv()
MODEL_ID_OR_PATH = os.getenv("HUGGINGFACE_MODEL_PATH", "microsoft/DialoGPT-small")

class State(TypedDict, total=False):
	question: str
	answer: str

def make_llm(model_ref: str):
    tokenizer = AutoTokenizer.from_pretrained(model_ref, local_files_only=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    model = AutoModelForCausalLM.from_pretrained(model_ref, local_files_only=True)
    return HuggingFaceLLM(
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=128,
    )

llm = make_llm(MODEL_ID_OR_PATH)

def llm_node(state: State) -> State:
	question = state.get("question", "")
	resp = llm.complete(question)
	# resp may be a string or an object with .text
	answer = resp.text if hasattr(resp, "text") else str(resp)
	return {"answer": answer}

graph = StateGraph(State)
graph.add_node("llm", llm_node)
graph.set_entry_point("llm")
graph.add_edge("llm", END)
app = graph.compile()

if __name__ == "__main__":
	user_question = input("Ask your question: ")
	result = app.invoke({"question": user_question})
	print("\nAnswer:\n" + result["answer"])