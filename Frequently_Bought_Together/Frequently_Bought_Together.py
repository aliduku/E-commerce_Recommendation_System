from flask import Flask, request, render_template
import random
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the user_item_matrix from the file
rules = pd.read_csv('Frequently_Bought_Together/data/rules.csv', index_col=0)

# Load the item_mapping from the file
item_mapping = pd.read_csv('Frequently_Bought_Together/data/item_mapping.csv', index_col='StockCode')

# Define function to get frequently bought together items for a given item
def frequently_bought_together(item_id, num_recommendations=5):
    item_description = item_mapping.loc[item_id, 'Description']
    associated_items = rules[rules['antecedents'].apply(lambda x: item_id in x)]
    associated_items = associated_items[associated_items['consequents'] != item_id]
    associated_items = associated_items.sort_values('lift', ascending=False).head(num_recommendations)
    recommended_items = associated_items['consequents'].tolist()
    return recommended_items, item_description

# Route to handle recommendations
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend_frequent', methods=['POST'])
def recommend_frequent():
    item_id = request.form['item_id']  # Get item ID from user input

    if item_id not in item_mapping.index:
        return render_template('error.html', message=f'Invalid item ID: {item_id}')

    recommended_items, item_description = frequently_bought_together(item_id)

    if not recommended_items:
        return render_template('error.html', message=f'No frequent items found for the given item ID')

    return render_template('frequent_items.html', item_description=item_description, recommended_items=recommended_items, item_mapping=item_mapping)

if __name__ == '__main__':
    # Convert stock codes to a list of items with recommendations
    items_with_recommendations = rules['antecedents'].explode().unique().tolist()

    # Sample 10 items from the list of items with recommendations
    sample_stock_codes = random.sample(items_with_recommendations, min(10, len(items_with_recommendations)))
    print("Sample of Stock Codes with Recommendations:", sample_stock_codes)

    app.run(debug=True)
