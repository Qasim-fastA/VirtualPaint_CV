"""
hand_tracking.py
-----------------
A thin, reusable wrapper around MediaPipe Hands.

This adapts the classic "HandTrackingModule" pattern into a cleaner,
type-hinted class so the rest of the application never has to touch
MediaPipe's API directly.
"""

from typing import List, Tuple

import cv2
import mediapipe as mp

import config


class HandDetector:
    """
    Detects a hand in a video frame and exposes its landmark positions.

    Usage:
        detector = HandDetector()
        frame = detector.find_hands(frame)
        landmarks = detector.find_landmark_positions(frame)
    """

    def __init__(
        self,
        max_num_hands: int = config.MAX_NUM_HANDS,
        detection_confidence: float = config.DETECTION_CONFIDENCE,
        tracking_confidence: float = config.TRACKING_CONFIDENCE,
    ) -> None:
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )
        self._mp_draw = mp.solutions.drawing_utils
        self._results = None

    def find_hands(self, frame, draw_landmarks: bool = True):
        """
        Run hand detection on a BGR frame.

        Args:
            frame: BGR image (as returned by cv2.VideoCapture.read()).
            draw_landmarks: If True, draws MediaPipe's default landmark
                skeleton on top of the frame for debugging purposes.

        Returns:
            The (possibly annotated) frame.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self._results = self._hands.process(rgb_frame)

        if draw_landmarks and self._results.multi_hand_landmarks:
            for hand_landmarks in self._results.multi_hand_landmarks:
                self._mp_draw.draw_landmarks(
                    frame, hand_landmarks, self._mp_hands.HAND_CONNECTIONS
                )

        return frame

    def find_landmark_positions(self, frame, hand_index: int = 0) -> List[Tuple[int, int, int]]:
        """
        Return pixel-space landmark positions for a detected hand.

        Args:
            frame: The frame used only to resolve pixel coordinates
                (landmarks from MediaPipe are normalized 0-1).
            hand_index: Which detected hand to read (0 = first hand).

        Returns:
            A list of (landmark_id, x, y) tuples. Empty list if no hand
            was detected.
        """
        landmark_positions: List[Tuple[int, int, int]] = []

        if not self._results or not self._results.multi_hand_landmarks:
            return landmark_positions

        if hand_index >= len(self._results.multi_hand_landmarks):
            return landmark_positions

        frame_height, frame_width = frame.shape[:2]
        hand_landmarks = self._results.multi_hand_landmarks[hand_index]

        for landmark_id, landmark in enumerate(hand_landmarks.landmark):
            pixel_x = int(landmark.x * frame_width)
            pixel_y = int(landmark.y * frame_height)
            landmark_positions.append((landmark_id, pixel_x, pixel_y))

        return landmark_positions

    def has_hand(self) -> bool:
        """Whether a hand was found in the most recent `find_hands` call."""
        return bool(self._results and self._results.multi_hand_landmarks)

    def close(self) -> None:
        """Release MediaPipe resources."""
        self._hands.close()
