from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_huggingface import HuggingFacePipeline

model_id = "google/flan-t5-base"  # Much better instruction following

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=50
)

llm = HuggingFacePipeline(pipeline=pipe)

response = llm.invoke("Give me only the correct capital city name. What is the capital of India?")
print("\nResponse:", response)

