import cv2

# Load the image
image = cv2.imread("C:\Users\aurvi\Desktop\ct.jpg")

# Define block size for binning
block_size = 4

# Apply pixel binning
binned_image = cv2.resize(image, (image.shape[1] // block_size, image.shape[0] // block_size))

# Display the original and binned images
cv2.imshow('Original Image', image)
cv2.imshow('Binned Image', binned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
