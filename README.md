# Sign-language

A sign-language to speech application that uses the [LeapMotion](http://leapmotion.com/) to track gestures and the [WekiMini](http://wekinator.org/) to map gestures to sentences.

The project was originally created in the Hack2Wear hackathon (2014), together with Ilai Giloh and Mel.

## How to run it?

1. First, you will have to install the [WekiMini](http://wekinator.org/).

1. In addition, I use [leap_python3](https://github.com/Nagasaki45/leap_python3) as a git submodule, so make sure to pull the submodule and compile it (see instruction in the link) before running.

1. Install the rest of the dependencies with `pip install -r requirements` (preferably into a virtuel env).

1. Make sure you have a [voice rss](http://voicerss.org/) key, to convert text to speech. Get one and export it with `export VOICE_RSS_KEY=<YOUR KEY>`.

  > If you are using [autoenv](https://github.com/horosgrisa/autoenv) you can write the above line to a `secrets` file and it will be sourced when you change into the project directory.

1. Start the WekiMini. In the input section choose 30 inputs and in the output section choose the type: "All dynamic time warping" with `X` gesture types where `X` is the number of expected sentences you want to work with. Hit next.

1. Run `./sign_language.py`. It will start to pass data from the LeapMotion to the WekiMini and get data back to convert to audio and say them.

  > Some WekiMini functions are still not fully automated. You will have to find the sweet spot of the threshold slider manually using the WekiMini GUY.

1. Enjoy
