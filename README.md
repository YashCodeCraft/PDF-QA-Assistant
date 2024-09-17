# PDF-QA-Assistant

PDF-QA-Assistant is a generative AI tool that enables users to upload PDF documents and ask questions based on their content. Using OpenAI embeddings and LangChain, it converts the content into an easily searchable format and retrieves answers based on natural language queries.

## Features
- Upload a PDF document.
- Extract and process text from the PDF.
- Perform similarity-based question answering using OpenAI's GPT models.
- Search through the content to find answers to any relevant question from the document.

## Installation

Before running the project, ensure you have installed the necessary Python libraries. You can install them using the following commands:

```bash
pip install langchain
pip install openai
pip install PyPDF2
pip install faiss-cpu
pip install -U langchain-community
pip install tiktoken
