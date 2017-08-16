import webbrowser


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    """
    This class provides a way to store movie related information
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] is lesson 10
    constants
    class variables
    """

    '''
    self is the object being created so toy_story is it

    constructor also self is toy_story, Avatar, or YourName
    '''
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        valid_ratings
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.valid_rated = valid_ratings

    """
    instance method
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
