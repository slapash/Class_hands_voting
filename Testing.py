import cv2
import pytest
from VotingSystem import VotingSystem
from CameraInterface import CameraInterface
from VoteProcessor import VoteProcessor

def test_camera_capture():
    camera = CameraInterface()
    frame = camera.capture_frame()
    assert frame is not None
    camera.release()

def test_vote_detection():
    processor = VoteProcessor()
    frame = cv2.imread('test_vote.jpg')
    votes = processor.tally_votes(frame)
    assert votes == {1: 5, 2: 10}

def test_voting_system():
    system = VotingSystem()
    system.start_voting()
    votes = system.get_live_feedback()
    assert votes != {}
    system.stop_voting()
    