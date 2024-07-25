import cv2
import numpy as np
from matplotlib import pyplot as plt

def canny_edge_detection(frame):
    # Convert the frame to grayscale for edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and smoothen edges
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0.5)
    
    # Perform Canny edge detection
    edges = cv2.Canny(image=blurred, threshold1=70, threshold2=135)
    
    return blurred, edges

# Test the function with an example image
if __name__ == "__main__":
    # Read the image
    #image_path = r"C:\Users\Ayush\Desktop\download (1).jpg"
    image_path = r"C:\Users\Ayush\Desktop\potato-blight.jpg"
    # Replace with your image path
    frame = cv2.imread(image_path)
    
    if frame is None:
        print(f"Error: The image at {image_path} could not be read.")
    else:
        # Perform edge detection
        blurred, edges = canny_edge_detection(frame)
        
        # Use matplotlib to display images
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 3, 1)
        plt.title('Original Image')
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.subplot(1, 3, 2)
        plt.title('Blurred Image')
        plt.imshow(blurred, cmap='gray')
        plt.axis('off')
        
        plt.subplot(1, 3, 3)
        plt.title('Edges')
        plt.imshow(edges, cmap='gray')
        plt.axis('off')
        
        plt.show()
