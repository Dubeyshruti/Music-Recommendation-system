# -*- coding: utf-8 -*-
"""music_recommendation.iynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hf46gZ8vEeDPpkKuz_7vjP0vVAEVAUOT
"""

import pandas as pd

"""# New Section

**Spotify Song's Genre Segmentation**


![spotth.jpg](data:image/jpeg;base64,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)

**Spotify is a digital music, podcast, and video service that gives you access to millions of songs and other content from creators all over the world.**

**Basic functions such as playing music are totally free, but you can also choose to upgrade to Spotify Premium.**

**Whether you have Premium or not, you can:**

**✴ Get recommendations based on your taste**

**✴ Build collections of music and podcasts**

 **And more! **
"""

df=pd.read_csv("/content/drive/MyDrive/spotify dataset.csv")
df.head(3)

df = df.dropna()

import matplotlib.pyplot as plt
import seaborn as sns
plt.hist(df['duration_ms'], bins=30)
plt.xlabel('Song Duration')
plt.ylabel('Count')
plt.title('Distribution of Song Durations')
plt.show()

sns.scatterplot(data=df, x='danceability', y='energy')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.title('Danceability vs. Energy')
plt.show()

correlation_matrix = df.corr()

# Plot the correlation matrix using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Import the necessary libraries for clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Prepare the data for clustering
X = df[['loudness', 'speechiness', 'acousticness']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform clustering using K-means algorithm
kmeans = KMeans(n_clusters=5)
kmeans.fit(X_scaled)

# Add cluster labels to the dataset
df['cluster'] = kmeans.labels_

# Plot clusters based on playlist genres
sns.scatterplot(data=df, x='playlist_genre', y='loudness', hue='cluster')
plt.xlabel('Playlist Genre')
plt.ylabel('loudness')
plt.title('Clusters based on Playlist Genres')
plt.show()

# Import the necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Prepare the data for content-based recommendation
corpus = df['playlist_genre']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Calculate the similarity matrix
similarity_matrix = cosine_similarity(X)

# Function to recommend similar playlists based on a given playlist
def recommend_playlists(playlist_index, num_recommendations):
    playlist_similarity = similarity_matrix[playlist_index]
    similar_playlists_indices = playlist_similarity.argsort()[::-1][1:num_recommendations+1]
    similar_playlists = df.loc[similar_playlists_indices]['playlist_name']
    return similar_playlists

# Example usage: Recommend 5 similar playlists to the playlist at index 0
recommendations = recommend_playlists(0, 5)
print(recommendations)