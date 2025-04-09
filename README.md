# **Face Emoji Overlay Project** 🎭  

**A fun real-time face replacement tool that covers your entire head with an emoji using Python, OpenCV, and MediaPipe!**  

## **📌 Overview**  
This project detects faces in real-time using **MediaPipe's Face Mesh** and overlays a custom emoji (or any image) over the entire face. It’s perfect for creating funny videos, live filters, or privacy masking.  

### **✨ Features**  
✔ **Real-time face detection** using **MediaPipe Face Mesh**  
✔ **Full-head emoji overlay** (adjusts to face size)  
✔ **Transparency support** (PNG with alpha channel)  
✔ **FPS counter** to monitor performance  
✔ **Multi-face support** (works with multiple people in frame)  
✔ **Customizable resolution & brightness**  

---

## **🚀 Installation**  

### **📦 Requirements**  
- Python 3.7+  
- OpenCV (`pip install opencv-python`)  
- MediaPipe (`pip install mediapipe`)  

### **🔧 Setup**  
1. **Clone the repository** (if applicable):  
   ```bash
   git clone https://github.com/yourusername/full-face-emoji.git
   cd full-face-emoji
   ```
2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your emoji** (must be a **PNG with transparency**) and name it `emoji.png` in the project folder.  

---

## **🎮 Usage**  
Run the script:  
```bash
python face_emoji_overlay.py
```  

### **🖥️ Controls**  
- **Press `X`** to exit the application  
- **FPS counter** shows performance in real-time  

### **⚙️ Customization**  
- **Change emoji**: Replace `emoji.png` with your own image (keep transparency).  
- **Adjust resolution**: Modify `frameWidth` and `frameHeight` in the code.  
- **Brightness control**: Change `cam.set(10, 150)` (higher = brighter).  

## **💡 Possible Improvements**  
- **Add rotation** to make the emoji follow head tilts  
- **Dynamic resizing** for smoother transitions  
- **GUI controls** for emoji selection & settings  

---

## **📜 License**  
This project is open-source under the **MIT License**.  

**Enjoy hiding your face behind emojis!** 😷🎭
