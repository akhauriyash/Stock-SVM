import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

# clf => classifier

clf = svm.SVC(gamma=0.0000001, C=100)
print(len(digits.data))

x, y = digits.data[:-15], digits.target[:-15]
clf.fit(x, y)

print('Prediction:', clf.predict(digits.data[-5]))
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
