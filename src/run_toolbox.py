# run_toolbox.py
from cv_toolbox import CVToolbox

if __name__ == "__main__":
    image_path = "data/000000000139.jpg" #change the number of picture here
    toolbox = CVToolbox(image_path)


    toolbox.gray()
    toolbox.gaussian_blur()
    toolbox.canny()
    toolbox.sift()


    toolbox.save_results(output_dir="outputs")
    toolbox.generate_report(output_path="outputs/report.pdf")

    print("✅ All done!")
