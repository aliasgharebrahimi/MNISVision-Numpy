import numpy as np
from mnist_dataset import Mnist

class Conv2:
    def __init__(self, data, in_channels, out_channels, kernel_size,  batch_size, stride=1):
        self.batch_size = batch_size
        self.data = data
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride

    def conv(self):
        s = 0
        x = 0

        # ساخت کرنل رندوم
        self.kernel_random = np.random.rand(self.kernel_size, self.kernel_size)

        # بنچ بتچ کردن دیتاست
        for i in range(0, len(self.data), self.batch_size):
            self.data_batch = self.data[i: i + self.batch_size]
            # ساخت ماتریس خالی برای گذشتن اعداد خروجی
            self.output = np.zeros((
                self.data_batch.shape[1] - self.kernel_size + 1,
                self.data_batch.shape[2] - self.kernel_size + 1
            ))

            # کشیدن بیرون مربع به اندازه کرنل سایز از عکس
            for row in range(0, self.data_batch.shape[1] - self.kernel_size + 1):
                for col in range(0, self.data_batch.shape[1] - self.kernel_size + 1):

                    self.kernel_target = self.data_batch[0, row: row + self.kernel_size, col: col + self.kernel_size]
                    if self.kernel_target.shape == self.kernel_random.shape:
                        self.dot = np.sum(self.kernel_target * self.kernel_random)

                        self.output[row: col] += self.dot

        return self.output

ob = Conv2(Mnist, 1, 6, 3, 1, 1)
ob.conv()