import cv2
import os

def convert(image_path):
    # Step 1: Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image. Check the file path.")
        return None

    # Step 2: Convert the image to grayscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply a bilateral filter to reduce noise while keeping edges sharp
    filtered_image = cv2.bilateralFilter(grey_image, d=9, sigmaColor=75, sigmaSpace=75)

    # Step 4: Detect edges using Canny edge detection
    canny_edges = cv2.Canny(filtered_image, threshold1=50, threshold2=150)  # Adjusted threshold

    # Step 5: Invert the grayscale image for sketch effect
    invert = cv2.bitwise_not(grey_image)

    # Step 6: Apply Gaussian blur to smooth the inverted image
    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    # Step 7: Invert the blurred image again
    inverted_blur = cv2.bitwise_not(blur)

    # Step 8: Create a basic pencil sketch by dividing the grayscale by the blurred inverted image
    sketch = cv2.divide(grey_image, inverted_blur, scale=256.0)

    # Step 9: Blend the sketch with the Canny edge detection result for strong lines
    final_sketch = cv2.addWeighted(sketch, 0.7, canny_edges, 0.3, 0)  # Blend with Canny edges

    # Step 10: Optionally, increase brightness or contrast for better visibility
    final_sketch = cv2.add(final_sketch, 30)

    # Step 11: Save the result in the processed folder
    output_filename = "Refined_Sketch.png"
    output_path = os.path.join("processed", output_filename)  # Save in processed folder
    cv2.imwrite(output_path, final_sketch)

    print(f"Sketch saved at: {output_path}")  # Debug print
    return output_path  # Return the path of the saved sketch
