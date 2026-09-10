import numpy as np

class MnistDataset:
    def __init__(self):

        self.images = np.zeros((2, 28, 28))

        # =========================
        # Image 0 → digit 6
        # =========================

        self.images[0, 4:7, 9:19] = 255
        self.images[0, 7:11, 7:11] = 255
        self.images[0, 10:23, 6:9] = 255
        self.images[0, 20:24, 9:19] = 255
        self.images[0, 17:21, 17:21] = 255
        self.images[0, 13:18, 18:21] = 255
        self.images[0, 11:14, 10:19] = 255

        # =========================
        # Image 1 → digit 1
        # =========================

        self.images[1, 5:9, 14:18] = 255
        self.images[1, 8:23, 12:18] = 255
        self.images[1, 21:24, 10:20] = 255

        return self.images