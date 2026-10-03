import numpy as np
import pandas as pd

WEIGHTS = {
    "equal": np.array([1/3, 1/3, 1/3]),
    "entropy": np.array([0.722, 0.123, 0.155]),
    "critic": np.array([0.362, 0.312, 0.326]),
    "pca": np.array([0.355, 0.341, 0.304]),
}

def compute_clri(cei, api, bwi, method="critic"):
    """Compute normalized CLRI from CEI, API and BWI."""
    if method not in WEIGHTS:
        raise ValueError(f"Unknown method: {method}")
    w = WEIGHTS[method]
    return w[0] * np.asarray(cei) + w[1] * np.asarray(api) + w[2] * np.asarray(bwi)

def compute_clri_dataframe(df, method="critic"):
    """Add a CLRI column to a dataframe containing CEI, API and BWI."""
    out = df.copy()
    out[f"CLRI_{method.upper()}"] = compute_clri(
        out["CEI"], out["API"], out["BWI"], method
    )
    return out
