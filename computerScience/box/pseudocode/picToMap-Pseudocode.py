import numpy as np
from PIL import Image
FUNCTION generateMap(map):
    im <- Image.open(map)
    im <- im.transpose(Image.FLIP_TOP_BOTTOM)
    im <- im.convert("L")
    data <- im.getdata()
    data <- np.ndarray.tolist(np.matrix(data).reshape(40,140))
    RETURN data
ENDFUNCTION