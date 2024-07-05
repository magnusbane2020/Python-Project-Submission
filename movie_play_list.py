from tkinter import *
from tkinter import ttk
import pandas as pd
from scraperIMDB import MovieScraper  # Ensure this module is created with appropriate methods
from data_processor import MovieDataProcessor  # Ensure this module is created with appropriate methods

# Constants
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}
AVAILABLE_GENRES = [
    "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Family",
    "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery",
    "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"
]
CSV_FILE = "my_list_of_movies.csv"

# Initialize movie processor globally
movie_processor = None


def display_movie_info(row, key, value):
    Label(text=key, height=2, width=20, font=("Arial", 14, 'bold'), bg='#FF7F50', fg='white', anchor="w").grid(row=row, column=0)
    Label(text=value, height=3, width=100, font=("Arial", 12), bg='#FF7F50', fg='white', anchor="w", wraplength=800,
          justify='left').grid(row=row, column=1)


def clear_movie_info():
    for row in range(30, 39):
        Label(text='', height=2, width=20, font=("Arial", 14, 'bold'), bg='#F0F0F0', anchor="w").grid(row=row, column=0)
        Label(text='', height=3, width=100, font=("Arial", 12), bg='#F0F0F0', anchor="w", wraplength=800,
              justify='left').grid(row=row, column=1)


def recommend():
    selected_genre = genre_var.get()
    if not selected_genre:
        return

    movie_info = movie_processor.recommend_movie(selected_genre)
    if movie_info:
        display_movie_info(30, '', '')
        display_movie_info(31, 'Movie name', movie_info['title'])
        display_movie_info(32, 'Year', movie_info['year'])
        display_movie_info(33, 'Certification', movie_info['certification'])
        display_movie_info(34, 'Runtime', movie_info['runtime'])
        display_movie_info(35, 'IMDb Rating', movie_info['imdb_rating'])
        display_movie_info(36, 'Metascore', movie_info['metascore'])
        display_movie_info(37, 'Number of Votes', movie_info['number_of_votes'])
        display_movie_info(38, 'Plot', movie_info['plot'])


def reset():
    genre_var.set('')
    clear_movie_info()


def close_app():
    app.quit()
    app.destroy()


def main():
    global movie_processor, genre_var, app

    # Initialize the movie scraper and data processor
    scraper = MovieScraper(HEADERS)
    movie_list = []
    for genre in AVAILABLE_GENRES:
        url = f"https://www.imdb.com/search/title/?genres={genre}&groups=top_1000"
        movie_list.extend(scraper.scrape_movies(url, genre))

    movie_dataframe = pd.DataFrame(movie_list)
    movie_dataframe.to_csv(CSV_FILE, index=False)

    movie_processor = MovieDataProcessor(CSV_FILE)
    unique_genres = movie_processor.unique_genres

    # Building the Tkinter App
    app = Tk()
    app.title('Choose a Genre and get a movie :)')
    app.attributes('-fullscreen', True)
    app.config(background="#98FF98")

    # UI components for genre selection and recommendation button
    banner = Label(
        text='Choose a film genre that interests you..\nWe will recommend a popular movie based on your preferences.',
        font=("Arial", 16, 'bold'), width=100, height=2, bg='#333333', fg='white'
    )
    banner.grid(row=0, column=0, columnspan=3)

    genre_var = StringVar()
    Label(text="Select the genre:", height=2, width=20, font=("Arial", 14, 'bold'), bg='#006400', fg='white',
          anchor="w").grid(row=5, column=0)
    ttk.Combobox(textvariable=genre_var, values=unique_genres, height=10, width=40, state='readonly').grid(row=5,
                                                                                                           column=1)

    Button(text="Suggest Movie", bg="#006400", fg='white', font="Arial", width=12, height=1, command=recommend).grid(row=7,
                                                                                                         column=1)
    Button(text="Reset", bg="#006400", fg='white', font="Arial", width=12, height=1, command=reset).grid(row=7, column=2)
    Button(text="Close", bg="#006400", fg='white', font="Arial", width=12, height=1, command=close_app).grid(row=7, column=3)

    # Start the Tkinter main loop
    app.mainloop()


if __name__ == '__main__':
    main()
