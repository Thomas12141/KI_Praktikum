import tensorflow as tf
fashion_mnist = tf.keras.datasets.fashion_mnist


(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(fashion_mnist)