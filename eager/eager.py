import os
train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"
filename = os.path.basename(train_dataset_url)
if os.path.exists(filename):
  train_dataset_fp = tf.keras.utils.get_file(fname=filename, origin=train_dataset_url)
print("Local copy of the dataset file: {}".format(filename))

