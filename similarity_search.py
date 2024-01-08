import argparse
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings
import os

os.environ["OPENAI_API_KEY"] = "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"

vectordb = None
embedding = OpenAIEmbeddings()

# vectorstore = Chroma.from_documents(docs, embeddings)
vectordb = Chroma(
    persist_directory="2018-G12-Physics-E_chapters-embeddings", embedding_function=embedding
)

query = "wavelength"
docs = vectordb.similarity_search(query)

for i in range(len(docs)):
    print(docs[i].page_content)
    print("\n\n")