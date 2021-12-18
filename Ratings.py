import csv
import json
from flask_restful import reqparse, abort, Api, Resource

class Ratings:
    def __init__(self,userid,movieid,rating,timestamp):
        self.userid = userid
        self.movieid = movieid
        self.rating = rating
        self.timestamp = timestamp

listOfRatings = []
with open('ratings.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfRatings.append(Ratings(row[0],row[1],row[2],row[3]).__dict__)

class RatingList(Resource):
    def get(self):
        return listOfRatings