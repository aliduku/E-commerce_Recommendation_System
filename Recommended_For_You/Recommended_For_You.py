from flask import Flask, request, render_template
from sklearn.metrics.pairwise import cosine_similarity
import random
import pandas as pd

app = Flask(__name__)

# Split data into past and future purchases
past_data = pd.read_csv('Recommended_For_You/data/past_data.csv', index_col=0)

future_data = pd.read_csv('Recommended_For_You/data/future_data.csv', index_col=0)

# Create a user-item matrix for past data
user_item_matrix = past_data.pivot_table(index='CustomerID', columns='Description', values='Quantity', fill_value=0)

# Compute cosine similarity matrix between users
user_similarity = cosine_similarity(user_item_matrix)

# Find user IDs present in both past and future datasets
common_user_ids = set(past_data['CustomerID']).intersection(set(future_data['CustomerID']))

# Define the function to get recommendations
def get_recommendations_cosine(user_id, num_recommendations=5):
    if user_id not in user_item_matrix.index:
        return None  # User ID not found in the data
    user_index = user_item_matrix.index.get_loc(user_id)
    user_similarities = user_similarity[user_index]

    # Calculate recommendation scores based on past data
    recommendation_scores = user_similarities.dot(user_item_matrix.values)

    # Get top recommended items
    recommended_indices = recommendation_scores.argsort()[-num_recommendations:][::-1]
    return user_item_matrix.columns[recommended_indices]

# Route to handle recommendations
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_id = int(request.form['user_id'])  # Convert user input to integer
    except ValueError:
        return render_template('error.html', message='Please enter a valid user ID (integer)')
    
    recommendations = get_recommendations_cosine(user_id)
    
    if recommendations is None:
        return render_template('error.html', message=f'User ID {user_id} not found')
    
    return render_template('recommendations.html', user_id=user_id, recommendations=recommendations)

if __name__ == '__main__':
    # Convert common_user_ids to a list and get a sample of 10 user IDs
    sample_common_user_ids = random.sample(list(common_user_ids), 10)
    print("Sample of Common User IDs:", sample_common_user_ids)

    app.run(debug=True)
