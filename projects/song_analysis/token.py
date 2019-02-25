import sys
import spotipy as sp
import spotipy.util as util

credentials = {
    'scope': 'user-library-read',
    'username': 'rzera',
    'client_id': '52899fd885774f98ba9481e894e0d22e',
    'client_secret': '1280a1394bfe430ea08c11ef1caecaa8',
    'redirect_uri': 'myanalysis://dataset'}

token = util.prompt_for_user_token(**credentials)
print(token)
