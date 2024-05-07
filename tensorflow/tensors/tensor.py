import tensorflow as tf

# 创建两个张量
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

# 加法
add_result = tf.add(a, b)

# 减法
sub_result = tf.subtract(a, b)

# 乘法
mul_result = tf.matmul(a, b)

# 除法
div_result = tf.divide(a, b)

# 矩阵转置
transpose_result = tf.transpose(a)

# 张量索引和切片
slice_result = a[:, 0]

# 获取张量的形状
shape = tf.shape(a)

# 打印张量的值
with tf.Session() as sess:
    print("Addition result:", sess.run(add_result))
    print("Subtraction result:", sess.run(sub_result))
    print("Multiplication result:", sess.run(mul_result))
    print("Division result:", sess.run(div_result))
    print("Transpose result:", sess.run(transpose_result))
    print("Slice result:", sess.run(slice_result))
    print("Shape:", sess.run(shape))
