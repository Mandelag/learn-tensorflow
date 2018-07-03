import os, sys
import tensorflow as tf
train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"
filename = os.path.basename(train_dataset_url)
if not os.path.exists(filename):
  train_dataset_fp = tf.keras.utils.get_file(fname=os.path.join(sys.path[0], filename), origin=train_dataset_url)
print("Local copy of the dataset file: {}".format(filename))


