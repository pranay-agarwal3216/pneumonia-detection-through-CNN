import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from glob import glob
import matplotlib.pyplot as plt

IMAGE_SIZE = [224, 224]

train_path = 'kaggle_data/chest_xray/train'
valid_path = 'kaggle_data/chest_xray/test'

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

for layer in vgg.layers:
    layer.trainable = False
# useful for getting number of output classes
folders = glob('kaggle_data/chest_xray/train/*')
# our layers - you can add more if you want
x = Flatten()(vgg.output)
prediction = Dense(len(folders), activation='softmax')(x)

# create a model object
model = Model(inputs=vgg.input, outputs=prediction)
model.summary()
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)
training_set = train_datagen.flow_from_directory('kaggle_data/chest_xray/train',
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')
test_set = test_datagen.flow_from_directory('kaggle_data/chest_xray/test',
                                            target_size=(224, 224),
                                            batch_size=32,
                                            class_mode='categorical')
r = model.fit_generator(training_set,
                        validation_data=test_set,
                        epochs=5,
                        steps_per_epoch=len(training_set),
                        validation_steps=len(test_set)
                        )
plt.plot(r.history['loss'], label='train loss')
plt.plot(r.history['val_loss'], label='val loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')

import tensorflow as tf
from keras.models import load_model

model.save('model_vgg16.h5')

