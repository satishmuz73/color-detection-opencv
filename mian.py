import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        # Draw rectangle directly on the original frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Convert BGR image to RGB format for display
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('frame', frame)
    # cv2.imshow('Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
