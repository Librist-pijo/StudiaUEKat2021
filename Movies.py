import csv
import json
from flask_restful import reqparse, abort, Api, Resource

class Movies:
    def __init__(self,id:int,title: str,genres:str):
        self.id = id
        self.title = title
        self.genres = genres

listOfMovies = []
with open('movies.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfMovies.append(Movies(row[0],row[1],row[2]).__dict__)

class MovieList(Resource):
    def get(self):
        return listOfMovies