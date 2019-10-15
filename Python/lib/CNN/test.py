from PIL import Image
import numpy as np
from CNN import *
# The mnist package handles the MNIST dataset for us!
# Learn more at https://github.com/datapythonista/mnist
train_images = mnist.train_images()
train_labels = mnist.train_labels()

conv = Conv2D(3,3, num_filters=3)
output = conv.forward(train_images[0])
print(output) # (26, 26, 8)

img = Image.fromarray(output, 'RGB')
img.save('CNN.png')
img.show()