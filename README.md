# 🖼️ Image Filtering and Feature Extraction Toolbox

A Python toolbox for basic computer vision operations, including:

- Grayscale conversion
- Gaussian blur filtering
- Edge detection (Canny)
- SIFT feature extraction
- Saving results as images and JSON
- Automatically generating a PDF report

---

## 🚀 Features

1. **Grayscale Conversion**  
   Convert RGB images to grayscale.

2. **Gaussian Blur**  
   Smooth images using a Gaussian kernel.

3. **Edge Detection (Canny)**  
   Detect edges in images.

4. **SIFT Feature Extraction**  
    - Detect keypoints
    - Compute descriptors
    - Visualize features
    - Export keypoints and descriptors as JSON

5. **PDF Report Generation**  
   Compile all results into a single PDF summary.

---

## 📂 Project Structure

```
Project Root/
│
├── data/
│      your_image.jpg
│
├── outputs/
│      gray.png
│      gaussian_blur.png
│      canny.png
│      sift_image.png
│      features.json
│      report.pdf
│
├── src/
│      cv_toolbox.py
│      run_toolbox.py
│
├── requirements.txt
└── README.txt
```

---

## ⚙️ Installation

### 1. Create a virtual environment

**Windows (PowerShell):**

```
python -m venv myenv
.\myenv\Scripts\activate
```

**macOS / Linux:**

```
python3 -m venv myenv
source myenv/bin/activate
```

---

### 2. Install requirements

```
pip install -r requirements.txt
```

---

## 📝 How to Run

Edit the image path in `run_toolbox.py`:

```
image_path = "data/your_image.jpg"
```

Then run:

```
python -m src.run_toolbox
```

All results will be saved under the `outputs/` folder.

---

## 📊 Example Outputs

Outputs generated:

- gray.png             (grayscale image)
- gaussian_blur.png    (blurred image)
- canny.png            (edges detected)
- sift_image.png       (keypoints visualized)
- features.json        (keypoints + descriptors)
- report.pdf           (PDF report with images)

---

## 📄 JSON Example

Sample from `features.json`:

```
{
  "num_keypoints": 120,
  "keypoints": [
    {
      "x": 50.2,
      "y": 30.1,
      "size": 2.4,
      "angle": 45.0
    }
  ],
  "descriptors": [[...], [...], ...]
}
```

---

## 💻 Requirements

- Python 3.8+
- OpenCV
- NumPy
- FPDF
- Matplotlib (optional for plotting)

---

## License

MIT License

---

## Author

Keming Xing
