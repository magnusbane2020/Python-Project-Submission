import requests
from bs4 import BeautifulSoup

class MovieScraper:
    def __init__(self, headers):
        self.headers = headers

    def fetch_url_content(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')  # Using html.parser
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None

    def scrape_movies(self, url, genre):
        content = self.fetch_url_content(url)
        if not content:
            return []

        movie_list = []
        for movie in content.select('.ipc-metadata-list-summary-item'):
            try:
                title = movie.select_one('.ipc-title__text').get_text().strip()
                year = movie.select('.sc-b189961a-8.kLaxqf.dli-title-metadata-item')[0].text.strip()
                certification = movie.select('.sc-b189961a-8.kLaxqf.dli-title-metadata-item')[2].text.strip()
                runtime = movie.select('.sc-b189961a-8.kLaxqf.dli-title-metadata-item')[1].text.strip()
                imdb_rating = movie.select_one('.ipc-rating-star--imdb').text.strip()
                plot = movie.select_one('.ipc-html-content-inner-div').get_text().strip()
                number_of_votes = movie.select_one('.ipc-rating-star--voteCount').text.strip()
                metascore = movie.select_one('.sc-b0901df4-0.bcQdDJ.metacritic-score-box')
                metascore = metascore.text.strip() if metascore else "0"

                movie_data = {
                    "title": title,
                    "year": year,
                    "certification": certification,
                    "runtime": runtime,
                    "genre": genre,
                    "imdb_rating": imdb_rating,
                    "metascore": metascore,
                    "plot": plot,
                    "number_of_votes": number_of_votes
                }
                movie_list.append(movie_data)
            except (IndexError, AttributeError) as e:
                print(f"Index error: {e}")
                continue
        return movie_list
