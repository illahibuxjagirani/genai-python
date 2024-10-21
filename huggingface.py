
from langchain_huggingface import HuggingfaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingfaceEndpoint(
  repo_id="HuggingFaceH4/zephyr-7b-beta",
  huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_TOKEN")
)