#!/usr/bin/env python3
"""Estimate optical perceived-age bias from camera distance, focal length, and lighting."""
import json, sys

def estimate_age_bias(focal_mm: float = 26.0, distance_cm: float = 40.0, lighting: str = "overhead_cool") -> dict:
    lens_bias = round(max(0.0, (50.0 - focal_mm) * 0.06) + max(0.0, (55.0 - distance_cm) * 0.05), 1)
    light_map = {"window_soft": -1.5, "golden_hour": -2.0, "ring_front": -0.8, "overhead_cool": 3.8, "harsh_noon": 4.5}
    light_bias = light_map.get(lighting, 0.0)
    net_years = round(lens_bias + light_bias, 1)
    return {
        "focal_length_mm": focal_mm,
        "camera_distance_cm": distance_cm,
        "lighting_condition": lighting,
        "estimated_perceived_age_shift_years": net_years,
        "recommendation": "Step back to >=75cm (2x portrait lens) facing soft 45-degree window light to eliminate +3 to +5yr under-eye shadow bias."
    }

if __name__ == "__main__":
    f = float(sys.argv[1]) if len(sys.argv) > 1 else 26.0
    d = float(sys.argv[2]) if len(sys.argv) > 2 else 38.0
    l = sys.argv[3] if len(sys.argv) > 3 else "overhead_cool"
    print(json.dumps(estimate_age_bias(f, d, l), indent=2))
