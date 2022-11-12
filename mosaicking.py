import numpy as np
from PIL import Image

def get_mosaic_from_image(image, mask):
    """
        Generate CFA from image with a given mask.
        Mask must be an square array of uint8 dtype.
    """
    offset = mask.shape[0]
    assert mask.shape[1] == offset
    arr = np.array(image)
    width, height = image.size
    x = y = 0
    for x in range(0, height, offset):
        for y in range(0, width, offset):
            if x+offset < height and y+offset < width:
                arr[x:x+offset, y:y+offset] *= mask
            elif y+offset > width and x+offset < height:
                arr[x:x+offset, y:width] *= mask[:,:width-y]
            elif y+offset < width and x+offset > height:
                arr[x:height, y:y+offset] *= mask[:height-x,:]
            else:
                arr[x:height, y:width] *= mask[:height-x,:width-y]
           
    result = Image.fromarray(arr)
    return result