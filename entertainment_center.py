import movies
import fresh_tomatoes


#list of movies & attributes used in website
#-------
step_brothers = movies.Movie(
	"Step Brothers",
	"Two grown children do a bunch of goofy stuff",
	"https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
	"https://www.youtube.com/watch?v=CewglxElBK0")
george_jungle = movies.Movie(
	"George of the Jungle",
	"A Man raised in the jungle goes on an adventure",
	"https://upload.wikimedia.org/wikipedia/en/f/f8/George_Of_The_Jungle.jpg",
	"https://www.youtube.com/watch?v=_OHAUghSoEA")
goldeneye = movies.Movie(
	"Goldeneye",
	"James Bond takes on an evil villan",
	"https://upload.wikimedia.org/wikipedia/en/2/24/GoldenEye_-_UK_cinema_poster.jpg",
	"https://www.youtube.com/watch?v=HHFXthl5IJo")
gilmore = movies.Movie(
	"Happy Gilmore",
	"A crazy amature golfer takes on the pros",
	"https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
	"https://www.youtube.com/watch?v=-6sT7MSJ4GE")
hot_shots = movies.Movie(
	"Hot Shots!",
	"A spoof on Top Gun",
	"https://upload.wikimedia.org/wikipedia/en/b/b5/Hot_Shots_2.jpg",
	"https://www.youtube.com/watch?v=WjDhBBUOEdo")
bourne = movies.Movie(
	"The Bourne Ultimatum",
	"A brainwashed assasin discovers his past",
	"https://upload.wikimedia.org/wikipedia/en/f/fe/The_Bourne_Ultimatum_%282007_film_poster%29.jpg",
	"https://www.youtube.com/watch?v=N6J2oiKJr-A")
#--------


movie_list = [step_brothers, george_jungle, goldeneye, gilmore, hot_shots, bourne]

fresh_tomatoes.open_movies_page(movie_list)	








