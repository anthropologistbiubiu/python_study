import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建一个图形和轴
fig, ax = plt.subplots()

# 绘制数据
ax.plot(x, y)

# 添加标题和标签
ax.set_title('Basic Line Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# 显示图形
plt.show()
