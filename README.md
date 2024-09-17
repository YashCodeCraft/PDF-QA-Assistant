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

## Provide the PDF Path
Make sure to specify the path to your PDF file in the code:

## Run the Code
Run the main script after you’ve set up the API key and PDF path. The script will:

- Extract the text from your PDF.
- Break the text into manageable chunks.
- Use embeddings to generate vector representations for efficient querying.
- Allow you to input any query and get an answer based on the PDF content.
You can customize or add more queries as needed. For example:
```python
queries = [
    "What is the main idea of the document?",
    "Explain the conclusion of the paper."
]

for query in queries:
    answer = answer_query(query)
    print(f"Query: {query}\nAnswer: {answer}\n")
```
## Example Output
After running the code, you will see results like this:

```bash
Copy code
Query: What is energy?
Answer: Energy is defined as the capacity to do work and comes in various forms such as kinetic, potential, thermal, etc.
```

## How It Works

- Text Extraction: The PyPDF2 library extracts text from the PDF.
- Text Splitting: LangChain splits the text into smaller chunks that fit within token limits for the GPT model.
- Embeddings: OpenAI’s embedding model converts each chunk of text into vector embeddings.
- Vector Search: FAISS is used to perform similarity search over the vectorized text chunks to find relevant sections based on user queries.
- Question-Answering: The model answers queries by running a QA chain on the most relevant text sections.
