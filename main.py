# 1. Install and Import Libraries

!pip install langchain
!pip install openai
!pip install PyPDF2
!pip install faiss-cpu
!pip install -U langchain-community
!pip install tiktoken


from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

# 2. Read and Extract Text
from PyPDF2 import PdfReader
import os
print(os.listdir())

pdf_path = "Your pdf path"
pdfreader = PdfReader(pdf_path)

page = pdfreader.pages[0]
text = page.extract_text()

# print(text)
import os
OPENAI_API_KEY = "Enter openai_API key"


from typing_extensions import Concatenate
raw_text=''
for i,page in enumerate(pdfreader.pages):
    content=page.extract_text()
    if content:
        raw_text+=content

# print(raw_text)


# 3. Split Text into Chunks

text_splitter=CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)
texts=text_splitter.split_text(raw_text)
# print(len(texts))

# 4. Create Embeddings and Index

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# 5. Implement Question-Answering System

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import openai

qa_chain = load_qa_chain(OpenAI(api_key=OPENAI_API_KEY), chain_type="stuff")


def answer_query(query):
    docs = documentsearch.similarity_search(query)
    answer = qa_chain.run(input_documents=docs, question=query)
    return answer

queries = [
    "Ask question from PDF"
]

for query in queries:
    answer = answer_query(query)
    print(f"Query: {query}\nAnswer: {answer}\n")




