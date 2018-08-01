import tensorflow as tf
tf.reset_default_graph()
test_constant = tf.constant(10.0, dtype=tf.float32)
add_one_operation = test_constant + 1
with tf.Session() as sess:
    print(sess.run(add_one_operation))
input_data = tf.placeholder(dtype=tf.float32, shape=[None, 2])
double_operation = input_data * 2
with tf.Session() as sess:
    print(sess.run(double_operation, feed_dict={input_data:[[1, 2],[3,4]]}))
    print (double_operation)
