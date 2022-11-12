from PIL import Image
import numpy as np

from mosaicking import get_mosaic_from_image
from demosaicking import get_demosaicked_image

if __name__ == "__main__":
    R = 1, 0 ,0
    G = 0, 1, 0
    B = 0, 0, 1

    bayer = np.array([[G,R],
                      [B,G]], 'uint8')
    bayer_kernel = np.array([np.ones((2, 2)) * w for w in [1, 1/2, 1]])
    
    xtrans = np.array([[G,B,R,G,R,B],
                       [R,G,G,B,G,G],
                       [B,G,G,R,G,G],
                       [G,R,B,G,B,R],
                       [B,G,G,R,G,G],
                       [R,G,G,B,G,G]], 'uint8')
    xtrans_mask = np.array([[0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
                            [0.  , 0.25, 0.5 , 0.5 , 0.25, 0.  ],
                            [0.  , 0.5 , 1.  , 1.  , 0.5 , 0.  ],
                            [0.  , 0.5 , 1.  , 1.  , 0.5 , 0.  ],
                            [0.  , 0.25, 0.5 , 0.5 , 0.25, 0.  ],
                            [0.  , 0.  , 0.  , 0.  , 0.  , 0.  ]])
    xtrans_kernel = np.array([xtrans_mask * w for w in [1/2, 1/5, 1/2]])

    with Image.open('4demosaicking.bmp') as img:
        bayer_img = get_mosaic_from_image(img, bayer)
        bayer_img.save('bayer.bmp')
        debayer_img = get_demosaicked_image(bayer_img, bayer_kernel)
        debayer_img.save('debayer.bmp')

        xtrans_img = get_mosaic_from_image(img, xtrans)
        xtrans_img.save('xtrans.bmp')
        dextrans_img = get_demosaicked_image(xtrans_img, xtrans_kernel)
        dextrans_img.save('dextrans.bmp')