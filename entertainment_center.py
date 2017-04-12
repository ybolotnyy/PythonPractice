import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://images.static-bluray.com/movies/covers/40179_front.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://images-na.ssl-images-amazon.com/images/I/511pMVAwuAL.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, school_of_rock, ratatouille]

fresh_tomatoes.open_movies_page(movies)