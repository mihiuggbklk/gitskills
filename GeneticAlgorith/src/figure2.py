import numpy as np
import matplotlib.pyplot as plt

# 定义函数 f1 和 f2
def f1(x):
    return (x - 1)**2 + 1

def f2(x):
    return (x - 2)**2 + 1

# 创建 x 的取值范围
x = np.linspace(-2, 5, 400)

# 计算 y 的值
y1 = f1(x)
y2 = f2(x)

# 创建图像
plt.figure(figsize=(6, 6))
plt.plot(x, y1, label='$f_1(x)=(x-1)^2+1$', color='blue')
plt.plot(x, y2, label='$f_2(x)=(x-2)^2+1$', color='red')
plt.title('Graphs of $f_1(x)$ and $f_2(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 保存为eps文件
plt.savefig("figure2.eps", format='eps')

# 显示图像
plt.show()
