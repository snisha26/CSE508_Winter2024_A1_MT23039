import os

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

def main():
    folder_path = input("Enter the path to the folder containing preprocessed files: ").strip()

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    positional_index = create_positional_index(folder_path)

    # Print the positional index
    for term, postings in positional_index.items():
        print(f"Term: {term}")
        print("Postings:")
        for posting in postings:
            print(f"Document ID: {posting[0]}, Position: {posting[1]}")
        print()

if __name__ == "__main__":
    main()