import webbrowser


# class 'Movie' is the data structure holding all details of the movies
class Movie():
    # initialization function
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_img,
            trailer_youtube,
            movie_genre):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_img_url = poster_img
        self.trailer_youtube_url = trailer_youtube
        self.genre = movie_genre

    # function to play trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

