import os
import pickle

def create_inverted_index_from_folder(folder_path):
    inverted_index = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            doc_id = filename  # Assuming filename serves as the document identifier
            for word in words:
                if word in inverted_index:
                    if doc_id not in inverted_index[word]:
                        inverted_index[word].append(doc_id)
                else:
                    inverted_index[word] = [doc_id]
    inverted_index = {word: sorted(doc_ids) for word, doc_ids in inverted_index.items()}
    return inverted_index

def save_inverted_index(index, filename):
    with open(filename, 'wb') as f:
        pickle.dump(index, f)

def load_inverted_index(filename):
    with open(filename, 'rb') as f:
        index = pickle.load(f)
    return index

# Example usage:
folder_path = "C:\\Users\\sainiisha2619\\IR_A1\\preprocessed_files"
unigram_inverted_index = create_inverted_index_from_folder(folder_path)
# print(unigram_inverted_index)
# Save the inverted index to a file
save_inverted_index(unigram_inverted_index, "inverted_index.pkl")

# Load the inverted index from the file
loaded_inverted_index = load_inverted_index("inverted_index.pkl")

# Print the loaded inverted index
#for word, doc_ids in sorted(loaded_inverted_index.items()):
   # print(f"{word}: {doc_ids}")