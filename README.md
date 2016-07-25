# LightPi
This is a Raspberry Pi experiment, utilizing the addon Piface to the Raspberry Pi to connect speakers, warning tower light, and siren combined with code in Python to simultaneously fire off the lights and play an mp3 file.

Running:
----------

    $ cd LightPi
    $ python server.py

It should create service running on port 5000 on the raspberry pi ip address

This app uses a native lib called festival and requires its installation:

      - $ sudo apt-get install festival
