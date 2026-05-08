
import cv2
import matplotlib.pyplot as plt

# Load the image using the correct path
image = cv2.imread('/content/moon_00001.jpg')

# Check if image loaded successfully
if image is None:
    print("Error: Image not found.")
else:

    # Function to process image
    def process_image(image):

        # Resize image to 144x96
        resized = cv2.resize(image, (144, 96))

        # Convert image to grayscale
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        return gray

    # Process image
    gray_image = process_image(image)

    # Apply binary threshold
    threshold_value = 120

    _, threshold_image = cv2.threshold(
        gray_image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # Save processed image
    cv2.imwrite('/content/processed_moon.jpg', threshold_image)

    # Display images
    plt.figure(figsize=(10,5))

    # Original image
    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    # Processed image
    plt.subplot(1,2,2)
    plt.title("Processed Image")
    plt.imshow(threshold_image, cmap='gray')
    plt.axis('off')

    plt.show()

    print("Processing completed successfully!")
