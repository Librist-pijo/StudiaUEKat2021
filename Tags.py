import csv
import json
from flask_restful import reqparse, abort, Api, Resource

class Tags:
    def __init__(self,userid,movieid,tag,timestamp):
        self.userid = userid
        self.movieid = movieid
        self.tag = tag
        self.timestamp = timestamp

listOfTags = []
with open('tags.csv', 'r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        listOfTags.append(Tags(row[0],row[1],row[2],row[3]).__dict__)

class TagList(Resource):
    def get(self):
        return listOfTags