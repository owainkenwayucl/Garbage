# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import termshow
from tensorflow.python import ipu

print(tf.__version__)

# Get the dataset
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Names of classes in the dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
     
# Images are stored as integer greyscale - convert to float brightness
train_images = train_images / 255.0
test_images = test_images / 255.0


# Configure the IPU system
cfg = ipu.config.IPUConfig()
cfg.auto_select_ipus = 1
cfg.configure_ipu_system()

# Create an IPU distribution strategy.
strategy = ipu.ipu_strategy.IPUStrategy()

with strategy.scope():

    # Set up layers     
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    # Train it     
    model.fit(train_images, train_labels, epochs=10)

    # Test its loss on the test data aka how accurate is it
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2, batch_size=10)

    print('\nTest accuracy:', test_acc)

    # Add a layer that shows us probabilities
    probability_model = tf.keras.Sequential([model, 
                tf.keras.layers.Softmax()])

    # Display the first test image
    termshow.show(test_images[0].transpose())

    # Generate probabilities for the set of test images
    predictions = probability_model.predict(test_images, batch_size=10)

    # Print the most likely class for the first image
    print(class_names[np.argmax(predictions[0])])



