import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Load your dataset (replace 'spotify-2023.csv' with your actual file path)
file_path = 'spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# 2. Set up Spotify API credentials
client_id = '5cb86911ffb34863925ff5b7ea0d8865'       # Replace with your Spotify Client ID
client_secret = '5b45189be7a544b28366c1887bef9a6b'  # Replace with your Spotify Client Secret

# 3. Authenticate using Spotipy
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 4. Function to get album cover URL using track name and artist
def get_album_cover_url(track_name, artist_name):
    try:
        # Search for the track on Spotify
        query = f"track:{track_name} artist:{artist_name}"
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            album_cover_url = results['tracks']['items'][0]['album']['images'][0]['url']
            return album_cover_url
    except Exception as e:
        print(f"Error fetching album cover: {e}")
    return None

# 5. Apply the function to your dataset
spotify_data['album_cover_url'] = spotify_data.apply(
    lambda row: get_album_cover_url(row['track_name'], row['artist(s)_name']), axis=1)

# 6. Save the updated dataset with album cover URLs
spotify_data.to_csv('spotify_with_album_covers.csv', index=False)
print("Updated dataset saved as 'spotify_with_album_covers.csv'")

# 7. Display a few rows to verify
print(spotify_data[['track_name', 'artist(s)_name', 'album_cover_url']].head())
