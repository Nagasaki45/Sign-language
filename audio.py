import urllib2
import os

AUDIO_DIR = 'audio'
URL = 'http://translate.google.com/translate_tts?tl=en&q='

 
def word_to_url(word):
    return URL + urllib2.quote(word.encode('utf8'))
 
def get_mp3_file(address, item):
    url = address
    request = urllib2.Request(url)
    request.add_header('User-agent', 'Mozilla/5.0')
    opener = urllib2.build_opener()
    with open(os.path.join(AUDIO_DIR, item + ".mp3"), "wb") as f:
        f.write(opener.open(request).read())
 
def play_sound(name):
    from subprocess import call
    # for mac: afplay
    # windows:
    # call(['vlc', '--play-and-exit', os.path.join(AUDIO_DIR, name + ".mp3")])
    # linux:
    call(['mpg123', os.path.join(AUDIO_DIR, name + ".mp3")])
    
def text2speech(item):
    if not item + '.mp3' in os.listdir(AUDIO_DIR):
        print 'downloading'
        get_mp3_file(word_to_url(item), item)
        
    play_sound(item)
