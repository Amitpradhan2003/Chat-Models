from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile',temperature=0)

result = model.invoke("suggest me a good hindi movie in between 2024 to 2025")
print(result.content)



# suggest me a good hindi movie in between 2024 to 2025
# Expected Output: A recommendation of a good Hindi movie released between 2024 and 2025.
# Example Output: "One highly recommended Hindi movie from that period is 'Pathaan' (2024), starring Shah Rukh Khan. It's an action-packed thriller that received great reviews."