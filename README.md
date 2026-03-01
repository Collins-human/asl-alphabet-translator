# ASL Alphabet Translator

A real-time web application that recognizes American Sign Language (ASL) alphabet letters using a webcam and machine learning.

Developed as a final year project by **Collins Tumuheki** and **Nakitende Christine**  
Kabale University – Bachelor of Science in Computer Science – 2026

## Features
- Live webcam-based letter recognition
- Real-time word formation from signed letters
- Save words to personal list
- Alphabet guide (click to see sign image + audio)
- Multi-language support (English & Kiswahili)
- User login/logout
- Community feedback form with timestamps
- Dark mode toggle
- Responsive design

## How to Run (Local Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/Collins-human/asl-alphabet-translator.git
   cd asl-alphabet-translator


   Create and activate virtual environment (or use conda):Bash
   conda create -n sign_translator python=3.9 -y
conda activate sign_translator
Install dependencies: pip install flask tensorflow==2.10.0 numpy==1.23.5 opencv-python==4.8.1.78
Run the app:python app.py
Open in browser: http://127.0.0.1:5000

Login credentials (hardcoded for demo):

Username: collins / Password: password123
Username: christine / Password: kabaleuni2026
Username: guest / Password: guest123

Technologies Used

Backend: Flask (Python)
Machine Learning: TensorFlow (CNN model trained on ASL Alphabet dataset)
Frontend: HTML, CSS, JavaScript
Webcam: OpenCV
Other: NumPy, MediaPipe (hand detection optional)

Future Improvements

Database for users & saved words
Advanced community forum
Mobile optimization
Better model accuracy


License
MIT License – feel free to use and modify.
Made with Passion by Collins & Christine

   
