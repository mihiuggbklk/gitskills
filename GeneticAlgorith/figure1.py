import numpy as np
import matplotlib.pyplot as plt

# 定义函数 f1 和 f2
def f1(x):
    return (x - 1) ** 2 + 1

def f2(x):
    return np.abs(x - 1) + 2

# 定义x的范围
x = np.linspace(-2, 4, 400)

# 创建图形
plt.figure(figsize=(6, 6))

# 画f1和f2
plt.plot(x, f1(x), label=r'$f_1(x)=(x-1)^2+1$')
plt.plot(x, f2(x), label=r'$f_2(x)=|x-1|+2$')


# 图形设置
plt.title(r'Graphs of $f_1(x)$ and $f_2(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()

# 保存图形为EPS文件
plt.savefig('figure1.eps', format='eps')

# 展示图形
plt.show()
