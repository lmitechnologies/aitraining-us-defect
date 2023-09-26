import os
import cv2
import sys
import numpy as np
sys.path.append('/home/yijun1121/LMI_AI_Solutions/lmi_utils')
import glob 

from image_utils.img_stretch import stretch
BLACK = (0,0,0)

def process_p(img_p):
    # empty pixels receive value=0
    # replace empty pixels with min above 0
    minval=img_p[img_p>0].min()
    floor=minval-1
    empty_ind=np.where(img_p==0)
    img_p[empty_ind]=floor
    img_p=img_p-floor
    maxval=img_p.max()
    img_p=(img_p.astype(np.float32)/maxval)*255.0
    img_p=img_p.astype(np.uint8)
    img_p=cv2.applyColorMap(img_p,cv2.COLORMAP_JET)
    img_p[empty_ind]=BLACK
    img_p = img_p[:,:,::-1]
    return img_p

def blend(img_p, img_i):
    # Blend the images
    alpha = 0.3  # Weight for image1
    beta = 0.7  # Weight for image2
    gamma = 0  # Scalar added to each pixel
    blended_image = cv2.addWeighted(img_p, alpha, img_i, beta, gamma)
    return blended_image



path_data = './data/manual-upload'
path_out = './data/blend'

if not os.path.exists(path_out):
    os.makedirs(path_out)

files_i = glob.glob(os.path.join(path_data,'intensity','*.png'))
files_p = glob.glob(os.path.join(path_data,'profile','*.png'))

files_i.sort()
files_p.sort()

for pi,pp in zip(files_i,files_p):
    fname_p = os.path.basename(pp)
    fname_i = os.path.basename(pi)
    
    I_i = cv2.imread(pi,cv2.IMREAD_UNCHANGED)
    intensity = stretch(I_i, 0.67)
    intensity = np.stack([intensity,]*3,axis=2)
    
    I_p = cv2.imread(pp,cv2.IMREAD_UNCHANGED)
    profile = stretch(I_p, 0.67)
    
    profile = process_p(profile)
    
    # blend images
    print(fname_p,fname_i)
    print(profile.shape,intensity.shape)
    blended = blend(profile, intensity)
    cv2.imwrite(os.path.join(path_out,fname_p), blended)
    