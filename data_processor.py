import pandas as pd
import random

class MovieDataProcessor:
    def __init__(self, csv_file):
        try:
            self.movie_df = pd.read_csv(csv_file)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            self.movie_df = pd.DataFrame()

    @property
    def unique_genres(self):
        unique_genre_set = set()
        for genre in self.movie_df['genre'].str.split(', '):
            unique_genre_set.update(genre)
        return list(unique_genre_set)

    def recommend_movie(self, selected_genre):
        genre_df = self.movie_df[self.movie_df['genre'].str.contains(selected_genre, na=False)]
        genre_df.reset_index(drop=True, inplace=True)

        if genre_df.empty:
            return {}

        random_index = random.randint(0, genre_df.shape[0] - 1)
        selected_movie = genre_df.loc[random_index]

        movie_info = {
            'title': selected_movie['title'],
            'year': selected_movie['year'],
            'certification': selected_movie['certification'],
            'runtime': selected_movie['runtime'],
            'genre': selected_movie['genre'],
            'imdb_rating': selected_movie['imdb_rating'],
            'metascore': selected_movie['metascore'],
            'number_of_votes': selected_movie['number_of_votes'],
            'plot': selected_movie['plot']
        }
        return movie_info
