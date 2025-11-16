import json

import requests


class MovieRepository:
    def __init__(self, api_key = 'test'):
        self.movies = []
        self._load()
        self.url = f'https://www.omdbapi.com/?apikey={api_key}&'

    def _load(self):
        try:
            with open('movies.json', 'r', encoding='utf-8') as f:
                self.movies = [movie for movie in json.load(f)]
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None

    def get_movies(self):
        return self.response(json.dumps(self.movies, ensure_ascii=False))

    def index(self):
        with open("page.html", "r", encoding="utf-8") as f:
            content = f.read()

        return self.response(content, 'text/html')

    def online_movies(self):
        with open("online-page.html", "r", encoding="utf-8") as f:
            content = f.read()

        return self.response(content, 'text/html')

    def about(self):
        content = "<h1>About page</h1>"
        return self.response(content, 'text/html')

    def search(self, search):
        url = self.url + 's=' + search + '&'
        resp = requests.get(url, timeout=10)
        data = resp.json()
        return self.response(json.dumps(data, ensure_ascii=False), 'application/json')

    def response(self, body, content_type = 'application/json'):
        if content_type == 'application/json':
            return (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json; charset=utf-8\r\n"
                "Access-Control-Allow-Origin: *\r\n"
                "\r\n"
                f"{body}"
            )
        else:
            return (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                f"{body}"
            )

