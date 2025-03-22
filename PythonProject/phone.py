import cv2
import numpy as np

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Approximate the contour
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

        # If the approximated contour has 4 points, it could be a rectangle
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)

            # Filter by aspect ratio to detect phone-like shapes
            aspect_ratio = float(w) / h
            if 0.5 < aspect_ratio < 1.5:  # Roughly square/rectangular
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
                cv2.putText(frame, 'Mobile Phone', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Show the output
    cv2.imshow('Mobile Phone Detector', frame)

    # Break on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
