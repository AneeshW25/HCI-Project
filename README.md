# 🎤 PPT Voice Explainer using Generative AI

## 📌 Overview

The PPT Voice Explainer is an intelligent presentation system that converts static PowerPoint slides into a fully narrated, automated presentation.

The system extracts slide content, generates human-like explanations using AI (or local NLP fallback), converts them into speech, and synchronizes audio with slide transitions.

---

## 🎯 Objectives

* Transform static PPT slides into interactive narrated presentations
* Reduce cognitive load for users
* Improve accessibility using audio explanations
* Automate presentation delivery

---

## 🚀 Features

* 📂 Upload `.pptx` files
* 🧠 AI-based explanation generation
* 🔊 Text-to-Speech (TTS) narration
* 🖼 Slide-to-image conversion
* ▶️ Auto slide transition with audio
* ⏯ Manual controls (next/previous)
* ⚡ Real-time presentation playback
* 🔁 Offline fallback (no API required)

---

## 🏗 System Architecture

```
Frontend (HTML/JS)
        ↓
Backend (FastAPI)
        ↓
PPT Parser → AI Generator → TTS Engine
        ↓
LibreOffice → Poppler → Slide Images
        ↓
Frontend Display + Audio Sync
```

---

## 🔄 Workflow

1. User uploads PPT file
2. Slides are extracted using `python-pptx`
3. PPT converted to PDF → Images
4. AI generates explanation for each slide
5. Explanation converted to speech
6. Frontend displays slides + plays audio
7. Slides auto-transition after narration

---

## 🛠 Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python (FastAPI)

### Libraries & Tools

* `python-pptx` → Slide extraction
* `gTTS` → Text-to-Speech
* `pdf2image` → PDF to images
* LibreOffice → PPT to PDF
* Poppler → Image rendering

### AI Options

* OpenAI (GPT) *(optional)*
* Claude (Anthropic) *(optional)*
* Local NLP generator *(default for demo)*

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd ppt-voice-explainer
```

---

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Install External Tools

#### LibreOffice

Download & install from:
https://www.libreoffice.org/

#### Poppler (Windows)

Download from:
https://github.com/oschwartz10612/poppler-windows/releases/

Extract to:

```
C:\poppler-xx.x.x
```

---

### 4. Run Backend

```bash
uvicorn app:app --reload
```

---

### 5. Run Frontend

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://127.0.0.1:5500
```

---

## ▶️ Usage

1. Open the frontend
2. Upload a `.pptx` file
3. Click **Start Presentation**
4. System will:

   * Process slides
   * Generate explanation
   * Play audio
   * Auto-switch slides

---

## 🧠 HCI Concepts Applied

* Feedback (loading messages, transitions)
* Consistency (uniform slide flow)
* Visibility (clear slide + explanation display)
* Cognitive Load Reduction (guided narration)
* Accessibility (audio support)

---

## ⚠️ Challenges Faced

* PPT to image conversion setup
* File path handling issues
* API quota limitations
* Synchronization of audio with slides

---

## ✅ Solutions

* Used absolute paths for stability
* Implemented offline explanation generator
* Added UI feedback (“Starting presentation…”)
* Used audio events for slide synchronization

---

## 🔮 Future Scope

* Real-time voice synthesis
* Multilingual support
* Cloud deployment (AWS)
* Interactive Q&A system
* Voice-controlled navigation

---

## 📊 Applications

* 🎓 Education & e-learning
* 🏢 Corporate presentations
* ♿ Accessibility tools
* 📚 Self-learning systems

---

## 📌 Conclusion

This project demonstrates how AI and HCI can be combined to convert passive slide content into an **interactive, automated presentation system**, improving usability, accessibility, and user experience.

---

## 👨‍💻 Author

* Name: ANEESH WANJARE
* Project: HCI Mini Project / Final Project

---

## 📎 Note

For demo purposes, a **local explanation generator** is used to ensure reliability without API dependency. The system is designed to integrate with AI APIs like OpenAI or Claude when required.

---
