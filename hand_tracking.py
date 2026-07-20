"""
Wraps MediaPipe Hands for hand detection and landmark extraction.

Responsibilities:
- Initialize and configure the MediaPipe Hands model.
- Given a frame, return detected hand landmarks (converted to usable pixel
  coordinates) and handedness (left/right), if any hand is present.

Should NOT contain: gesture interpretation, drawing logic, or UI code.
This module only answers "where is the hand and what are its landmarks?" —
it has no concept of "drawing" or "modes."
"""

