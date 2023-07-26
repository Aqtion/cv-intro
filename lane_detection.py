import cv2
import numpy as np
import matplotlib.pyplot as plt








def get_slopes_intercepts(lines):
    slopes = []
    intercepts = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2 - y1) / (x2 - x1)
        slopes.append(slope)
        y_intercept = y2 - x2 * slope
        x_intercept = -y_intercept / slope
        intercepts.append(x_intercept)
    return (slopes, intercepts)


def detect_lanes(lines):
    slopes_and_intercepts = get_slopes_intercepts(lines)
    slopes = slopes_and_intercepts[0]
    intercepts = slopes_and_intercepts[1]
