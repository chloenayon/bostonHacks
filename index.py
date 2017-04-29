from PIL import Image, ImageFilter
import numpy as np
import random
import math
from numpy import array

HIDDEN_LAYERS_SIZE = 100
OUTPUT_SIZE = 26

im = Image.open('helloWorld.png')
input = np.asarray(im)

print input.size

INPUT_SIZE = input.size

#print input.length

#pixels = list(im.getdata())
#width, height = im.size

#print pixels

#b = im.load()

#im = np.asarray(Image.open('helloWorld.png').convert('L'))

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def activation(arr, rows, cols):
    for n in range(rows):
        for m in range(cols):
            arr[n, m] = sigmoid(arr[n,m])


######################## INPUT LAYER ######################################

weights_0 = np.random.random((100, INPUT_SIZE))
bias_0 = np.random.rand(INPUT_SIZE)

hiddenLayer = weights_0.dot(input) + bias_0

#print hiddenLayer
#activation(hiddenLayer, height, HIDDEN_LAYERS_SIZE)

########################## HIDDEN LAYER ###################################


    

###########################################################################





####################### LAST STEP #########################################



#layerOne = [[random.random() for i in range(width)] for i in range (100)]

#print layerOne[10,10]


#print im

#im.show()


