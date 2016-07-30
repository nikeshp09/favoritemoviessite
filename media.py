import webbrowser
class Movie():
    """All movies that generate are a few of my all-time favorite."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_trailer, movie_storyline,
                 poster_image, trailer_youtube, VALID_RATINGS):
        self.title = movie_trailer # Title  
        self.storyline = movie_storyline # Storyline from IMBD  
        self.poster_image_url = poster_image # Movie Poster Image URL's  
        self.trailer_youtube_url = trailer_youtube #Youtube Trailer
        self.VALID_RATINGS = VALID_RATINGS
        
# Shows Trailer from Youtube  
    def show_trailer(self):
        webbrowser.open(self.trailer_youtuble_url)
