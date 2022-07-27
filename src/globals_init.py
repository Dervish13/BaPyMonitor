import cv2


def initialize_globals():
    global video
    video = cv2.VideoCapture(0)
