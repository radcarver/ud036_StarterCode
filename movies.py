import webbrowser



class Movie():
	'''
	Creates a class, Movie, to storing movie information and open movie trailers

	Attributes:
		title: Title of the movie
		storyline: One line summary of the movie
		poster_image_url: URL of the poster from wikipedia
		trailer_youtube_url: YouTube URL of the trailer
	'''

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		''' initializes title, storyline, poster_image_url and trailer_youtube_url '''
		self.title =  movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def showtrailer(self):
		''' opens the trailer in the user's browser''' 
		webbrowser.open(self.trailer_youtube_url)


