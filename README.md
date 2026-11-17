# 🏋️ AI Gym Coach – AI-Powered Personal Fitness Assistant

An AI-powered fitness coaching application that helps users monitor their workouts, track exercise performance, and receive intelligent feedback on exercise form using computer vision and Generative AI.

AI Gym Coach combines **Computer Vision, MediaPipe, Streamlit, and Groq LLM** to create an interactive workout assistance experience.

## 🌟 Project Overview

AI Gym Coach is designed to act as a virtual fitness assistant. It uses real-time video processing and pose estimation to analyze body movements during workouts.

The application processes exercise movements, tracks workout metrics, identifies potential form issues, and provides AI-generated coaching feedback to help users improve their exercise technique.

## ✨ Key Features

- **Real-Time Pose Detection:** Uses MediaPipe to detect and track body landmarks.
- **Exercise Tracking:** Monitors exercise repetitions and workout performance.
- **Form Analysis:** Identifies potential exercise form issues using movement analysis.
- **AI-Powered Coaching:** Generates personalized workout feedback using Groq LLM.
- **Voice Feedback:** Provides audio-based coaching using Text-to-Speech.
- **Workout Metrics:** Tracks repetitions, sets, and exercise-related metrics.
- **Interactive Dashboard:** Streamlit-based interface for workout monitoring.
- **Live Video Processing:** Uses WebRTC for real-time video streaming.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Computer Vision | OpenCV |
| Pose Estimation | MediaPipe |
| Video Streaming | Streamlit WebRTC |
| Generative AI | Groq API |
| LLM | Groq-supported language models |
| Text-to-Speech | gTTS |
| Data Processing | NumPy, Pandas |
| Environment Management | Python dotenv |
| Deployment | Streamlit Community Cloud |
 
## 🏗️ Project Architecture

```text
AI_GYM_COACH/
│
├── core/
│   └── Core application logic
│
├── detectors/
│   └── Exercise detection and movement analysis
│
├── ml_models/
│   └── Machine learning and pose model files
│
├── services/
│   ├── coaching/
│   │   ├── llm.py
│   │   ├── tts.py
│   │   └── voice_pipeline.py
│   │
│   ├── tracking/
│   │   └── metrics.py
│   │
│   └── vision/
│       └── exercise_viedo_processor.py
│
├── static/
│
├── .streamlit/
│
├── tutorial-info/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── packages.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sahil-0905/AI_GYM_COACH.git
```

### 2. Navigate to the Project Directory

```bash
cd AI_GYM_COACH
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r tutorial-info/requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file inside the `tutorial-info` directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

Get your API key from:

https://console.groq.com/keys

**Important:** Never upload your API key or `.env` file to GitHub.

### 6. Run the Application

From the project root directory, execute:

```bash
python -m streamlit run tutorial-info/main.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🧠 How It Works

1. **Video Input:** The application receives live video through the webcam.
2. **Pose Estimation:** MediaPipe detects body landmarks from video frames.
3. **Movement Analysis:** Exercise detection logic processes body movements.
4. **Workout Tracking:** Repetitions, sets, and exercise metrics are updated.
5. **AI Feedback:** The Groq-powered LLM generates contextual coaching feedback.
6. **Voice Assistance:** The voice pipeline converts feedback into audio using Text-to-Speech.

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

**Live Demo:**  
https://ai-gym-coach-sahil.streamlit.app/

Deployment requirements:
- Python 3.11
- Dependencies configured in `tutorial-info/requirements.txt`
- System packages configured through `packages.txt`
- Groq API key configured in Streamlit Cloud Secrets

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key for Groq LLM integration |

## 🚀 Future Enhancements

- Support for additional exercises and workout routines.
- Improved exercise form analysis and accuracy.
- Personalized workout plans based on user performance.
- Workout history and progress visualization.
- Advanced fitness analytics.
- Integration with wearable fitness devices.
- More intelligent voice-based interaction.

## 👨‍💻 Developer

**Sahil Kumar**

B.Tech Student | AI/ML Enthusiast | Full Stack Developer

- **GitHub:** https://github.com/sahil-0905
- **Project Repository:** https://github.com/sahil-0905/AI_GYM_COACH

---

⭐ If you find this project interesting, consider giving it a star on GitHub!

*AI Gym Coach – Your Virtual Personal Fitness Assistant.*
