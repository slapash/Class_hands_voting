
import cv2
import mediapipe as mp


class VoteProcessor:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

    def detect_hands(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results.multi_hand_landmarks

    def count_fingers(self, hand):
        finger_tips = [4, 8, 12, 16, 20]
        raised_fingers = sum([1 for tip in finger_tips if hand.landmark[tip].y < hand.landmark[tip - 2].y])
        return raised_fingers

    def tally_votes(self, frame):
        hand_landmarks = self.detect_hands(frame)
        if not hand_landmarks:
            return {}

        votes = {}
        for hand in hand_landmarks:
            fingers = self.count_fingers(hand)
            votes[fingers] = votes.get(fingers, 0) + 1

        return votes

    def detect_hands(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        # If hands are detected, annotate them
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                self._annotate_hand(frame, landmarks)

        return results.multi_hand_landmarks

    def _annotate_hand(self, frame, landmarks):
        # Draw hand landmarks
        mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp.solutions.hands.HAND_CONNECTIONS)


    def __del__(self):
        self.mp_hands.Hands().close()
    