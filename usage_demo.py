# usage_demo.py

from distrand import distrand
import numpy as np

print("Integer Mode Example:")
try:
    ints = distrand(low=0, high=100, size=5, min_dist=10, dtype=int)
    print("Generated integers:", ints)
except ValueError as e:
    print("Error:", e)

print("\nFloat Mode Example:")
try:
    floats = distrand(low=0.0, high=5.0, size=4, min_dist=1.2, dtype=float)
    print("Generated floats:", np.round(floats, 2))
except ValueError as e:
    print("Error:", e)

print("\nInvalid Parameters Example:")
try:
    distrand(low=0, high=10, size=10, min_dist=5, dtype=int)
except ValueError as e:
    print("Caught expected error:", e)
