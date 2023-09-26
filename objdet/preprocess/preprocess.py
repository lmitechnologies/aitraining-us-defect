import os
import cv2
import sys
sys.path.append('/home/yijun1121/LMI_AI_Solutions/lmi_utils')
import glob 

from image_utils.img_stretch import stretch

path_data = './data/manual-upload/intensity'
path_out = './data/unwarp/intensity'

if not os.path.exists(path_out):
    os.makedirs(path_out)

files = glob.glob(os.path.join(path_data,'*.png'))
for p in files:
    fname = os.path.basename(p)
    im = cv2.imread(p)
    im_out = stretch(im, 0.67)
    cv2.imwrite(os.path.join(path_out,fname), im_out)
    