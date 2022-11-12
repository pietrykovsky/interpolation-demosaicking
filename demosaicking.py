import numpy as np
from PIL import Image
import cv2

def get_demosaicked_image(image, mask):
    """
    Generate and return demosaicked image.
    """
    img = np.array(image)
    R, G, B = np.array([cv2.filter2D(img[:,:,n], -1, mask[n]) for n in range(3)])
    color_masks = np.dstack((R, G, B))
    result = Image.fromarray(color_masks)

    return result