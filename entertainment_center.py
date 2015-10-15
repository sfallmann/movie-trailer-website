'''  The file that needs to be executed to make the webpage '''
# Import function and classes
import webbrowser
from media import Movie
from utils import get_movie
from fresh_tomatoes import create_movie_tiles_content, open_movies_page


# Passing the movie name into the get_movie function
# which returns an instance of Movie.
# Since the api used doesn't supply the trailer,
# the trailer is set after instantiation
conan = get_movie("Conan the Barbarian")
conan.trailer_youtube_url = "https://www.youtube.com/watch?v=xwdYd_RdLCQ"

fellowship = get_movie("The Fellowship of the Ring")
fellowship.trailer_youtube_url = "https://www.youtube.com/watch?v=V75dMMIW2B4"

empire = get_movie("The Empire Strikes Back")
empire.trailer_youtube_url = "https://www.youtube.com/watch?v=96v4XraJEPI"

ghostbusters = get_movie("Ghostbusters")
# Broken into two lines to meet PEP8 requirement
ghostbusters.trailer_youtube_url = "https://www.youtube.com/"
ghostbusters.trailer_youtube_url += "watch?v=vntAEVjPBzQ"

good_bad_ugly = get_movie("The Good, the Bad and the Ugly")
# Broken into two lines to meet PEP8 requirement
good_bad_ugly.trailer_youtube_url = "https://www.youtube.com/"
good_bad_ugly.trailer_youtube_url += "watch?v=WCN5JJY_wiA"

minority_report = get_movie("Minority Report")
# Broken into two lines to meet PEP8 requirement
minority_report.trailer_youtube_url = "https://www.youtube.com/"
minority_report.trailer_youtube_url += "watch?v=jdl6eAIx2K4"

#  Create a list of movies
movies = [conan, fellowship, empire, ghostbusters,
          good_bad_ugly, minority_report]

# invoke the function open_movies_page
# to open the movies page
open_movies_page(movies)
