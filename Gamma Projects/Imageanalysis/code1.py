import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.preprocessing import image
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, Activation
from keras._tf_keras.keras import backend as k
import numpy as np


img_width, img_height = 150, 150
train_dataset = 'Gamma Projects/Imageanalysis/training_set'
test_dataset = 'Gamma Projects/Imageanalysis/test_set'
nb_train_samples = 500
nb_test_samples = 500
epochs = 100  # Reduced for practical purposes
batch_size = 32  # More practical batch size

if k.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dataset,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary',
    classes=['cats', 'dogs']
)

test_generator = test_datagen.flow_from_directory(
    test_dataset,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

# Plot some training images
plt.figure(figsize=(12, 12))
for i in range(0, 15):
    plt.subplot(5, 3, i + 1)
    for x_batch, y_batch in train_generator:
        image = x_batch[0]
        plt.imshow(image)
        break
plt.tight_layout()
plt.show()

# Check for GPU availability
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
if tf.config.experimental.list_physical_devices('GPU'):
    tf.config.experimental.set_memory_growth(tf.config.experimental.list_physical_devices('GPU')[0], True)
# Model Definition
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

# Compilation
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Training
training = model.fit(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=test_generator,
    validation_steps=nb_test_samples // batch_size
)

# Plot training & validation accuracy values
plt.plot(training.history['accuracy'])
plt.plot(training.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(training.history['loss'])
plt.plot(training.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Predict a new image
img_pred = image.load_img('Gamma Projects/Imageanalysis/test_set/dogs/dog.4990.jpg', target_size=(150, 150))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis=0)

# Normalize the input image
img_pred = img_pred / 255.0

rslt = model.predict(img_pred)
print(rslt)
if rslt[0][0] > 0.5:
    prediction = 'Dog'
else:
    prediction = 'Cat'
print('Prediction:', prediction)

img = mpimg.imread('Gamma Projects/Imageanalysis/test_set/dogs/dog.4990.jpg')
img_plot = plt.imshow(img)
plt.show()

