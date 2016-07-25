#!/usr/bin/env python2
import os
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
    lightsOn()
    os.system("echo 'failed.' | festival --tts")
    return 'Go fix the build.\n'

@app.route("/on/<message>")
def onWithMessage(message):
    lightsOn()
    os.system("echo '{0}' | festival --tts".format(message))
    return message


def lightsOn():
    pifacedigital = pifacedigitalio.PiFaceDigital()
    pifacedigital.leds[1].toggle()
    pifacedigital.leds[0].toggle()

def run():
    try:
        app.run(host='0.0.0.0', debug=True, use_reloader=True)
    except KeyboardInterrupt:
        pass
