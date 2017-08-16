import media
import fresh_tomatoes

'''
This intances are setting up space for
each intance and their own instance variables
'''
upWiki = "https://upload.wikimedia.org/wikipedia/en/"
toy_story_3 = media.Movie(
    "Toy Story 3",
    "A story of a boy and his toys that come to life.",
    upWiki+"6/69/Toy_Story_3_poster.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg",
    media.Movie.VALID_RATINGS[0]
)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io",
    media.Movie.VALID_RATINGS[2]
)

your_name = media.Movie(
    "Your Name",
    "Couple of teens that switch body when they sleep.",
    "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
    "https://www.youtube.com/watch?v=xU47nhruN-Q",
    media.Movie.VALID_RATINGS[2]
)


dragonheart = media.Movie(
    "dragonheart",
    "A former knight and a dragon join forces to save a kingdom.",
    upWiki+"thumb/1/18/Dragonheart_ver1.jpg/220px-Dragonheart_ver1.jpg",
    "https://www.youtube.com/watch?v=SF9tgeo1HuA",
    media.Movie.VALID_RATINGS[1]
)

the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "A smart banker is sentenced to prison, will he survive?",
    upWiki+"8/81/ShawshankRedemptionMoviePoster.jpg",
    "https://www.youtube.com/watch?v=NmzuHjWmXOc",
    media.Movie.VALID_RATINGS[3]
)

forrest_gump = media.Movie(
    "Forrest Gump",
    "A disadvantaged man overcomes his disability" +
    " while going through important historical events.",
    upWiki+"thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg",
    media.Movie.VALID_RATINGS[2]
)

chappie = media.Movie(
    "Chappie",
    "A robot with human emotions",
    upWiki+"thumb/7/71/Chappie_poster.jpg/220px-Chappie_poster.jpg",
    "https://www.youtube.com/watch?v=lyy7y0QOK-0",
    media.Movie.VALID_RATINGS[3]
)

iron_man = media.Movie(
    "Iron Man",
    "A smart rich inventor makes a metal weapon suit and becomes a hero.",
    upWiki+"thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY",
    media.Movie.VALID_RATINGS[3]
)

movies = [
    your_name,
    avatar, dragonheart,
    the_shawshank_redemption,
    forrest_gump, toy_story_3,
    chappie,
    iron_man
]

fresh_tomatoes.open_movies_page(movies)
