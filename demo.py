# coding: utf-8

# a = 'BANC'
# b = 'ABC'
# print b.split('')
# if set(b) in set(a):
#     print 'ok'


import numpy as np
import keras
from sklearn.preprocessing import LabelEncoder

a = ['apple','banana','banana','tomato','carrot']
encoder = LabelEncoder()
encoder.fit(a)
a_encoder = encoder.transform(a)
print a_encoder
num_classes = np.max(a_encoder)+1
print num_classes
a_encoder = keras.utils.to_categorical(a_encoder, num_classes)
print a_encoder