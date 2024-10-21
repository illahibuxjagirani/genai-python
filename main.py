

from langchain_openai import OpenAI #type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Convert this english sentence into urdu language: 'How are you doing today?'  "

respone = llm.invoke(prompt)

print(respone)
