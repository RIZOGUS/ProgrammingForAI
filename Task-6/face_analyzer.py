import cv2
import mediapipe as mp
import numpy as np

class FaceProfiler:
    def __init__(self, model_path=None):
        # MediaPipe doesn't need external model files
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
        
        # MediaPipe landmark indices that correspond to dlib 68 landmarks
        # This mapping converts MediaPipe's 468 landmarks to dlib-like 68 landmarks
        self.landmark_mapping = {
            # Jawline (0-16)
            0: 234, 1: 227, 2: 137, 3: 177, 4: 215, 5: 135, 6: 169, 7: 170, 8: 152,
            9: 399, 10: 396, 11: 364, 12: 435, 13: 401, 14: 366, 15: 447, 16: 454,
            # Eyebrows (17-26)
            17: 70, 18: 63, 19: 105, 20: 66, 21: 107,
            22: 336, 23: 296, 24: 334, 25: 293, 26: 300,
            # Nose (27-35)
            27: 168, 28: 6, 29: 197, 30: 195, 31: 5,
            32: 4, 33: 19, 34: 94, 35: 2,
            # Eyes (36-47)
            36: 33, 37: 160, 38: 158, 39: 133, 40: 153, 41: 144,
            42: 362, 43: 385, 44: 387, 45: 263, 46: 373, 47: 380,
            # Mouth (48-67)
            48: 61, 49: 39, 50: 37, 51: 0, 52: 267, 53: 269, 54: 291,
            55: 375, 56: 321, 57: 405, 58: 314, 59: 17, 60: 84, 61: 181,
            62: 91, 63: 146, 64: 78, 65: 191, 66: 80, 67: 81
        }

    def get_landmarks(self, image):
        # Convert BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_image)
        
        if not results.multi_face_landmarks:
            return None, None
        
        # Get the first face
        face_landmarks = results.multi_face_landmarks[0]
        
        # Convert MediaPipe landmarks to dlib-like 68 landmarks format
        h, w = image.shape[:2]
        coords = np.zeros((68, 2), dtype=int)
        
        for i in range(68):
            mp_idx = self.landmark_mapping[i]
            landmark = face_landmarks.landmark[mp_idx]
            coords[i] = (int(landmark.x * w), int(landmark.y * h))
        
        # Create a fake face rectangle for compatibility
        x_coords = coords[:, 0]
        y_coords = coords[:, 1]
        face_rect = {
            'left': int(np.min(x_coords)),
            'top': int(np.min(y_coords)),
            'right': int(np.max(x_coords)),
            'bottom': int(np.max(y_coords))
        }
        
        return coords, face_rect

    def calculate_metrics(self, landmarks):
        
        def dist(p1, p2):
            return np.linalg.norm(p1 - p2)

        # 1. Face Width (Jawline width)
        face_width = dist(landmarks[0], landmarks[16])
        
        # 2. Face Height (Chin to mid-eyebrow)
        mid_eyebrow = (landmarks[21] + landmarks[22]) / 2
        chin = landmarks[8]
        face_height = dist(mid_eyebrow, chin)
        
        # 3. Eye Size (Average width of eyes)
        left_eye_width = dist(landmarks[36], landmarks[39])
        right_eye_width = dist(landmarks[42], landmarks[45])
        avg_eye_width = (left_eye_width + right_eye_width) / 2
        
        # 4. Nose Width
        nose_width = dist(landmarks[31], landmarks[35])
        
        # 5. Lip Fullness (Height of mouth)
        mouth_height = dist(landmarks[51], landmarks[57])
        
        # Ratios (normalized by face width/height to be scale invariant)
        metrics = {
            "face_ratio": face_height / face_width, # > 1.3 oblong, < 1.3 round/square
            "eye_spacing_ratio": dist(landmarks[39], landmarks[42]) / face_width,
            "nose_width_ratio": nose_width / face_width,
            "lip_fullness_ratio": mouth_height / face_height,
            "jaw_width_ratio": dist(landmarks[4], landmarks[12]) / face_width # Lower jaw width
        }
        
        return metrics

    def analyze_personality(self, metrics):
        # This is a heuristic/fun mapping, not scientific!
        traits = []
        mbti_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
        # Face Shape Analysis
        if metrics["face_ratio"] > 1.35:
            traits.append("Analytical & Logical (High Face Ratio)")
            mbti_scores["T"] += 2
            mbti_scores["J"] += 1
        else:
            traits.append("Practical & Grounded (Low Face Ratio)")
            mbti_scores["S"] += 2
            mbti_scores["P"] += 1
            
        # Eye Spacing
        if metrics["eye_spacing_ratio"] > 0.25:
            traits.append("Broad Perspective & Tolerant (Wide Eyes)")
            mbti_scores["N"] += 2
            mbti_scores["P"] += 1
        else:
            traits.append("Focused & Detail-Oriented (Close Eyes)")
            mbti_scores["S"] += 2
            mbti_scores["J"] += 1
            
        # Nose Width
        if metrics["nose_width_ratio"] > 0.22:
            traits.append("Assertive & Confident (Prominent Nose)")
            mbti_scores["E"] += 2
            mbti_scores["T"] += 1
        else:
            traits.append("Diplomatic & Careful (Narrow Nose)")
            mbti_scores["I"] += 2
            mbti_scores["F"] += 1
            
        # Lip Fullness
        if metrics["lip_fullness_ratio"] > 0.15:
            traits.append("Expressive & Empathetic (Full Lips)")
            mbti_scores["F"] += 2
            mbti_scores["E"] += 1
        else:
            traits.append("Reserved & Stoic (Thin Lips)")
            mbti_scores["T"] += 2
            mbti_scores["I"] += 1
            
        # Determine MBTI
        mbti = ""
        mbti += "E" if mbti_scores["E"] >= mbti_scores["I"] else "I"
        mbti += "S" if mbti_scores["S"] >= mbti_scores["N"] else "N"
        mbti += "T" if mbti_scores["T"] >= mbti_scores["F"] else "F"
        mbti += "J" if mbti_scores["J"] >= mbti_scores["P"] else "P"
        
        return {
            "mbti": mbti,
            "traits": traits,
            "metrics": metrics
        }

    def draw_analysis(self, image, landmarks):
        img_copy = image.copy()
        # Draw jaw
        for i in range(0, 16):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        # Draw eyebrows
        for i in range(17, 21):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        for i in range(22, 26):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        # Draw nose
        for i in range(27, 30):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        for i in range(31, 35):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        # Draw eyes
        for i in range(36, 41):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        cv2.line(img_copy, tuple(landmarks[41]), tuple(landmarks[36]), (0, 255, 0), 2)
        for i in range(42, 47):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        cv2.line(img_copy, tuple(landmarks[47]), tuple(landmarks[42]), (0, 255, 0), 2)
        # Draw mouth
        for i in range(48, 59):
            cv2.line(img_copy, tuple(landmarks[i]), tuple(landmarks[i+1]), (0, 255, 0), 2)
        cv2.line(img_copy, tuple(landmarks[59]), tuple(landmarks[48]), (0, 255, 0), 2)
        
        return img_copy
