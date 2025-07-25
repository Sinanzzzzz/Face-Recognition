import os
import cv2
import numpy as np
from PIL import Image


def train_recognizer():
    # Ensure recognizer directory exists
    if not os.path.exists('recognizer'):
        os.makedirs('recognizer')

    # Create face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Path to dataset
    path = "dataset"

    def get_images_with_ids(path):
        # List all image paths in the dataset
        image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

        faces = []
        ids = []

        for single_image_path in image_paths:
            # Open image and convert to grayscale
            faceImg = Image.open(single_image_path).convert('L')

            # Convert image to numpy array
            faceNp = np.array(faceImg, 'uint8')

            # Extract ID from filename
            id = int(os.path.split(single_image_path)[-1].split('.')[1])

            faces.append(faceNp)
            ids.append(id)

            # Optional: Display training images
            cv2.imshow("Training", faceNp)
            cv2.waitKey(10)

        return np.array(ids), faces

    # Get training data
    print("Preparing faces for training...")
    ids, faces = get_images_with_ids(path)

    # Train recognizer
    print("Training face recognizer...")
    recognizer.train(faces, ids)

    # Save the trained model
    recognizer.save("recognizer/trainingdata.yml")
    print("Training complete. Model saved.")

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    train_recognizer()
