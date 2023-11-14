import cv2

# Load an image from file
image_path = 'i'
image = cv2.imread(image_path)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  
