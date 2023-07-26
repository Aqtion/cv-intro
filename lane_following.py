def get_lane_center(lanes):
    center_lane = ""
    min_dist = 1e9
    center_x = 2000
    avg_slope = -1
    for lane in lanes:
        line1 = lane[0]
        line2 = lane[1]
        x_int_1 = line1[0][1]
        x_int_2 = line2[0][1]
        avg_x_int = (x_int_1 + x_int_2) / 2
        distance_to_center = abs(avg_x_int - center_x)
        if (distance_to_center) < min_dist:
            center_lane = lane
            min_dist = distance_to_center
            slope_1 = line1[0][0]
            slope_2 = line1[1][0]
            avg_slope = (slope_1 + slope_2) / 2
    return [center_lane, avg_slope]


def recommend_direction(center, slope):
    center_x = 2000
    line1 = center[0]
    line2 = center[1]
    x_int_1 = line1[0][1]
    x_int_2 = line2[0][1]
    avg_x_int = (x_int_1 + x_int_2) / 2

    tol_lr = 250
    if abs(avg_x_int - center_x) < tol_lr:
        return "forward"
    else:
        if slope > 0:
            return "left"
        if slope < 0:
            return "right"
