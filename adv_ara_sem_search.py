import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import psycopg2
import numpy as np

# Load the dataset
dataset = pd.read_csv('small.csv')

# Load the Arabert tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabertv2")
model = AutoModel.from_pretrained("aubmindlab/bert-base-arabertv2")

# Function to embed sentences using the model
def embed_sentences(sentences):
# Tokenize the sentences
    tokenized = tokenizer(sentences, padding=True, truncation=True, max_length=100, return_tensors="pt")
# Pass the tokenized sentences through the model
    with torch.no_grad():
        outputs = model(**tokenized)
        embeddings = outputs.last_hidden_state[:,0,:]
    # Return the sentence embeddings
    return embeddings

def query_model(s_word):

    # Load the index from the file
    index = faiss.read_index('indexed_embeddings.faissindex')
    # Example query text (replace this with your actual query text)
    query_text = s_word

    # Compute the embedding for the query text (using Arabert or your chosen embedding model)
    query_embedding = embed_sentences(query_text)

    # Find similar embeddings using Faiss
    k = 5  # Number of nearest neighbors to retrieve
    distances, indices = index.search(query_embedding, k)

    closest_sentences = dataset.iloc[indices[0]]["Sentences"].to_list()

    return closest_sentences
    
