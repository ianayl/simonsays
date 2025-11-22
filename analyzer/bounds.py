import cv2

if len(sys.argv) < 2:
    print("provide image first")
    exit(1)

# Load the image
image = cv2.imread(sys.argv[1])

# 1. Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 2. Detect edges
edges = cv2.Canny(blurred, 50, 150)

# 3. Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Filter contours for rectangles
rectangles = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 4 and cv2.isContourConvex(approx):
        # Calculate aspect ratio
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        # Define aspect ratio threshold for rectangles (adjust as needed)
        if 1.2 < aspect_ratio < 2.5:  
            rectangles.append(approx)

# 5. Extract rectangle coordinates
for rectangle in rectangles:
    x, y, w, h = cv2.boundingRect(rectangle)
    print(f"Rectangle coordinates: Top-left:({x}, {y}), Bottom-right:({x+w}, {y+h})")

# 6. (Optional) Draw rectangles on the original image
for rectangle in rectangles:
    x, y, w, h = cv2.boundingRect(rectangle)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Detected Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
