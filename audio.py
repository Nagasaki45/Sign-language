import urllib2
s = 'http://translate.google.com/translate_tts?tl=en&q='
audio_dir = 'audio/'
 
def word_to_url(word):
    return s + urllib2.quote(word.encode('utf8'))
 
def get_mp3_file(address, item):
    url = address
    request = urllib2.Request(url)
    request.add_header('User-agent', 'Mozilla/5.0')
    opener = urllib2.build_opener()
    f = open(audio_dir + item + ".mp3", "wb")
    f.write(opener.open(request).read())
    f.close()
 
def play_sound(name):
    from subprocess import call
    # for linux: mpg123
    # for mac: afplay
    call(['mpg123', audio_dir + item +'.mp3'])
 
if __name__ == "__main__":
    for item in ['hello',
                 'how are you feeling?',
                 'tired','was it hard?',
                 'beep',
                 'we should do it again',
                 'sure',
                 'have a great week',
                 'you too','goodbye',
                 'thank you',
                 'where is the bathroom?',
                 'i need a drink',
                 'i',
                 'you',
                 'pardon my english']:
        address = word_to_url(item)
        # get_mp3_file(address,item)
        play_sound(item)