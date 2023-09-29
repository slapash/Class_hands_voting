
from CameraInterface import CameraInterface
from VoteProcessor import VoteProcessor

class VotingSystem:
    def __init__(self):
        self.camera = CameraInterface()
        self.processor = VoteProcessor()
        self.votes = {}

    def start_voting(self):
        frame = self.camera.capture_frame()
        current_votes = self.processor.tally_votes(frame)
        for key, value in current_votes.items():
            self.votes[key] = self.votes.get(key, 0) + value

    def stop_voting(self):
        self.camera.release()

    def get_live_feedback(self):
        return self.votes
    