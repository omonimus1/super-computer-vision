from skimage import data, segmentation, color
from skimage import io
from skimage import data
from skimage.future import graph

imgage_to_analize = io.imread('../media/animal.jpeg')
img_segments = segmentation.slic(imgage_to_analize, compactness=30, n_segments=200)
outl = color.lab2rgb(img_segments, imgage_to_analize, kind='avg')

segmentation_graph = graph.rag_mean_color(imgage_to_analize, img_segments, mode = 'similarity')
img_cuts = graph.cut_normalized(img_segments, segmentation_graph)
normalized_cut_segments = color.label2rgb(img_cuts, imgage_to_analize, kind='avg')

io.imshow(outl)
io.show()