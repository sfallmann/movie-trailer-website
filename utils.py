''' Contains the function get_movie which gets movie infor rom omdbapi.com '''
from urllib import urlopen
from media import Movie
import json


# Using www.omdbapi.com to get movie information
OMDB_API = 'http://omdbapi.com/?type=movie&r=json&t='

def get_movie(title):

    # Get the movie info from the api
    movie_json = urlopen(OMDB_API + title)
    # Set info to output
    info = movie_json.read()
    # close the request
    movie_json.close()
    # decode from json to a dictionary
    info = json.loads(info)

    # create an instance of movie with data
    movie = Movie(
        title = title,
        storyline = info["Plot"],
        poster_image_url = info["Poster"],
        rated = info["Rated"],
        runtime = info["Runtime"]
    )
    if movie.rated == "NOT RATED":
        movie.rated = "NOT-RATED"
    # return movie
    return movie
