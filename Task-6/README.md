# Face Profiler AI

A Flask-based web application that analyzes facial features using OpenCV and MediaPipe to generate a personality profile based on physiognomy heuristics.

## 🌟 Features

- **Face Landmark Detection**: Uses MediaPipe's Face Mesh to precisely locate eyes, nose, mouth, and jawline (mapped to 68 landmarks).
- **Feature Measurement**: Calculates facial ratios (face width/height, eye spacing, nose width, lip fullness).
- **Personality Profiling**: Maps physical measurements to personality traits and MBTI types (for entertainment purposes).
- **Video Analysis**: Detects and counts moving objects in uploaded videos.
- **Premium UI**: Modern, dark-themed interface built with Flask and CSS.

## 🛠️ Setup & Installation

1. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application**:

    ```bash
    python app.py
    ```

3. **Open in Browser**:
    Go to `http://127.0.0.1:5000`

## 📊 How it Works

1. **Upload**: User uploads a front-facing portrait or a video.
2. **Detect**: MediaPipe detects the face and key landmarks (for images) or OpenCV detects motion (for videos).
3. **Measure**: The app calculates geometric ratios (e.g., face width vs height).
4. **Analyze**: Heuristic rules map these ratios to traits (e.g., "Wide face" -> "Assertive").
5. **Result**: Displays the original image with landmarks drawn and the generated profile, or the motion count for videos.

## 📝 Disclaimer

The personality profiling in this application is based on physiognomy (face reading) heuristics and is for **entertainment purposes only**. It is not scientifically proven.
