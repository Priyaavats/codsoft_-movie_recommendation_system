# recommendation_system.py
# Simple Collaborative Filtering Recommendation System (All Users)

import pandas as pd

# Sample dataset
data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'Movie': [
        'Inception', 'Interstellar', 'The Matrix',
        'Inception', 'The Dark Knight',
        'Interstellar', 'The Matrix',
        'The Matrix', 'The Dark Knight'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

def recommend(user):
    """Recommend movies for a given user based on similar users' preferences."""
    liked_movies = set(df[df['User'] == user]['Movie'])
    
    # Find similar users (share at least one movie)
    similar_users = df[df['Movie'].isin(liked_movies) & (df['User'] != user)]['User'].unique()
    
    # Movies liked by similar users but not by current user
    recommendations = df[df['User'].isin(similar_users) & (~df['Movie'].isin(liked_movies))]['Movie'].unique()
    
    return list(recommendations)

if __name__ == "__main__":
    users = df['User'].unique()
    print("Movie Recommendations for All Users:\n")
    for u in users:
        print(f"User {u}: {recommend(u)}")
