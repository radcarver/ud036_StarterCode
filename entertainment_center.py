import movies
import fresh_tomatoes

step_brothers = movies.Movie("Step Brothers",
	"Two grown children do a bunch of goofy stuff",
	"https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
	"https://www.youtube.com/watch?v=CewglxElBK0")

#print step_brothers.storyline

#step_brothers.showtrailer()


movies2 = []
for _ in range (0,8):
	movies2.append(step_brothers)

#fresh_tomatoes.open_movies_page(movies)	
print(movies.Movie.__module__)







