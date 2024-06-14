import tensorflow as tf
fashion_mnist = tf.keras.datasets.fashion_mnist

# x und y Werte von fashion_mnist laden und auf Werten zwischen 0 und 1 normalisieren.
(x_train, y_train), (x_test, y_test) = fashion_mnist .load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("NN1")
# Neurale Netze aufbauen NN1.
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])


# Vorhersagen für jeden Datensatz
predictions = model(x_train[:1]).numpy()
# Vorhersagen in Wahrscheinlichkeiten umwandeln
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
# Kompelirien
model.compile(
    optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy']
)
# Training mit 5 Iterationen.
model.fit(x_train, y_train, epochs=5)

# Bewertung des Modells auf den Testdaten
model.evaluate(x_test, y_test, verbose=2)

# Erstellen eines Modells, das Wahrscheinlichkeiten ausgibt
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

# Ausgabe des tatsächlichen Labels des ersten Testbeispiels
print(y_test[:1])

# Vorhersage der Wahrscheinlichkeit für das erste Testbeispiel
probability_model(x_test[:1])