import time
import threading
import cv2
from collections import Counter
from .processor import QWXProcessor

shared = {'frame': None, 'running': True, 'confirmed': None}
lock = threading.Lock()
processor = QWXProcessor()

def recognition_loop():
    candidates = []
    while shared['running']:
        with lock:
            frame = shared['frame']
        if frame is None:
            time.sleep(0.01)
            continue
            
        results = processor.process_frame(frame)
        for res in results:
            candidates.append(res['plate'])
            freq = Counter(candidates)
            top_plate, count = freq.most_common(1)[0]
            
            if count >= 3:
                shared['confirmed'] = top_plate
                print(f"RECOGNIZED: {top_plate}")
                shared['running'] = False

if __name__ == "__main__":
    print("QWX Worker started on CPU")
    threading.Thread(target=recognition_loop, daemon=True).start()
