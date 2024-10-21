
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="HuggingFaceH4/zephyr-7b-beta",
  huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_TOKEN")
)