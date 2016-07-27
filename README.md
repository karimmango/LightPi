# LightPi
This is a Raspberry Pi experiment, utilizing the addon Piface to the Raspberry Pi to connect speakers, warning tower light, and siren combined with code in Python to simultaneously fire off the lights and play an mp3 file.

Running:
----------

    $ cd LightPi
    $ python server.py

It should create service running on port 5000 on the raspberry pi ip address

This app uses a native lib called festival and requires its installation:

      - $ sudo apt-get install festival

Instructions:
------------
This is a Raspberry Pi.

![Alt Raspberry Pi](/Users/karim/LightPi/img/Raspberry Pi.jpg?raw=true "Raspberry Pi")



This is the PiFace, an additional piece of hardware that can be attached to the Raspberry Pi.

![Alt Raspberry Pi](/Users/karim/LightPi/img/PiFace.jpg?raw=true "PiFace")

Attach the PiFace onto the Raspberry pi using the 26 pin adapter.

![Alt Raspberry Pi](/Users/karim/LightPi/img/R+PF.jpg?raw=true "R+PF")

Connect the monitor via HDMI output, speakers into the audio output port, mouse and keyboard are connected to the USB ports, ethernet can be used by connecting the ethernet cable into the ethernet port or a wireless usb receiver can be inserted into one of the USB ports. Finally insert the SD card and plug the Raspberry Pi into the power outlet.

![Alt Raspberry Pi](/Users/karim/LightPi/img/Cables.jpg?raw=true "Cables")

Connect the warning tower light to the relay outputs in the following order: RED, BLACK, GREEN. With the BLACK wire coming from the power supply. 

With the Siren, the power supply will be directly connected into it due to the fact that it requires a lot of power. The wires stemming from the Siren are then connected to the second relay on the PiFace in the first two outlets.

![Alt Raspberry Pi](/Users/karim/LightPi/img/Wires.jpg?raw=true "Wires")
