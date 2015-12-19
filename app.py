from camera_pi import Camera
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/get_fps')
def get_fps():
	return Response(genfps(Camera()), mimetype='text\plain');

def genfps(camera):
    while True:
        fps = camera.get_fps()
        yield (b'--frame\r\n'
               b'Content-Type: text/plain\r\n\r\n' + fps + b'\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)