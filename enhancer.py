import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_image(input_path, output_path, chart_path):

    img = cv2.imread(input_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    denoised = cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 7, 15)

    blurred = cv2.GaussianBlur(denoised, (7, 7), 2)
    sharpened = cv2.addWeighted(denoised, 1.5, blurred, -0.5, 0)

    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    enhanced = cv2.filter2D(sharpened, -1, kernel)

    cv2.imwrite(output_path, enhanced)

    def stats(img):
        brightness = img.mean()
        contrast = img.std()
        sharpness = cv2.Laplacian(img, cv2.CV_64F).var()
        return brightness, contrast, sharpness

    o_b, o_c, o_s = stats(img_rgb)
    e_b, e_c, e_s = stats(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))

    labels = ["Brightness", "Contrast", "Sharpness"]
    orig = [o_b, o_c, o_s]
    new = [e_b, e_c, e_s]

    x = np.arange(len(labels))
    w = 0.35

    plt.figure(figsize=(7,5))
    plt.bar(x - w/2, orig, w, label="Original")
    plt.bar(x + w/2, new, w, label="Enhanced")
    plt.xticks(x, labels)
    plt.title("Deblur Comparison")
    plt.legend()
    plt.savefig(chart_path)
    plt.close()

    return {
        "original": {"brightness": o_b, "contrast": o_c, "sharpness": o_s},
        "enhanced": {"brightness": e_b, "contrast": e_c, "sharpness": e_s}
    }
