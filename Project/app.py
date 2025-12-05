import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)

# Use absolute paths based on the application file location
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
app.config['STATIC_FOLDER'] = os.path.join(BASE_DIR, 'static')

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['STATIC_FOLDER'], exist_ok=True)

# Load YOLO model
model = YOLO('yolov8n.pt')

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    # Video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Output writer
    # Try 'avc1' for better browser compatibility, fallback to 'mp4v'
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not out.isOpened():
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Background Subtractor
    backSub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Background Subtraction
        fgMask = backSub.apply(frame)
        
        # Cleanup mask (remove noise/shadows)
        _, fgMask = cv2.threshold(fgMask, 250, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)
        fgMask = cv2.dilate(fgMask, kernel, iterations=2)

        # 2. Find Contours (Moving Objects)
        contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 3. YOLO Detection
        results = model(frame, verbose=False)
        yolo_boxes = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = float(box.conf[0].cpu().numpy())
                cls = int(box.cls[0].cpu().numpy())
                name = model.names[cls]
                yolo_boxes.append({
                    'bbox': (x1, y1, x2, y2),
                    'conf': conf,
                    'name': name
                })

        # 4. Match Motion to YOLO
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 500: # Filter small movements
                continue

            x, y, w, h = cv2.boundingRect(cnt)
            mx1, my1, mx2, my2 = x, y, x+w, y+h
            
            # Find best matching YOLO box
            best_match = None
            max_iou = 0.0

            for yb in yolo_boxes:
                yx1, yy1, yx2, yy2 = yb['bbox']
                
                # Calculate Intersection
                ix1 = max(mx1, yx1)
                iy1 = max(my1, yy1)
                ix2 = min(mx2, yx2)
                iy2 = min(my2, yy2)
                
                iw = max(0, ix2 - ix1)
                ih = max(0, iy2 - iy1)
                intersection = iw * ih
                
                # Calculate Union
                motion_area = w * h
                yolo_area = (yx2 - yx1) * (yy2 - yy1)
                union = motion_area + yolo_area - intersection
                
                if union > 0:
                    iou = intersection / union
                    if iou > 0.1: 
                        if iou > max_iou:
                            max_iou = iou
                            best_match = yb

            # Draw
            color = (255, 255, 255) # White
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            label = ""
            if best_match:
                label = f"{best_match['name']} ({best_match['conf']:.2f})"
            else:
                label = "Unknown"

            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    return {
        'width': width,
        'height': height,
        'fps': fps,
        'total_frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) if cap.get(cv2.CAP_PROP_FRAME_COUNT) > 0 else 0
    }

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/process', methods=['POST'])
def process():
    if 'video' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['video']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        output_filename = 'output.mp4'
        output_path = os.path.join(app.config['STATIC_FOLDER'], output_filename)
        
        # Process
        stats = process_video(filepath, output_path)
        
        return render_template('result.html', video_file=output_filename, stats=stats)

    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_video(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
