from flask import Flask, request, render_template
import random
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the user_item_matrix from the file
user_item_matrix = pd.read_csv('Similar_Items/data/user_item_matrix.csv', index_col=0)

# Load the item_item_similarity matrix from the compressed file
loaded_data = np.load('Similar_Items/data/item_item_similarity.npz')
item_item_similarity = loaded_data['data']

# Load the item_mapping from the file
item_mapping = pd.read_csv('Similar_Items/data/item_mapping.csv', index_col='StockCode')

# define function to recommend similar items and returns a list of similar item descriptions
def recommend_similar_items(item_id, n=10):
    item_index = user_item_matrix.columns.get_loc(item_id)
    similar_items_indices = item_item_similarity[item_index].argsort()[::-1][1:n+1]
    similar_item_codes = list(user_item_matrix.columns[similar_items_indices])

    return (item_mapping.loc[item_mapping.index.isin(similar_item_codes)]['Description'].drop_duplicates().tolist())


# Route to handle recommendations
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    item_id = request.form['item_id']  # Get item ID from user input

    if item_id not in user_item_matrix.columns:
        return render_template('error.html', message=f'Invalid item ID: {item_id}')

    similar_items = recommend_similar_items(item_id)

    if not similar_items:
        return render_template('error.html', message=f'No similar items found for the given item ID')

    return render_template('similar_items.html', item_id=item_mapping.loc[item_id, 'Description'], similar_items=similar_items)

if __name__ == '__main__':
    # Convert stock codes to a list and get a sample of 10 stock codes
    sample_stock_codes = random.sample(list(user_item_matrix.columns), 10)
    print("Sample of Stock Codes:", sample_stock_codes)

    app.run(debug=True)