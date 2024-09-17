# PDF-QA-Assistant

PDF-QA-Assistant is a generative AI tool that enables users to upload PDF documents and ask questions based on their content. Using OpenAI embeddings and LangChain, it converts the content into an easily searchable format and retrieves answers based on natural language queries.

## Features
- Upload a PDF document.
- Extract and process text from the PDF.
- Perform similarity-based question answering using OpenAI's GPT models.
- Search through the content to find answers to any relevant question from the document.


## Install Dependencies

You need to install the required Python packages Before running the project. You can do so by running the following commands:


```bash
pip install langchain
pip install openai
pip install PyPDF2
pip install faiss-cpu
pip install -U langchain-community
pip install tiktoken
```
Alternatively, you can install all dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Set Your OpenAI API Key
To use OpenAI's models, you need an API key from OpenAI. You can obtain one by signing up at OpenAI's platform.

Once you have the key, open the script and replace `"Enter opai_key"` with your actual API key:

```python
OPENAI_API_KEY = "your-openai-api-key"
```


## Provide the PDF Path
Make sure to specify the path to your PDF file in the code:

```python
pdf_path = "Your pdf path"
```
