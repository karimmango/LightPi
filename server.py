#!/usr/bin/env python2
import pyglet
from pygame import mixer
import pifacedigitalio
from flask import Flask, url_for
from time import sleep

app = Flask(__name__)
users = { 'ON': 'ff', 'OFF': 'kk' }


@app.route("/ON/<OFF>")
def user(ON):
    f =  users.get(ON)
    t = '\n{}\n'
    if f:
        return t.format(f, "the light is on")
    else:
        return '\nthe light is off\n'

@app.route("/off")
def off():
    pifacedigital = pifacedigitalio.PiFaceDigital()
    pifacedigital.leds[2].toggle()
    return '\nSuccess!'

@app.route("/on")
def on():
    pifacedigital = pifacedigitalio.PiFaceDigital()
    pifacedigital.leds[0].toggle()
    pifacedigital.leds[1].toggle()
    music = pyglet.resource.media('mysound.mp3')
    music.play()
    return '\nGo fix the build.'

if __name__ == "__main__":
    try:
    	app.run(host='0.0.0.0', debug=True, use_reloader=True)
    except KeyboardInterrupt:
	pass
