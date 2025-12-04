from flask import Flask, render_template, request, redirect, url_for, flash
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from face_analyzer import FaceProfiler

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def allowed_video_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'mov', 'mkv'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('analyze', filename=filename))
    
    return render_template('index.html')

@app.route('/analyze/<filename>')
def analyze(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        profiler = FaceProfiler()
        
        # Read image
        image = cv2.imread(filepath)
        if image is None:
            flash("Error loading image")
            return redirect(url_for('index'))
            
        # Get landmarks
        landmarks, face_rect = profiler.get_landmarks(image)
        
        if landmarks is None:
            flash("No face detected in the image! Please try another photo.")
            return redirect(url_for('index'))
            
        # Calculate metrics and profile
        metrics = profiler.calculate_metrics(landmarks)
        profile = profiler.analyze_personality(metrics)
        
        # Draw analysis on image
        result_img = profiler.draw_analysis(image, landmarks)
        result_filename = 'result_' + filename
        result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
        cv2.imwrite(result_path, result_img)
        
        return render_template('result.html', 
                             original=filename, 
                             result=result_filename, 
                             profile=profile)
                             
    except FileNotFoundError as e:
        flash(str(e))
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('index'))

import threading

# Helper function to count moving objects in a video using background subtraction
def process_video(video_path):
    """Return the total count of moving objects detected in the video.
    Simple approach: use MOG2 background subtractor, find contours on each frame,
    and count distinct moving blobs per frame. The sum across frames is returned.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Unable to open video file: {video_path}")
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)
    total_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        fgmask = fgbg.apply(frame)
        # Remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        # Find contours of moving objects
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Count contours with a reasonable area to filter out specks
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:  # heuristic threshold
                total_count += 1
    cap.release()
    return total_count

@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('No video part')
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('No selected video')
            return redirect(request.url)
        if file and allowed_video_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            try:
                count = process_video(filepath)
            except Exception as e:
                flash(f"Error processing video: {str(e)}")
                return redirect(url_for('index'))
            return render_template('result_video.html', video=filename, count=count)
    # GET request – show a simple upload page or redirect to index
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
