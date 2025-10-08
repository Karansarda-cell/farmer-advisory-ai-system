# Setup Instructions

1. Create virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python run.py
   ```

3. Test API with sample input (e.g. using curl or Postman):
   ```bash
   curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d '{"voice_file":"data/audio/banana_query.wav","image_file":"data/images/banana_leaf_spot.jpg"}'
   ```
