from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile',temperature=0)

result = model.invoke("suggest me a good hindi movie in between 2024 to 2025")
print(result.content)