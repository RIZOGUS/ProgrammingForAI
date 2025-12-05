# AI Video Motion & Object Detector

A powerful Flask-based web application that combines **Motion Detection** (Background Subtraction) with **YOLOv8 Object Detection** to analyze videos. It highlights moving objects and identifies them using state-of-the-art AI.

## 🚀 Features

-   **Motion Detection**: Uses OpenCV's MOG2 Background Subtractor to detect any movement in the video.
-   **AI Object Recognition**: Integrates YOLOv8 to identify objects (e.g., Person, Car, Dog).
-   **Smart Visualization**:
    -   Draws a **WHITE** bounding box around moving objects.
    -   Labels known objects with their name and confidence score (e.g., "Car 0.95").
    -   Labels unrecognized moving objects as "Unknown".
-   **Interactive Web GUI**:
    -   Drag & Drop video upload.
    -   Real-time processing status.
    -   Video player to view results immediately.
    -   Download option for the processed video.
    -   Detailed video statistics (Resolution, FPS, Total Frames).

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **Computer Vision**: OpenCV (cv2)
-   **AI Model**: Ultralytics YOLOv8 (`yolov8n.pt`)
-   **Frontend**: HTML5, CSS3 (Inter font), JavaScript

## 📦 Installation

1.  **Clone or Navigate to the project directory**:
    ```bash
    cd d:\Tasks\PFAI\Project
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This will install Flask, OpenCV, Ultralytics, and NumPy. On the first run, it will also automatically download the YOLOv8 model weights.*

## ▶️ Usage

1.  **Run the Application**:
    ```bash
    python app.py
    ```

2.  **Open in Browser**:
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

3.  **Analyze a Video**:
    -   Upload an `.mp4` or `.avi` file.
    -   Wait for the processing to complete.
    -   View the result and download the annotated video.

## 📂 Project Structure

```
Project/
├── app.py              # Main Flask application & Logic
├── requirements.txt    # Python dependencies
├── yolov8n.pt          # YOLOv8 Model (downloaded automatically)
├── static/             # Static assets & processed videos
│   └── output.mp4      # The latest processed video
├── templates/          # HTML Templates
│   ├── upload.html     # Upload page
│   └── result.html     # Result & Dashboard page
└── uploads/            # Temporary storage for uploaded videos
```

## 📝 Notes

-   **Performance**: Processing speed depends on your CPU/GPU. YOLOv8 Nano (`yolov8n`) is used for a balance of speed and accuracy.
-   **Motion Threshold**: The system filters out very small movements to reduce noise.
