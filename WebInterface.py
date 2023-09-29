from flask import Flask, render_template, jsonify, Response
from VotingSystem import VotingSystem
from CameraInterface import CameraInterface
from VoteProcessor import VoteProcessor
import cv2

app = Flask(__name__)
voting_system = VotingSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_voting', methods=['POST'])
def start_voting():
    voting_system.start_voting()
    return jsonify(status='started')

@app.route('/stop_voting', methods=['POST'])
def stop_voting():
    voting_system.stop_voting()
    return jsonify(status='stopped')

@app.route('/results')
def get_results():
    votes = voting_system.get_live_feedback()
    return jsonify(votes)

@app.route('/video_feed')
def video_feed():
    camera = CameraInterface()
    processor = VoteProcessor()
    
    def generate():
        while True:
            frame = camera.capture_frame()
            processor.tally_votes(frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
    