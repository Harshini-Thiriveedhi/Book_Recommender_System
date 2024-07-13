import pickle
import pandas as pd
# Path to your pickle file
pickle_file_path = 'popular.pkl'

# Load data from pickle file
try:
    with open(pickle_file_path, 'rb') as file:
        data = pickle.load(file)
    
    # Print the loaded data
    print("Data loaded from pickle file:")
    print(data)
    
    # Optionally, print specific parts of the data
    if isinstance(data, dict):
        print("Book names:", data.get('Book-Title', 'Key not found'))
        print("Authors:", data.get('Book-Author', 'Key not found'))
        print("Votes:", data.get('num_ratings', 'Key not found'))
        print("Ratings:", data.get('avg_ratings', 'Key not found'))
        print("Images:", data.get('image', 'Key not found'))
except Exception as e:
    print("Error loading pickle file:", e)
