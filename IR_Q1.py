import os
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    print("Original Text:")
    print(text)
    print("--------------------")
    
    # Lowercase the text
    print("Text after lowercasing:")
    text = text.lower()
    print(text)
    print("--------------------")
    
    # Tokenization with WordPunctTokenizer
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    
    print("Tokens after tokenization:")
    print(tokens)
    print("--------------------")
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    print("Tokens after removing stopwords:")
    print(tokens)
    print("--------------------")
    
    # Remove punctuations
    tokens = [word for word in tokens if word not in string.punctuation]
    
    print("Tokens after removing punctuations:")
    print(tokens)
    print("--------------------")
    
    # Remove blank space tokens
    tokens = [word for word in tokens if word.strip()]
    
    print("Tokens after removing blank spaces:")
    print(tokens)
    print("--------------------")
    
    # Join tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    print("Text after joining tokens:")
    print(preprocessed_text)
    print("--------------------")
    
    return preprocessed_text

def preprocess_files(input_folder, output_folder, num_files=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    processed_files = 0
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            
            with open(input_file_path, 'r') as input_file:
                text = input_file.read()
                print(f"File: {filename}")
                preprocess_text(text)
                print("--------------------")
            
            processed_files += 1
            if processed_files >= num_files:
                break

# Provide the folder paths for input and output files
input_folder = "C:\\Users\\sainiisha2619\\IR_A1\\text_files"
output_folder = "C:\\Users\\sainiisha2619\\IR_A1\\preprocessed_files"

preprocess_files(input_folder, output_folder)