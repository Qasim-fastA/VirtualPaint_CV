"""
Entry point for the Virtual Paint application.

Responsibilities:
- Initialize webcam capture.
- Run the main loop: read frame -> flip -> detect hands -> interpret gesture ->
  update canvas -> blend canvas with frame -> display.
- Handle exit conditions and resource cleanup (release camera, destroy windows).

Should NOT contain: hand detection logic, drawing math, or UI rendering details.
This file orchestrates other modules; it does not implement them.
"""