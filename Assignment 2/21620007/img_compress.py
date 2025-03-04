#PRN:21620007
#Name:Shashikant Sunil Mane
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

#Read the image
image = io.imread('photo.jpeg')
io.imshow(image)
io.show()

#Dimension of the original image
rows = image.shape[0]
cols = image.shape[1]

#Flatten the image
image = image.reshape(rows*cols, 3)

#Implement k-means clustering to form k clusters
kmeans = KMeans(n_clusters=64)
kmeans.fit(image)

#Replace each pixel value with its nearby centroid
compressed_image = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = np.clip(compressed_image.astype('uint8'), 0, 255)

#Reshape the image to original dimension
compressed_image = compressed_image.reshape(rows, cols, 3)

#Save and display output image
io.imsave('after.jpeg', compressed_image)
io.imshow(compressed_image)
io.show()
