import os

class WorkerConfig:
    MODEL_PATH = os.getenv("MODEL_PATH", "models/yolov8n.pt")
    CONFIDENCE_THRESHOLD = float(os.getenv("CONF_THRESHOLD", 0.45))
    ALPR_ENABLED = os.getenv("ALPR_ENABLED", "True").lower() == "true"
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    DEVICE = "cpu" # Default to CPU for ARM64 optimization
