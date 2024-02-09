import os
import pickle

def create_positional_index(folder_path):
    positional_index = {}

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            with open(file_path, 'r') as file:
                content = file.read()
                terms = content.split()
                doc_id = file_name.split('.')[0]  # Extract document ID from file name

                for position, term in enumerate(terms, start=1):
                    if term not in positional_index:
                        positional_index[term] = []
                    positional_index[term].append((doc_id, position))

    return positional_index

def save_positional_index(positional_index, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(positional_index, file)

def load_positional_index(file_name):
    with open(file_name, 'rb') as file:
        positional_index = pickle.load(file)
    return positional_index

def main():
    folder_path = input("Enter the path to the folder containing preprocessed files: ").strip()

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    positional_index = create_positional_index(folder_path)

    save_file_name = input("Enter the filename to save the positional index (with .pkl extension): ").strip()
    save_positional_index(positional_index, save_file_name)
    print("Positional index saved successfully.")

    # Load positional index from saved file and print
    load_file_name = input("Enter the filename to load the positional index from: ").strip()
    loaded_index = load_positional_index(load_file_name)

    # Print the loaded positional index
    print("\nLoaded Positional Index:")
    for term, postings in loaded_index.items():
        print(f"Term: {term}")
        print("Postings:")
        for posting in postings:
            print(f"Document ID: {posting[0]}, Position: {posting[1]}")
        print()

if __name__ == "__main__":
    main()