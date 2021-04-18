import numpy as np
import cv2


def image_reader(image_path,image_name):
  img = cv2.imread(image_path,0)
  cv2.imshow(image_name,img)
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
      cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
      cv2.imwrite(image_name,img)
      cv2.destroyAllWindows()