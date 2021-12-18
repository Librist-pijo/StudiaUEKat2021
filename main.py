from Links import LinkList
from Movies import MovieList
from Tags import TagList
from Ratings import RatingList
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(MovieList, '/movies')
api.add_resource(LinkList, '/links')
api.add_resource(RatingList, '/ratings')
api.add_resource(TagList, '/tags')


if __name__ == '__main__':
    app.run(debug=True)