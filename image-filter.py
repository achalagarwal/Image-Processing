import cv2
import numpy as np
import sys
sys.setrecursionlimit(150000000)
imgOriginal = cv2.imread("asd.jpg")
sizeRow = imgOriginal
imageNew = np.zeros(imgOriginal.shape)
print (imgOriginal.shape)
img=np.empty([100,100])
visited = np.empty([100,100])
segment = np.empty([100,100])
i = 0
seg=1
pixels = np.zeros(100000000)
a=100
b =100
while (i<100):
    j=0
    while (j<100):
        visited[i][j]=0
        j+=1
    i+=1
def rec(row,col,seg2):
    global seg
    #print("[",row,",",col,"]")
    if visited[row][col]==1:
        print("return1")
        return
    visited[row][col]=1
    if img[row][col]<10:
        segment[row][col]=-1
        print("return2")
        return
    segment[row][col]= seg
    pixels[seg]+=1
    if row>0:
        if visited[row-1][col]==0:
            print("calling -> [" , row-1 ,",",col,"]")
            rec(row-1,col,seg)
        if col>0:
            if visited[row-1][col-1]==0:
                print("calling -> [" , row-1 ,",",col-1,"]")
                rec(row-1,col-1,seg)
        if col<(b-1):
            if visited[row-1][col+1]==0:
                print("calling -> [" ,row-1 ,",",col+1,"]")
                rec(row-1,col+1,seg)
    if col>0:
        if visited[row][col-1]==0:
            print("calling -> [", row ,",",col-1,"]")
            rec(row, col-1,seg)
    if col<(b-1):
        if visited[row][col+1]==0:
            print("calling -> [" , row ,",",col+1,"]")
            rec(row, col+1,seg)
    if row<(a-1):
        if visited[row+1][col]==0:
            print("calling -> [", row+1 ,",",col,"]")
            rec(row+1,col,seg)
        if col>0:
            if visited[row+1][col-1]==0:
                print("calling -> [" , row+1 ,",",col-1,"]")
                rec(row+1,col-1,seg)
        if col<(b-1):
            if visited[row+1][col+1]==0:
                print("calling -> [" , row+1 ,",",col+1,"]")
                rec(row+1,col+1,seg)
    print("broken out of segment", seg)
    return 1

imgFinal = np.zeros([imgOriginal.shape[0],imgOriginal.shape[1]])
k = 0
while k<imgOriginal.shape[0]:
    l = 0
    while l<imgOriginal.shape[1]:
        window = cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
        img= window[k:k+100,l:l+100]
        print("k is ",k, " and l is ",l)
        i = 0
        pixels[0]=-1
        pixels[seg]=0
        print("this is " ,i)
        print(j)
        print(img.shape)
        while i<img.shape[0]:
            j=0
            while j<img.shape[1]:
                x = rec(i,j,seg)
                if x == 1:
                    print("Success")
                    seg+=1
                j+=1
            i+=1
        #print("Outside recursive while")
        i =0
        while (i<100):
            j=0
            while (j<100):
                visited[i][j]=0
                j+=1
            i+=1
        i = 0
        while i<100:
            j = 0
            while j<100:
                if segment[i][j]!=-1:
                    print(int(segment[i][j]))
                    if pixels[int(segment[i][j])]>1000:
                        imgFinal[i+k][j+l]= img[i][j]
                j+=1
            i+=1
        i=0
        print("l jumps by 100")
        l+=100
    k+=100
print("Number of Segments +1 = ",seg)

    #
    #     print("start")
    #     i = 0
    #     while i<img.shape[0]:
    #         j=0
    #         while j<img.shape[1]:
    #             if segment[i][j]!=-1:
    #                 y = int(segment[i][j])
    #                 print(y)
    #                 print (pixels[y])
    #                 if pixels[y]>400:
    #                     imageNew[i][j]=img[i][j]
    #             j+=1
    #         i+=1
    #     l+=100
    # k+=100

cv2.imwrite("hi"+".jpg",imgFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()
