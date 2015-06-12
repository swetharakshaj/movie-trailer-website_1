import fresh_tomatoes
import media


# all the movies' details
casino_royale = media.Movie(
            "Casino Royale",
            "Bond sets out to defeat a weapons dealer",
            "http://goo.gl/U6M3XC",
            "https://www.youtube.com/watch?v=fl5WHj0bZ2Q",
            "Action")

troy = media.Movie(
            "Helen of Troy",
            "The Iliad's story of the Trojan war.",
            "http://upload.wikimedia.org/wikipedia/en/3/33/Troy_moviep.jpg",
            "https://www.youtube.com/watch?v=znTLzRJimeY",
            "Period/ Action/ Drama")

avatar = media.Movie(
            "Avatar",
            "A marine in an alien land",
            "http://goo.gl/kPGcT3",
            "https://www.youtube.com/watch?v=d1_JBMrrYw8",
            "Science Fiction")

godfather = media.Movie(
            "Godfather",
            "Italian don family's feud with another for power",
            "http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
            "https://www.youtube.com/watch?v=sY1S34973zA",
            "Drama")
pulp_fiction = media.Movie(
            "Pulp Fiction",
            "The lives of two mob hit men and a boxer \
            and a gangster's wife and a pair of diner \
            bandits intertwine in four tales of violence and redemption.",
            "http://goo.gl/S8CbiK",
            "https://www.youtube.com/watch?v=ewlwcEBTvcg",
            "Crime/ Comedy")
gravity = media.Movie(
            "Gravity",
            "A medical engineer and an astronaut work together to survive after a \
             catastrophe destroys their shuttle \
             and leaves them adrift in orbit.",
            "http://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
            "https://www.youtube.com/watch?v=OiTiKOy59o4",
            "Science Fiction")

# making a list of all the movies mentioned above
movies = [casino_royale, troy, avatar, godfather, pulp_fiction, gravity]
# pass this list to function that reads and displays in web page
fresh_tomatoes.open_movies_page(movies)
