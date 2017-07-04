# image-particulate-filter
This program will departiculate a grainy image based on a user chosen pixel threshold

Edit the number in line number ### and change it to the minimum number of pixels that must be there in a cluster

This program breaks the image into 100*100 boxes and hence if you need a minimum cluster size of 'x', then make sure to set
the window size to atleast sqrt(1000*x*x)
