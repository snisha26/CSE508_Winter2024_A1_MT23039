import os
import string
import pickle
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords

def preprocess_text(text):
    """Preprocess the input text."""
    # Lowercase the text
    text = text.lower()
    # Tokenization with WordPunctTokenizer
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    # Remove punctuations
    tokens = [word for word in tokens if word not in string.punctuation]
    # Remove blank space tokens
    tokens = [word for word in tokens if word.strip()]
    # Join tokens back into a string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

def load_positional_index(index_file):
    with open(index_file, 'rb') as f:
        positional_index = pickle.load(f)
    return positional_index

def search_query(query, positional_index):
    # Implement your search algorithm here using the positional index
    # This is a placeholder function; you need to replace it with your actual search logic
    unique_results = set()
    query_terms = query.split()  # Split query into terms
    for term in query_terms:
        if term in positional_index:
            for doc_id, _ in positional_index[term]:
                unique_results.add(doc_id)
    return list(unique_results)



def main():
    num_queries = int(input("Enter the number of queries: "))
    queries = []
    
    # Take input for queries
    for _ in range(num_queries):
        query = input("Enter query: ").strip()
        queries.append(query)

    # Load positional index from PKL file
    index_file = "C:\\Users\\sainiisha2619\\IR_A1\\positional_index.pkl"
    if not os.path.isfile(index_file):
        print("Positional index file not found.")
        return
    positional_index = load_positional_index(index_file)

    # Process queries
    for i, query in enumerate(queries, 1):
        preprocessed_query = preprocess_text(query)
        result = search_query(preprocessed_query, positional_index)
        print(f"Number of documents retrieved for query {i} using positional index: {len(result)}")
        print(f"Names of documents retrieved for query {i} using positional index: {[f'{doc_id}.txt' for doc_id in result]}")

if __name__ == "__main__":
    main()