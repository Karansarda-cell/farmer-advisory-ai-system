from app.image_model import predict_disease
from app.voice_model import transcribe_voice

def process_voice(file_path):
    return transcribe_voice(file_path)

def process_image(file_path):
    return predict_disease(file_path)
