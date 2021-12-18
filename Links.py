import csv
import json
from flask_restful import reqparse, abort, Api, Resource

class Links:
    def __init__(self,movieid:int,imdbid:int,tmdbid:int):
        self.movieid = movieid
        self.imdbid = imdbid
        self.tmdbid = tmdbid

listOfLinks = []
with open('links.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfLinks.append(Links(row[0],row[1],row[2]).__dict__)


class LinkList(Resource):
    def get(self):
        return listOfLinks