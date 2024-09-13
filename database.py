import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date
import pickle


client_id = "61194f97e30e4e4d8bbcd887a261beab"
client_secret = "568099ff140c4996a59fca184bef60b2"
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class Song:
    id = None
    def __init__(self, id):
        self.id = id
        # TODO create another spotipy thing to get the song artist and name 
        features = sp.audio_features(id)
        for track in features:
            self.acousticness = track['acousticness']
            self.danceability = track['danceability']
            self.energy = track['energy']
            self.instrumentalness = track['instrumentalness']
            self.liveness = track['liveness']
            self.loudness = track['loudness']
            self.tempo = track['tempo']
            self.valence = track['valence']


class Album:
    #TODO Figure out optional and keyword arguments
    def __init__(self):
        self.songs = []
        self.date = None

    def __init__(self, songs: list):
        self.songs = songs
        self.date = None

    def __init__(self, date: date):
        self.songs = []
        self.date = date
    
    def __init__(self, songs: list, date: date):
        self.songs = songs
        self.date = date

    def addSong(self, song: Song):
        self.songs.append(song)
    
    def getDanceability(self):
        sum = 0.0
        for song in self.songs:
            sum += song.danceability
        return sum / len(self.songs)
    
    def getInstrumentalness(self):
        sum = 0.0
        for song in self.songs:
            sum += song.instrumentalness
        return sum / len(self.songs)
    
    def getLiveness(self):
        sum = 0.0
        for song in self.songs:
            sum += song.liveness
        return sum / len(self.songs)
    
    def getLoudness(self):
        sum = 0.0
        for song in self.songs:
            sum += song.loudness
        return sum / len(self.songs)
    
    def getTempo(self):
        sum = 0.0
        for song in self.songs:
            sum += song.tempo
        return sum / len(self.songs)
    
    def getValence(self):
        sum = 0.0
        for song in self.songs:
            sum += song.valence
        return sum / len(self.songs)
    
def save(obj, fileName: str):
    with open(fileName + ".pkl", mode="wb") as opened_file:
        pickle.dump(obj, opened_file)

def load(fileName: str):
    with open(fileName + ".pkl", mode="rb") as opened_file:
        obj = pickle.load(opened_file)
    return obj

def getSongID(songName: str, artist: str):
    return sp.search(q='artist:' + artist + ' track:' + songName , type='track')['tracks']['items'][0]['id']

def getFeature(songID: str, feature: str):
    features = sp.audio_features(songID)
    for track in features:
        return track[feature]