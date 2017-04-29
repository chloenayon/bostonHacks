from PIL import Image, ImageFilter
import numpy as np
import random
import math


HIDDEN_LAYERS_SIZE = 100

im = Image.open('helloWorld.png')
#pixels = list(im.getdata())
width, height = im.size



#b = im.load()

im = np.asarray(Image.open('helloWorld.png').convert('L'))

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def activation(arr, rows, cols):
    for n in range(rows):
        for m in range(cols):
            arr[n, m] = sigmoid(arr[n,m])

######################## FORWARD PROPAGATION ##############################

######################## LAYER ONE #############################

layerOne = np.random.random((width,HIDDEN_LAYERS_SIZE))

hiddenLayer = np.dot(im, layerOne)

activation(hiddenLayer, height, HIDDEN_LAYERS_SIZE)



#layerOne = [[random.random() for i in range(width)] for i in range (100)]

#print layerOne[10,10]


#print im

#im.show()


