import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import torch

# Load the dataset
dataset = pd.read_csv('small.csv')

# Load the Arabert tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabertv2")
model = AutoModel.from_pretrained("aubmindlab/bert-base-arabertv2")

# Function to embed sentences using the model
def embed_sentences(sentences):
    # Tokenize the sentences
    tokenized = tokenizer(sentences, padding=True, truncation=True, max_length=512, return_tensors="pt")

    # Pass the tokenized sentences through the model
    with torch.no_grad():
        outputs = model(**tokenized)
        embeddings = outputs.last_hidden_state[:,0,:]

    # Return the sentence embeddings
    return embeddings

# Embed the sentences from the dataset
sentence_embeddings = embed_sentences(dataset['Sentences'].tolist())

# Print the shape of the embeddings
print("Embeddings shape:", sentence_embeddings.shape)

# Create Faiss index and add embeddings
index = faiss.IndexFlatL2(768)  # You can choose a different index type based on your needs
index.add(sentence_embeddings)
# Save the index to a file
faiss.write_index(index, 'indexed_embeddings.faissindex')