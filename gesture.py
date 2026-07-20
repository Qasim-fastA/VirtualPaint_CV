"""
Interprets raw hand landmarks into meaningful application gestures/modes.

Responsibilities:
- Determine which fingers are extended/folded from landmark positions.
- Classify the current finger-state pattern into an application mode
  (e.g., DRAW, SELECT, ERASE, IDLE).

Should NOT contain: MediaPipe initialization, canvas manipulation, or
rendering. This module only transforms landmarks -> meaning.
"""