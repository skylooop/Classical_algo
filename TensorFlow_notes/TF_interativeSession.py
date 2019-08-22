import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.constant([[1.,2.]])
negMatrix = tf.negative(x)
res = negMatrix.eval()
print(res)
sess.close()
