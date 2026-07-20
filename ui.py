"""
Renders visual UI elements on the display frame (not the canvas).

Responsibilities:
- Draw the color palette, mode indicators, current tool/color display, and
  FPS counter onto the live display frame.
- Provide hit-testing helpers for UI regions (e.g., is a point inside a
  palette button?).

Should NOT contain: hand detection or drawing-onto-canvas logic. This module
only affects what the user sees overlaid on screen, never the saved artwork.
"""