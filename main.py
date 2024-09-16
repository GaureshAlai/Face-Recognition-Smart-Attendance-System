import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import Label, Button, messagebox
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Global variables
video_source = 0  # Webcam index
cap = None        # Webcam capture object
images = []
classNames = []
encoded_face_train = []

# Setup the GUI layout
header = Label(root, text="Face Recognition Attendance System", font=("Arial", 24), bg="#003366", fg="white")
header.pack(fill=tk.X, pady=10)

# Frame to hold the video feed
video_frame = tk.Frame(root, width=720, height=480, bg="black")
video_frame.pack(pady=20)
lbl_img = Label(video_frame)
lbl_img.pack()

# Status label
status_label = Label(root, text="Click 'Start Webcam' to begin face recognition", font=("Arial", 14), bg="#f0f0f0", fg="green")
status_label.pack(pady=10)

# Function to load known faces
def load_known_faces():
    global images, classNames, encoded_face_train
    path = 'known_faces'
    images = []
    classNames = []
    mylist = os.listdir(path)
    for cl in mylist:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encoded_face_train = findEncodings(images)
    print("Encoding complete")

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            date = now.strftime('%d-%B-%Y')
            f.write(f'{name}, {time}, {date}\n')

# Function to update the video frame
def update_frame():
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
        
        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            
            if matches[matchIndex]:
                name = classNames[matchIndex].upper().lower()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        # Convert the image to a format Tkinter can use
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # Update the image on the label
        lbl_img.imgtk = img
        lbl_img.configure(image=img)

    lbl_img.after(10, update_frame)  # Update every 10 ms

# Function to start the webcam
def start_webcam():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(video_source)
        load_known_faces()
        status_label.config(text="Recognizing Faces...", fg="blue")
        update_frame()

# Function to stop the webcam
def stop_webcam():
    global cap
    if cap is not None and cap.isOpened():
        cap.release()
        status_label.config(text="Webcam Stopped", fg="red")
        lbl_img.config(image='')  # Clear the label

# Buttons to control the webcam
btn_start = Button(root, text="Start Webcam", font=("Arial", 16), bg="#003366", fg="white", width=15, command=start_webcam)
btn_start.pack(pady=10)

btn_stop = Button(root, text="Stop Webcam", font=("Arial", 16), bg="#660000", fg="white", width=15, command=stop_webcam)
btn_stop.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Release the video capture when done
if cap is not None:
    cap.release()
cv2.destroyAllWindows()
