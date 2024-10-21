# getting started with langchain

- python based dev container with using vs code remote explorer 

- installing poetry from "https://python-poetry.org/docs/#installing-with-the-official-installer"

```
- Install poetry by run command in terminal “curl -sSL https://install.python-poetry.org | python3 –
```

- langchain installation link "https://python.langchain.com/v0.1/docs/get_started/installation/"

```
- installing "poetry add langchain-core"
- installing "poetry add langchain-community"
- installing "poetry add langchain-openai"
```

creating file main.py


- now we will run this file by running  " poetry run python main.py" in terminal

- in main.py file write from langchain_openai import OpenAI #type: ignore

llm = OpenAI()

- now for api keys search this link " https://platform.openai.com/api-keys" and create a new secret key

# print("hello World I am IB")
from langchain_openai import OpenAI #type: ignore

from langchain_openai import OpenAI #type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Convert this english sentence into urdu language: 'How are you doing today?'  "

respone = llm.invoke(prompt)

print(respone)
poetry add load_dotenv


