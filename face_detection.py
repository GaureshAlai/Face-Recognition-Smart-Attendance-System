import cv2
import matplotlib.pyplot as plt

# Load the image
imagePath = 'D:\MIT WPU\Face Recognition Project\known_faces\modi.jpg'
img = cv2.imread(imagePath)

# Check if the image was successfully loaded
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the Haar cascade for face detection
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detect faces in the grayscale image
    faces = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    # Check if faces were detected
    if len(faces) == 0:
        print("No faces detected.")
    else:
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Convert the image to RGB (from BGR) for displaying with Matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Display the result
        plt.figure(figsize=(20, 10))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.show()
