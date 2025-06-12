import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Movie': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5', 'Movie 6', 'Movie 7', 'Movie 8'],
    'Genre': ['Comedy', 'Drama', 'Action', 'Comedy', 'Action','Drama', 'Action', 'Comedy'],
    'IMDB_Rating': [7.8, 8.2, 5.4, 9.0, 7.0, 8.1, 5.9, 6.5],
    'Views_Million': [ 200, 130, 110, 180, 90, 250, 60, 150]
}

df = pd.DataFrame(data)
sns.barplot(x='Genre', y='IMDB_Rating', data=df)
plt.title('Average IMDB Rating by Genre')
plt.show()

sns.boxplot(x='Genre', y='Views_Million', data=df)
plt.title('Distribution of Views by Genre')
plt.show()

sns.scatterplot(x='IMDB_Rating', y='Views_Million', hue='Genre', data=df, s=100)
plt.title('Relationship Between IMDB Rating and Views')
plt.show()

sns.countplot(x='Genre', data=df)
plt.title('Number of Movies by Genre')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='Genre', y='IMDB_Rating', data=df, showfliers=False)
sns.swarmplot(x='Genre', y='IMDB_Rating', data=df, color='black', alpha=0.7)
plt.title('IMDB Rating Distribution by Genre')
plt.show()