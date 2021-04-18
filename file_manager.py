import os

import reader


for root, dirs, files in os.walk("./calibration_images"):
  count = 0
  for name in files:
    file_name = os.path.join(root, name)
    if(file_name.lower().endswith(('.png', '.jpg', '.jpeg'))):
      count += 1
      image_path = os.path.join(root, name)
      image_name = name
      #opencv code generator that gives checkerboard info
      reader.image_reader(image_path ,image_name)



  print(count)


