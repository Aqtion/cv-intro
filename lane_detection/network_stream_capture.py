import argparse

import cv2
from lane_detection import *
from lane_following import *


def main(ip_address):
    vcap = cv2.VideoCapture(f"rtsp://192.168.1.102:8554/rovcam")
    try:
        while True:
            ret, frame = vcap.read()
            if ret:
                print(" YOU GOT THIS ")
                print(frame.shape)
                lines = detect_lines(frame, 50, 90, 3, 150, 10)
                try:
                    lanes = detect_lanes(lines)
                    # print ("tried to detect lanes")
                    closest_lane = get_center_lane(lanes)
                    frame = draw_lane(frame, closest_lane, (255, 0, 0))
                    frame = draw_lines(frame, lines, (0, 255, 0))
                    avg_x_intercept, avg_slope = get_lane_center(closest_lane)
                    x = closest_lane[0][2]
                    y = closest_lane[0][3]
                    cv2.line(
                        frame,
                        (int(avg_x_intercept), 1080),
                        (int(x), int(y)),
                        (0, 0, 255),
                        3,
                    )
                    print(recommend_direction(avg_x_intercept, avg_slope))
                    plt.imshow(frame)
                except:
                    pass

            else:
                pass

    except KeyboardInterrupt:
        # Close the connection
        vcap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Stream Capture")
    parser.add_argument("--ip", type=str, help="IP Address of the Network Stream")
    args = parser.parse_args()

    main(args.ip)
