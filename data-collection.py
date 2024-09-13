import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials;
import billboard
import datetime 
import database as db

client_id = "61194f97e30e4e4d8bbcd887a261beab"
client_secret = "568099ff140c4996a59fca184bef60b2"
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, retries = 10, status_retries = 10, backoff_factor = 2)

date = datetime.datetime(2018, 1, 1)
endDate = datetime.datetime(2023, 12, 31)
deltaWeek = datetime.timedelta(7)

valences = []
leftovers = []

while (date < endDate):
    chart = billboard.ChartData('hot-100', date = date.strftime("%Y-%m-%d"), fetch = True)
    print(date)
    valenceSum = 0
    weekLeftovers = []
    songIDs = []
    for song in chart:
        try:
            songID = db.getSongID(song.title.split(" (")[0].replace("'", ""), song.artist.split(" Featuring ")[0].split(" & ")[0].split(" X ")[0].split(",")[0])
            songIDs.append(songID)
            print("worked " + song.title)
        except:
            weekLeftovers.append((song.title, song.artist))
            print("broke " + song.title)
    features = sp.audio_features(songIDs)
    for track in features:
        valenceSum += track["valence"]
        print(track["valence"])
    print(valenceSum/100)
    valences.append((date, valenceSum/100))
    leftovers.append((date, weekLeftovers))
    date = date + deltaWeek
db.save(valences, "valences")
db.save(leftovers, "leftovers")




