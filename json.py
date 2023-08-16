import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Creed", "year": 2015}

]

data = json.dumps(movies)
Path("movies.json")