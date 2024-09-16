# Face Recognition Smart Attendance System 

This project is a **Face Recognition Attendance System** that uses Python, OpenCV, and the `face_recognition` library to recognize faces in real-time using a webcam. It marks attendance for recognized individuals by saving their names, along with the time and date, in a CSV file. The project features a **Tkinter-based graphical user interface (GUI)** for better user experience, allowing users to start and stop the webcam, and monitor the recognition process.

## Features
- **Real-Time Face Recognition**: Detects and recognizes faces using a webcam.
- **Attendance Marking**: Automatically logs attendance when a recognized face is detected.
- **Tkinter GUI**: Provides a clean and simple graphical interface with buttons to control the webcam and display recognition results.
- **CSV Attendance Log**: Saves the attendance data (name, time, date) to a CSV file for easy record-keeping.

## Screenshots
![Screenshot](https://your-image-link.png)

## Requirements

Make sure you have Python 3.x installed along with the following libraries:

- OpenCV (`opencv-python`)
- Face Recognition (`face_recognition`)
- Pillow (`Pillow`)
- Tkinter (usually pre-installed with Python)

You can install the required libraries using pip:
```bash
pip install opencv-python face_recognition Pillow
```

## Project Structure

```plaintext
face-recognition-attendance/
│
├── known_faces/         # Directory containing known face images
├── Attendance.csv       # Attendance log file (created when the app runs)
├── main.py              # Main Python script for the application
├── README.md            # Project documentation (this file)
```

## How It Works

1. **Face Encoding**:
   - Images of known individuals are placed in the `known_faces` directory. Each file's name should match the person's name (e.g., `john_doe.jpg` for John Doe).
   - The program encodes these known faces during the initialization process.

2. **Real-Time Recognition**:
   - The webcam feed is captured and processed in real-time. Faces in each frame are compared with the encoded known faces.
   
3. **Marking Attendance**:
   - When a recognized face is detected, the individual's name is logged into the `Attendance.csv` file along with the current time and date.

4. **Tkinter GUI**:
   - A graphical interface built using Tkinter allows users to easily start and stop the webcam. The feed is displayed in the window, and recognized faces are shown with bounding boxes.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2. Add Known Faces

- Add images of individuals whose attendance you want to track in the `known_faces` folder.
- Make sure the filenames are meaningful as the system uses these names to log attendance (e.g., `john_doe.jpg`).

### 3. Run the Application

- Run the main Python script to start the Tkinter GUI and begin recognizing faces:
   ```bash
   python main.py
   ```

### 4. GUI Operation

- **Start Webcam**: Click the "Start Webcam" button to start the face recognition process. The webcam feed will appear, and recognized faces will be marked with a green bounding box.
- **Stop Webcam**: Click the "Stop Webcam" button to stop the webcam feed.

Attendance will be recorded in the `Attendance.csv` file.

## Example Attendance Log

```csv
Name, Time, Date
john_doe, 10:30:45 AM, 16-September-2024
jane_doe, 10:31:15 AM, 16-September-2024
```

## Code Overview

### 1. **Main Components**
- **Tkinter GUI**: Provides buttons to control the webcam and displays real-time video feed.
- **Face Recognition**: Utilizes the `face_recognition` library to encode known faces and recognize them in the webcam feed.
- **Attendance Marking**: Logs recognized faces with the time and date into a CSV file.

### 2. **Key Functions**

- `findEncodings(images)`: Encodes all known face images stored in the `known_faces` directory.
- `markAttendance(name)`: Logs the recognized person's name, time, and date in the `Attendance.csv` file.
- `update_frame()`: Captures webcam frames, performs face recognition, and updates the GUI with the processed frame.

### 3. **Application Flow**
- The user starts the webcam by clicking the **Start Webcam** button.
- The system captures video from the webcam, processes the frames, and checks if any faces match the known faces.
- Recognized faces are displayed in the GUI and attendance is logged in `Attendance.csv`.
- The user can stop the webcam by clicking the **Stop Webcam** button.

## Known Issues and Limitations
- **Face Encoding Errors**: Ensure that the images in the `known_faces` folder are clear and contain one face for optimal encoding.
- **Performance**: As the number of known faces increases, performance may slow down due to the comparison of multiple face encodings.

## Future Enhancements
- Add functionality to dynamically add new faces through the GUI.
- Display and manage attendance logs directly from the GUI.
- Improve scalability and performance for larger numbers of known faces.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository, submit issues, or open pull requests for improvements and bug fixes.

---

This `README.md` gives a clear and structured overview of the project, its usage, setup, and features. You can modify it to fit any additional features or customizations that you might add in the future!
