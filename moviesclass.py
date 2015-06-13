# Camacho - Main Movie class, instatiates with the three necessary
# parameters, added some get functions for them as well
class Movie:
    def __init__(self,title,posterurl,youtube,year,starring,imdb):
        self.title = title
        self.poster_image_url = posterurl
        self.trailer_youtube_url = youtube
        self.release_year = year
        self.starring = starring
        self.imdb = imdb
# Camacho - Added 3 get functions for the hell of it
    def getTitle(self):
        return self.title

    def getPosterUrl(self):
        return self.posterurl

    def getYoutube(self):
        return self.youtube

# Camacho - Created three movie objects
Tarantula = Movie('Tarantula',
                  'http://upload.wikimedia.org/wikipedia/commons/9/9c/Tarantula_1955.jpg',
                  'https://www.youtube.com/watch?v=WtU1YYxQXJw',
                  '1955',
                  'John Agar',
                  'http://www.imdb.com/title/tt0048696/?ref_=nv_sr_1')

BladeRunner = Movie('Blade Runner',
                    'http://www.impawards.com/1982/posters/blade_runner_xlg.jpg',
                    'https://www.youtube.com/watch?v=xP4WvJaMfj8',
                    '1982',
                    'Harrison Ford',
                    'http://www.imdb.com/title/tt0083658/?ref_=nv_sr_1')

ABeautifulMind = Movie('A Beautiful Mind',
                       'http://fontmeme.com/images/A-Beautiful-Mind-Poster.jpg',
                       'https://www.youtube.com/watch?v=aS_d0Ayjw4o',
                       '2001',
                       'Russel Crowe',
                       'http://www.imdb.com/title/tt0268978/?ref_=nv_sr_1')

# Camacho - Placed each of the movies in a list
movielist = [Tarantula,BladeRunner,ABeautifulMind]