from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from skimage import io, color, feature, transform


mnist = datasets.load_digits()
images = mnist.images
data_size = len(images)
#Preprocessing images
images = images.reshape(-1, 1)
# Reshape the image to a 2D array because we are analizying a single example

labels = mnist.target
#Initialize Logistic Regression
LR_classifier = LogisticRegression(C=0.01, penalty='l2', tol=0.01)
#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Lo
LR_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])
#Load a custom image
digit_img = io.imread('../media/digit.png')

#Convert image to grayscale
digit_img = color.rgb2gray(digit_img)
#Resize the image to 28x28
digit_img = transform.resize(digit_img, (8, 8), mode="wrap")
#Run edge detection on the image
digit_edge = feature.canny(digit_img, sigma=5)
digit_edge = digit_edge.flatten()#Testing the data
prediction = LR_classifier.predict(digit_edge)
print(prediction)