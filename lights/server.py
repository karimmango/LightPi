#!/usr/bin/env python2
import os
import pyglet
import pifacedigitalio
from flask import Flask

app = Flask(__name__)
PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



@app.route("/off")
def off():
    pifacedigital = pifacedigitalio.PiFaceDigital()
    pifacedigital.leds[2].toggle()
    return 'Success!\n'


@app.route("/on")
def on():
    pifacedigital = pifacedigitalio.PiFaceDigital()
    pifacedigital.leds[0].toggle()
    pifacedigital.leds[1].toggle()
    music = pyglet.resource.media('{}/mysound.mp3'.format(PACKAGE_ROOT_DIR))
    music.play()
    return 'Go fix the build.\n'


def run():
    try:
        app.run(host='0.0.0.0', debug=True, use_reloader=True)
    except KeyboardInterrupt:
        pass
