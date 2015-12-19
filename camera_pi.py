import time
import io
import threading
import picamera


class Camera(object):
    thread = None
    frame = None 
    start = 0
    end = 0
    last_delta = 0

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        self.initialize()
        return self.frame

    def get_fps(self):
        self.initialize()
        return self.last_delta

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.hflip = True
            camera.vflip = True

            camera.start_preview()
            time.sleep(1)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                start = time.clock()
                # store frame
                stream.seek(0)
                cls.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
                last_delta = time.clock() - start

        cls.thread = None
