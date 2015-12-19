# rpi-security-stream
Python + Flask video streaming service



1. Get your Rpi local IP by `ifconfig` command. Save that somewhere, you'll need that later.
2. On your RPI pull this repo. Run with `sudo python app.py`. Server will start on :80 port.
3. On your workstation, in your browser open IP that you fetched earlier.
4. Stream should start after 1-2 seconds.

@todo:
- motion detection with openCV
- framerate controller
- mail module
- fix get_fps
- create daemon that will start with RPI boot

Requires camera connected to Rpi + pi_camera module installed.
