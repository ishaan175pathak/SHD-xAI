import os
import cv2
import random
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------
# Paths
# -------------------------
IMAGE_DIR = Path("data/raw/Images")
MASK_DIR = Path("data/raw/Masks")

# -------------------------
# Get file list
# -------------------------
image_files = os.listdir(IMAGE_DIR)

def show_sample(img_path, mask_path):
    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Image")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title("Mask")
    plt.imshow(mask, cmap="gray")
    plt.axis("off")

    plt.show()


# -------------------------
# Random samples
# -------------------------

for _ in range(5):
    img_name = random.choice(image_files)

    img_path = os.path.join(IMAGE_DIR, img_name)
    mask_path = os.path.join(MASK_DIR, img_name.replace(".jpg", ".PNG"))

    print(os.listdir(MASK_DIR))

    if os.path.exists(mask_path):
        show_sample(img_path, mask_path)