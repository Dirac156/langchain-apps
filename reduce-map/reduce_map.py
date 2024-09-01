"""_summary_ module comment"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.summarize import load_summarize_chain

DOTENV_FILE_PATH = os.path.join(os.getcwd(), ".env")
load_dotenv(DOTENV_FILE_PATH)


PDF_FILE_PATH = os.path.join(os.getcwd(), "reduce-map", "homework_1.pdf")

pdf_laoder = PyPDFLoader(PDF_FILE_PATH)

docs = pdf_laoder.load_and_split()

llm = OpenAI()

chain = load_summarize_chain(llm, chain_type="map_reduce")

output = chain.invoke(docs)

print(output)
