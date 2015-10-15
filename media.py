

class Movie():
    # title is the only required argument
    def __init__(self, title, storyline=None, poster_image_url=None, trailer_youtube_url=None,
                rated=None, runtime=None):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rated = rated
        self.runtime = runtime

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
