import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import csv

app = Flask(__name__)
api = Api(app)


class Movies:
    def __init__(self,id:int,title: str,genres:str):
        self.id = id
        self.title = title
        self.genres = genres

class Links:
    def __init__(self,movieid:int,imdbid:int,tmdbid:int):
        self.movieid = movieid
        self.imdbid = imdbid
        self.tmdbid = tmdbid

class Ratings:
    def __init__(self,userid,movieid,rating,timestamp):
        self.userid = userid
        self.movieid = movieid
        self.rating = rating
        self.timestamp = timestamp

class Tags:
    def __init__(self,userid,movieid,tag,timestamp):
        self.userid = userid
        self.movieid = movieid
        self.tag = tag
        self.timestamp = timestamp


listOfMovies = []
with open('movies.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfMovies.append(Movies(row[0],row[1],row[2]).__dict__)

listOfLinks = []
with open('links.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfLinks.append(Links(row[0],row[1],row[2]).__dict__)

listOfRatings = []
with open('ratings.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfRatings.append(Ratings(row[0],row[1],row[2],row[3]).__dict__)

listOfTags = []
with open('tags.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfTags.append(Tags(row[0],row[1],row[2],row[3]).__dict__)

class MovieList(Resource):
    def get(self):
        return listOfMovies

class LinkList(Resource):
    def get(self):
        return listOfLinks

class RatingList(Resource):
    def get(self):
        return listOfRatings

class TagList(Resource):
    def get(self):
        return listOfTags

##
## Actually setup the Api resource routing here
##
api.add_resource(MovieList, '/movies')
api.add_resource(LinkList, '/links')
api.add_resource(RatingList, '/ratings')
api.add_resource(TagList, '/tags')


if __name__ == '__main__':
    app.run(debug=True)