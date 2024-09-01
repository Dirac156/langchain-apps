"""_summary_"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

DOTENV_FILE_PATH = os.path.join(os.getcwd(), ".env")
load_dotenv(DOTENV_FILE_PATH)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

output = llm.invoke("Hello")

print(output.usage_metadata)
