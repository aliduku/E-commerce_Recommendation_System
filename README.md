# Recommendation System

## Introduction

Welcome to the documentation of my recommendation system project. This document provides a comprehensive overview of the creation, evaluation, improvement, and deployment of my recommendation system. My aim was to build a robust recommendation system that enhances user experiences in an e-commerce environment. The system encompasses three distinct recommendation types: "Recommended for You," "Similar Items," and "Frequently Bought Together." These recommendations are generated through collaborative filtering, content-based filtering, and frequent itemset mining techniques.

## Development Process

My development process was meticulously planned and executed, involving data cleaning, exploration, algorithm implementation, evaluation, and deployment. The stages of development include:

- Understanding the Data: I delved into the provided e-commerce dataset, identifying discrepancies, missing values, and potential issues.
- Data Preprocessing: I cleaned the dataset by addressing missing values, canceled orders, negative quantities, and zero-unit prices.
- Exploratory Data Analysis (EDA): Visualizations uncovered patterns, customer behaviors, and sales trends, guiding subsequent stages.
- Recommendation Generation: Collaborative filtering, content-based filtering, and frequent itemset mining techniques were employed to generate personalized suggestions.
- Evaluation and Metrics: The recommendation system's performance was evaluated using precision, recall, and Mean Average Precision (MAP).
- Deployment: The recommendation system was deployed as interactive Flask apps, allowing users to interact with recommendations.
- Documentation: This comprehensive document showcases the development process, results, analysis, and insights.

## Data Cleaning and Exploration

My data cleaning and exploration phase involved:

- Addressing Missing Values: I removed rows with missing values to ensure data quality.
- Handling Canceled Orders: Canceled orders and negative quantities were excluded to maintain data integrity.
- Eliminating Zero Unit Prices: Entries with zero-unit prices were removed for data consistency.
- Managing Duplicate Entries: Duplicate entries were identified and removed to ensure accurate analyses.
- Data Type Corrections: Data types were adjusted for accuracy and consistency.
- Ensuring Unique Descriptions: A dictionary mapping 'StockCode' to the most common 'Description' was created for consistency.

## Recommendation Generation

My recommendation system generates three types of recommendations:

### Recommended for You

1. User-Item Interaction Matrix: A matrix represents interactions between users and items.
2. Similarity Calculation: User similarity is computed based on interactions.
3. Neighborhood Selection: Similar users form a "neighborhood."
4. Item Ranking: Items are ranked based on user neighbors' interactions.
5. Final Recommendations: Top-ranked items are recommended, avoiding redundancy.

### Similar Items

1. Item-Item Similarity Matrix: A matrix represents item similarities.
2. Item Similarity Calculation: Item similarity metrics are calculated.
3. Item Ranking: Items are ranked based on similarity scores.
4. Recommendation Generation: Top-ranked similar items are recommended.

### Frequently Bought Together

1. Purchase History Data: User purchase histories capture multiple-item transactions.
2. Frequent Itemset Mining: Frequent itemsets are identified using algorithms.
3. Association Rule Generation: Association rules express item relationships.
4. Confidence and Support: Rules are evaluated using confidence and support.
5. Recommendation Generation: High-confidence rules inform recommendations.

## Implementation and Deployment

I developed interactive Flask apps to showcase my recommendation system's functionality:

- Recommended for You App: Provides personalized recommendations based on user preferences and interactions.
- Similar Items App: Allows users to explore items similar to their selected product.
- Frequently Bought Together App: Suggests items frequently purchased alongside a selected item.

## Conclusion

Building these recommendation systems has deepened my understanding of data science and machine learning. I'm excited to contribute, learn more, and drive innovation and success.

## Kaggle Notebook Link

- [Kaggle Notebook](https://www.kaggle.com/code/aliessamali/recommendation-systems-e-commerce#Recommendations)
