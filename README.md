# 🧍‍♂️ Pose Estimator

**Pose Estimator** is a user-friendly application that leverages MediaPipe to detect human poses in images. It classifies the detected pose as **Standing**, **Sitting**, or **Lying Down**, and visually annotates the image with the identified landmarks.

---

## 🚀 Features

* **Human Pose Detection**: Utilizes MediaPipe's Pose solution to identify human body landmarks.
* **Pose Classification**: Determines if the person is standing, sitting, or lying down based on landmark positions.
* **Visual Annotation**: Displays the processed image with overlaid landmarks and pose classification.
* **Simple Interface**: Easy-to-use application suitable for beginners and developers alike.

---

## 📸 Demo

![Pose Estimation Demo](demo_image.jpg)

*Replace `demo_image.jpg` with an actual image demonstrating the application's output.*

---

## 🛠️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rktim/pose_estimator.git
   cd pose_estimator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Usage

1. **Prepare an Image**

   Ensure you have an image (e.g., `person.jpg`) in the project directory.

2. **Run the Application**

   ```bash
   python mp.py
   ```

3. **Follow the Prompt**

   The application will prompt you to enter the image filename:

   ```
   Enter image file name (with extension): person.jpg
   ```

4. **View the Result**

   The processed image will be displayed with landmarks and the classified pose.

---

## 🧠 How It Works

The application processes the input image using MediaPipe's Pose solution to detect body landmarks. It then calculates the vertical distance between the shoulder and hip landmarks to classify the pose:

* **Standing**: Significant vertical distance between shoulder and hip.
* **Sitting**: Moderate vertical distance.
* **Lying Down**: Minimal vertical distance.

This heuristic provides a simple yet effective method for basic pose classification.

---

## 📦 Dependencies

* [OpenCV](https://opencv.org/) - For image processing and display.
* [MediaPipe](https://mediapipe.dev/) - For pose detection.
* [Pillow](https://python-pillow.org/) - For image handling.
* [NumPy](https://numpy.org/) - For numerical operations.

All dependencies are listed in the `requirements.txt` file.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, improvements, or encounter issues, please open an [issue](https://github.com/Rktim/pose_estimator/issues) or submit a [pull request](https://github.com/Rktim/pose_estimator/pulls).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For any inquiries or feedback, please reach out via [GitHub Issues](https://github.com/Rktim/pose_estimator/issues).

---

Feel free to customize this `README.md` further to suit your project's needs. If you need assistance with additional features or deployment, don't hesitate to ask!
