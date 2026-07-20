"""
Owns the persistent drawing canvas and core drawing/erasing logic.

Responsibilities:
- Create and hold the canvas (persists across frames, independent of webcam feed).
- Apply strokes to the canvas given points, color, and thickness.
- Handle erasing as a parameterized variant of drawing.
- Maintain state needed for continuous strokes (e.g., previous point).

Should NOT contain: hand detection, gesture classification, or UI rendering.
This module only knows about pixels on the canvas, not where those points came from.
"""