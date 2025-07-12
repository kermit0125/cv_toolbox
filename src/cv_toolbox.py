# src/cv_toolbox.py

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
from fpdf import FPDF

class CVToolbox:
    #Initialization method
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        if self.img is None:
            raise ValueError(f"Image not found at {image_path}")
        self.gray_img = None
        self.results = {}

    #Convert to grayscale
    def gray(self):
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.results["gray"] = self.gray_img

    #Apply Gaussian Blur
    def gaussian_blur(self, kernel_size=(5, 5)):
        blurred = cv2.GaussianBlur(self.img, kernel_size, 0)
        self.results["gaussian_blur"] = blurred

    #Applying edge detection
    def canny(self, threshold1=100, threshold2=200):
        if self.gray_img is None:
            self.gray()
        edges = cv2.Canny(self.gray_img, threshold1, threshold2)
        self.results["canny"] = edges

    # Call the SIFT method to detect and annotate keypoints:
    # 1. Uses OpenCV's internal processes including Gaussian pyramid,
    #    edge filtering, orientation assignment, and descriptor generation
    #    to detect stable keypoints.
    # 2. Stores the keypoints as a list of KeyPoint objects
    #    and as a multidimensional array of numeric feature descriptors.
    # 3. Draws the detected keypoints and their information onto the image.
    # 4. Saves all keypoint data and descriptors into a dictionary
    #    for further use or export as JSON.

    def sift(self):
        if self.gray_img is None:
            self.gray()
        sift = cv2.SIFT_create()
        kp, des = sift.detectAndCompute(self.gray_img, None)
        img_kp = cv2.drawKeypoints(
            self.gray_img,
            kp,
            None,
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )
        self.results["sift_image"] = img_kp
        self.results["sift_features"] = {
            "num_keypoints": len(kp),
            "keypoints": [
                {
                    "x": float(k.pt[0]),
                    "y": float(k.pt[1]),
                    "size": float(k.size),
                    "angle": float(k.angle)
                }
                for k in kp
            ],
            "descriptors": des.tolist() if des is not None else []
        }

    #Save the results to the "Output" folder
    def save_results(self, output_dir="outputs"):
        os.makedirs(output_dir, exist_ok=True)

        for key, img in self.results.items():
            if isinstance(img, np.ndarray):
                save_path = os.path.join(output_dir, f"{key}.png")
                if len(img.shape) == 2:
                    cv2.imwrite(save_path, img)
                else:
                    cv2.imwrite(save_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                print(f"Saved image: {save_path}")


        if "sift_features" in self.results:
            json_path = os.path.join(output_dir, "features.json")
            with open(json_path, "w") as f:
                json.dump(self.results["sift_features"], f, indent=2)
            print(f"Saved JSON: {json_path}")

    #Create the PDF file for the result
    def generate_report(self, output_path="outputs/report.pdf"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(0, 10, f"CV Toolbox Report", ln=True)

        for key in ["gray", "gaussian_blur", "canny", "sift_image"]:
            img_path = f"outputs/{key}.png"
            if os.path.exists(img_path):
                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, f"Result: {key}", ln=True)
                pdf.image(img_path, w=120)
                pdf.ln(10)

        if "sift_features" in self.results:
            pdf.set_font("Arial", size=12)
            features = self.results["sift_features"]
            pdf.cell(0, 10, f"Number of Keypoints: {features['num_keypoints']}", ln=True)

        pdf.output(output_path)
        print(f"Saved PDF report: {output_path}")
