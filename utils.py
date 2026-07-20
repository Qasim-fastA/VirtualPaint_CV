"""
Shared helper functions and constants used across multiple modules.

Responsibilities:
- Small reusable utilities (e.g., distance calculations, coordinate
  normalization-to-pixel conversion, smoothing helpers).
- Centralized constants (colors, thresholds, default thickness values)
  to avoid magic numbers scattered across the codebase.

Should NOT contain: module-specific logic (e.g., no gesture rules here,
no canvas state here). If a function only makes sense in one module's
context, it belongs in that module, not here.
"""