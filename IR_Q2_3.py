import os
import pickle
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

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

def preprocess_query(query):
    """Preprocess the input query."""
    return preprocess_text(query)

def load_inverted_index(filename):
    """Load the inverted index from the file."""
    with open(filename, 'rb') as f:
        index = pickle.load(f)
    return index

def intersect_posting_lists(posting_list1, posting_list2):
    """Compute the intersection of two posting lists."""
    return sorted(list(set(posting_list1).intersection(posting_list2)))

def union_posting_lists(posting_list1, posting_list2):
    """Compute the union of two posting lists."""
    return sorted(list(set(posting_list1).union(posting_list2)))

def subtract_posting_lists(posting_list1, posting_list2):
    """Compute the subtraction of posting list2 from posting list1."""
    return sorted(list(set(posting_list1).difference(posting_list2)))

def perform_operation(operation, result, next_term, inverted_index):
    """Perform the specified operation on the given terms."""
    posting_list = search_query(next_term, inverted_index)
    if operation == 'AND':
        result = intersect_posting_lists(result, posting_list)
    elif operation == 'OR':
        result = union_posting_lists(result, posting_list)
    elif operation == 'AND NOT':
        result = subtract_posting_lists(result, posting_list)
    elif operation == 'OR NOT':
        result = union_posting_lists(result, subtract_posting_lists(inverted_index.keys(), posting_list))
    return result

def process_queries(N, queries, operations, inverted_index):
    """Process the list of queries and return results."""
    results = []
    for i in range(N):
        query = preprocess_query(queries[i])
        terms = query.split()
        ops = operations[i]
        result = search_query(terms[0], inverted_index)
        j = 1
        op_index = 0
        while j < len(terms):
            if j < len(ops):
                operation = ops[op_index]
                next_term = terms[j]
                result = perform_operation(operation, result, next_term, inverted_index)
                j += 1
                op_index += 1
            else:
                break
        results.append(result)
    return results

def search_query(term, inverted_index):
    """Retrieve the posting list for the given term."""
    return inverted_index.get(term, [])

def print_output(query, result, operations):
    """Print the output in the specified format."""
    preprocessed_terms = query.split()
    preprocessed_query = " AND ".join([f"{preprocessed_terms[i]}" for i in range(len(preprocessed_terms) - 1) if preprocessed_terms[i] not in stopwords.words('english')])
    preprocessed_query += f" {operations[-1]} {preprocessed_terms[-1]}"  # Use the last operation with the last term
    print(f"Query after preprocessing: {preprocessed_query}")
    print(f"Number of documents retrieved for query: {len(result)}")
    print(f"Names of the documents retrieved for query: {[f'{x}' for x in result]}")
    print()


# Example usage:
index_file = 'inverted_index.pkl'

# Load the inverted index from the file
loaded_inverted_index = load_inverted_index(index_file)

# Input
N = int(input("Enter the number of queries: "))
queries = []
operations = []
for i in range(N):
    query = input("Enter the query: ")
    ops = input("Enter the operations separated by comma: ")
    queries.append(query)
    operations.append(ops.split(','))

# Process queries
results = process_queries(N, queries, operations, loaded_inverted_index)

# Output
# Output
for i in range(N):
    print_output(queries[i], results[i], operations[i])
