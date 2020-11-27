# Bài toán: dựa vào chiều cao để dự đoán cân nặng.

import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu đầu vào và nhãn tương ứng.
# height (cm)
X = np.array(
    [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
Y = np.array([[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

ones = np.ones((X.shape[0], 1))

X_bar = np.hstack((X, ones))

A = np.dot(X_bar.T, X_bar)
B = np.dot(X_bar.T, Y)

w_star = np.dot(np.linalg.inv(A), B)

w1 = w_star[0][0]
w0 = w_star[1][0]

plt.plot(X, Y, "ro")

X = np.linspace(145, 185, 2)
Y = w1 * X + w0

plt.plot(X, Y)

plt.show()
