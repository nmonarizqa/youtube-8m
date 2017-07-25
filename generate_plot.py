from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import argparse
import cv2

# all thumbnail images
files = os.listdir("img")

def plot_colors(centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((1, 300, 3), dtype = "uint8")
	startX = 0

	# loop over the percentage of each cluster and the color of
	# each cluster
	for color in centroids:
		# plot the relative percentage of each cluster
		endX = startX + 100
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX

	# return the bar chart
	return bar

def get_colorbar(fname):
    im = nd.imread(os.path.join("img",fname))
    # cut to square
    sq = im[:,80:260]
    # reshape
    rs = sq.reshape(nrow*ncol,3)
    # kMeans to get top 3 colors
    km = KMeans(3)
    km.fit(rs)
    cc = km.cluster_centers_
    # get histogram
    the_bar = plot_colors(cc)

    row = the_bar[0,:]
    order = np.argsort(row[:,0])
    tb = the_bar[:,order]
    plt.imshow(tb)
    return tb, cc

if __name__ == '__main__':
    ccs = []
    the_list = []
    for i in range(len(files)):
        tb, cc = main(files[i])
        the_list.append(tb)
        ccs.append(cc)

    # plot the Data
    fig, ax = plt.subplots(1,1, figsize=(8,10))
    stck = np.vstack(the_list)
    ac = stck[:,102]
    # sort by second color
    order = np.argsort(ac.mean(1))
    plt.imshow(stck[order,:])
    plt.title("Top Three Dominant Colors for Each Thumbnail Image")
