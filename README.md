# Sign-language

A sign-language to speech application that uses the [LeapMotion](http://leapmotion.com/) to track gestures and the [WekiMini](http://wekinator.org/) to map gestures to sentences.

The project was originally created in the Hack2Wear hackathon (2014), together with Ilai Giloh and Mel.

## How to run it?

### Dependencies

First, you will have to install the [WekiMini](http://wekinator.org/). In addition, I use [leap_python3](https://github.com/Nagasaki45/leap_python3) as a git submodule, so make sure to pull the submodule and compile it (see instruction in the link) before running.

Create virtual environment:

    virtualenv env
    source env/bin/activate

You will also need a [voice rss](http://voicerss.org/) key, to convert text to speech. Get one and run:

    export VOICE_RSS_KEY=<YOUR KEY>

If you are using [autoenv](https://github.com/horosgrisa/autoenv) you can write the above line to a `secrets` file and it will be sourced when you change into the project directory.

### Run

Start the WekiMini. In the input section choose 30 inputs and in the output section choose the type: "All dynamic time warping" with `X` gesture types where `X` is the number of expected sentences you want to work with. Hit next.

You will have to manually set the "Gesture OSC message" for each output to sentences, with leading `/` and underscores instead of spaces.

Now run `./sign_language.py`. It will start to pass data from the LeapMotion to the WekiMini and get data back to convert to audio and say them.

## Future development

The next step is to create a web interface, where users will be able to write sentences, hit record, and perform a gesture. I hope that with enough automation of the WekiMini it will be much easier to add new sentences and change gestures on the fly.
