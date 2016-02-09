# Sign-language

A sign-language to speech application that uses the LeapMotion to track gestures, map the gestures into (currently) predefined sentences and say them.

The project was originally created in the TODO hackathon, together with TODO and TODO.

## How to run it?
I use [leap_python3](https://github.com/Nagasaki45/leap_python3) as a git submodule, so make sure to pull the submodule and compile it (see instruction in the link) before running.

Create a conda virtual environment:

    conda env create -f environment.yml
    conda activate Sign-language

You will also need a [voice rss](TODO link) key, to convert text to speech. Get one and run:

    export VOICE_RSS_KEY=f6a018e61f054a649596fc721e04a2e4

If you are using [autoenv](https://github.com/horosgrisa/autoenv) you can write the above line to a `secrets` file and it will be sourced when you change into the project directory.

## Future development

The next step is to create a web interface, where users will be able to write sentences, hit record, perform a gesture and create a gesture to speech mapping dynamically.

It will be based on the [WekiMini](http://www.wekinator.org/) project.
