import subprocess
import requests
import os

KEY = os.environ['VOICE_RSS_KEY']


def play(filepath):
    """Play an audio file."""
    call(['mpg123', filepath])


def call(args):
    """Call another process, don't show it's output."""
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()


def get_audio_file(text):
    """Download a text to speech file from Voice RSS."""
    query_params = {'key': KEY, 'src': text}
    response = requests.get('http://api.voicerss.org/', params=query_params)
    with open(text_filepath(text), "wb") as f:
        f.write(response.content)


def text_filepath(text):
    return os.path.join('audio', text + '.mp3')


def say(text):
    """Say the provided text using text to speech."""
    filepath = text_filepath(text)
    if not os.path.exists(filepath):
        get_audio_file(text)
    play(filepath)
