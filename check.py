import tensorflow as tf
from tensorflow.python.client import device_lib


# Construct 2 op nodes (m1, m2) representing 2 matrix.
m1 = tf.constant([[3, 5]])
m2 = tf.constant([[2],[4]])

product = tf.matmul(m1, m2)    # A matrix multiplication op node

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(product))

sess.close()
