# AraSearch
An Arabic Semantic search engine that enhances search precision and user experience in Arabic. The model is a Natural Language Processing task responsible for Arabic contextual understanding using the Arabert Model and FAISS as an indexing and querying tool to make an efficient search.

## Getting Started
You'll need to download the required libraries from requirements.txt file in your environment using `pip install` and note that the python that should be used in the environment should be python = 3.8

## Usage
You can download the three python files along with the templates and the static folders to your directory. Once you have all the files there, you can either use your own dataset or try ours, then run the app.py file.
You'll to run the embed.py file first on a dataset to obtain the faissindex file that contains the embeddings of all the arabic documents in your dataset, then you can run the app.py that will open a page in your browser where you will be able to use the model.

## Technology Stack
* [AraBERT](https://huggingface.co/aubmindlab/bert-base-arabertv02/tree/main)
  * This is a model that uses the BERT architecture and is customed to be used on arabic corpuses. It was build by [aubmindlab](https://huggingface.co/aubmindlab) in 2020, and we used it to obtain embeddings of our arabic documents.
* [FAISS](https://github.com/facebookresearch/faiss)
  * This is a library created by Facebook, we benefit from its indexing and querying abilities to work as a search engine in our project.
* [Wortschatz](https://wortschatz.uni-leipzig.de/de)
  * A german website that collects news datasets in different languages. We got the arabic dataset from this website, specifically news from the 3 recent years.
