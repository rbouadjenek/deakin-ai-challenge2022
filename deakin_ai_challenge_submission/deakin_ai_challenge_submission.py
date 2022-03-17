# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022. Reda Bouadjenek, Deakin University                      +
#     Email:  reda.bouadjenek@deakin.edu.au                                    +
#                                                                              +
#  Licensed under the Apache License, Version 2.0 (the "License");             +
#   you may not use this file except in compliance with the License.           +
#    You may obtain a copy of the License at:                                  +
#                                                                              +
#                 http://www.apache.org/licenses/LICENSE-2.0                   +
#                                                                              +
#    Unless required by applicable law or agreed to in writing, software       +
#    distributed under the License is distributed on an "AS IS" BASIS,         +
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  +
#    See the License for the specific language governing permissions and       +
#    limitations under the License.                                            +
#                                                                              +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import sys, os, h5py
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.python.keras.saving import hdf5_format

if __name__ == "__main__":
    if len(sys.argv) == 1:
        input_dir = '.'
        output_dir = '.'
    else:
        input_dir = os.path.abspath(sys.argv[1])
        output_dir = os.path.abspath(sys.argv[2])

    print("Using input_dir: " + input_dir)
    print("Using output_dir: " + output_dir)
    print(sys.version)
    print("Tensorflow version: " + tf.__version__)

    # Loading the model.
    model = 'model.h5'
    with h5py.File(model, mode='r') as f:
        model_loaded = hdf5_format.load_model_from_hdf5(f)
        print(model_loaded.summary())
        try:
            answers = f.attrs['class_names']
        except:
            answers = ['yes', 'no', '0', '1', '2', '3', '4', '5',  # Numbers
                       'black', 'white', 'red', 'yellow', 'brown', 'blue', 'gray', 'green', 'orange',  # Colors
                       'right', 'left', 'woman', 'man', 'day', 'night', 'open', 'closed', 'top', 'down', 'fire',
                       'water',
                       'glasses', 'glass', 'tree', 'tv', 'table', 'couch', 'book', 'car', 'ball',  # Objects
                       'happy', 'sad', 'laughing',  # Expressions
                       'eating', 'drinking', 'playing', 'walking', 'reading', 'cooking', 'sitting', 'standing',
                       'sleeping'  # Actions
                       ]

    input_shape = model_loaded.input_shape
    image_size = np.array(input_shape[0][1:3])

    print('Size of inputs images: ' + str(image_size))
    # Reading test images.    
    # files = []
    # images = []
    # for file in os.listdir(input_dir):
    #     if file.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
    #         img = image.load_img(os.path.join(input_dir, file),
    #                              target_size=image_size)
    #         x = image.img_to_array(img)
    #         x = np.expand_dims(x, axis=0)
    #         images.append(x)
    #         files.append(file)
    # images = np.vstack(images)
    #
    # # Making predictions!
    # batch_size = 16
    # y_proba = model_loaded.predict(images, batch_size=batch_size)
    # y_predict = np.argmax(y_proba, axis=1)
    # # Writting predictions to file.
    # with open(os.path.join(output_dir, 'answer.txt'), 'w') as result_file:
    #     for i in range(len(files)):
    #         result_file.write(files[i] + ',' + answers[y_predict[i]] + '\n')
