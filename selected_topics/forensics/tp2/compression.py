import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct

def compress (img, QF1, QF2):
    '''
    compresses the image using DCT transform and Q matrix
    '''
    #this is the quantization matrix
    Q50 = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]], order='F')

    #QF1
    if QF1 > 50:
        QM1 = np.around(Q50*(np.ones(Q50.shape)*((100-QF1)/50)))
        QM1.astype(int)

    elif QF1 < 50:
        QM1 = np.around(Q50*(np.ones(Q50.shape)*(50/QF1)))
        QM1.astype(int)

    elif QF1 == 50:
        QM1 = Q50

    else:
        print("error")

    QM1.astype(float)

    #QF2
    if QF2 > 50:
        QM2 = np.around(Q50*(np.ones(Q50.shape)*((100-QF2)/50)))
        QM2.astype(int)

    elif QF2 < 50:
        QM2 = np.around(Q50*(np.ones(Q50.shape)*(50/QF2)))
        QM2.astype(int)

    elif QF2 == 50:
        QM2 = Q50

    else:
        print("error")

    QM2.astype(float)

    #Set up the DCT values
    dct_domain = np.zeros(img.shape) #should just be same shape
    dct_quantized = np.zeros(img.shape)
    dct_dequantized = np.zeros(img.shape)
    dct_restored = np.zeros(img.shape)
    dct_quantized_coeff = np.zeros((64,(img.shape[0]//8)*(img.shape[1]//8)))

    #subtract the img by 128 to center around the 0
    img = np.copy(img) - (128*np.ones(img.shape))

    #JPEG Encoding
    k = 0
    for i in range(0, img.shape[0], 8): #row 8x8

        for j in range(0, img.shape[1], 8):

            block = img[i:i+8,j:j+8] #set the block
            win1 = dct(block, norm='ortho')
            dct_domain[i:i+8,j:j+8] = win1

            win2 = np.around(win1/QM1)
            dct_quantized[i:i+8,j:j+8] = win2
            dct_quantized_coeff[:,k] = zigzag(win2) #to get the coeff for pairwise
            k += 1

    #JPEG Decoding
    for i in range(0, img.shape[0], 8):

        for j in range(0, img.shape[1], 8):

            win2 = dct_quantized[i:i+8, j:j+8]
            win3 = win2*QM1 #dequantization of DCT coeff
            dct_dequantized[i:i+8, j:j+8] = win3
            win4 = idct(win3, norm='ortho')
            dct_restored[i:i+8, j:j+8] = win4

    #Return the relevant info
    img_recon = np.copy(dct_restored) + (128*np.ones(dct_restored.shape)) #don't forget to uncenter
    globalDCT = np.copy(dct_quantized)
    pairwiseDCT = np.copy(dct_quantized_coeff)

    return img_recon, globalDCT, pairwiseDCT
