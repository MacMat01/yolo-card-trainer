import os

import numpy as np

from card_measures import *

data_dir = "data"  # Directory that will contain all kinds of data (the data we download and the data we generate)

if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

#TODO modificare suits e values in base alle esigenze
card_suits = ['a', 'p', 'o', 'b']
card_values = ['1', '2', '3', '4', '5']

#TODO modificare dataset_name in base alle esigenze
dataset_name = "strategic-fruits-card-detection-dataset"

# Pickle file containing the background images from the DTD
backgrounds_pck_fn = data_dir + "/backgrounds.pck"

# Pickle file containing the card images
cards_pck_fn = data_dir + "/cards.pck"

# imgW,imgH: dimensions of the generated dataset images 
imgW = 736
imgH = 736

refCard = np.array([[0, 0], [cardWidth, 0], [cardWidth, cardHeight], [0, cardHeight]], dtype=np.float32)
refCardRot = np.array([[cardWidth, 0], [cardWidth, cardHeight], [0, cardHeight], [0, 0]], dtype=np.float32)
refCornerHL = np.array(
    [[cornerXmin, cornerYmin], [cornerXmax, cornerYmin], [cornerXmax, cornerYmax], [cornerXmin, cornerYmax]],
    dtype=np.float32)
refCornerLR = np.array([[cardWidth - cornerXmax, cardHeight - cornerYmax], [cardWidth - cornerXmin, cardHeight - cornerYmax],
                        [cardWidth - cornerXmin, cardHeight - cornerYmin], [cardWidth - cornerXmax, cardHeight - cornerYmin]],
                       dtype=np.float32)
refCorners = np.array([refCornerHL, refCornerLR])
