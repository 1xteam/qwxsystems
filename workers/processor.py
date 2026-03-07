import cv2
from ultralytics import YOLO
from paddleocr import PaddleOCR
from .utils import normalize_plate, extract_plate

class QWXProcessor:
    def __init__(self):
        self.detector = YOLO('yolov8n.pt')
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)

    def preprocess(self, crop):
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=2, fy=2)
        gray = cv2.GaussianBlur(gray, (3,3), 0)
        gray = cv2.equalizeHist(gray)
        return gray

    def process_frame(self, frame):
        h = frame.shape[0]
        roi = frame[int(h*0.6):, :]
        results = self.detector(roi, verbose=False)
        
        plates = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
            crop = roi[y1:y2, x1:x2]
            if crop.size == 0: continue

            processed = self.preprocess(crop)
            ocr_results = self.ocr.ocr(processed, cls=False)
            
            if ocr_results and ocr_results[0]:
                for line in ocr_results[0]:
                    text, conf = line[1][0], float(line[1][1])
                    norm = normalize_plate(text)
                    plate = extract_plate(norm)
                    if plate and conf > 0.6:
                        plates.append({"plate": plate, "conf": conf})
        return plates
