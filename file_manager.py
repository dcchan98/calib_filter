import os
for root, dirs, files in os.walk("./calibration_images"):
  count = 0
  for name in files:
    file_name = os.path.join(root, name)
    if(file_name.lower().endswith(('.png', '.jpg', '.jpeg'))):
      count += 1
      print(os.path.join(root, name)) # Replace with opencv code generator that gives checkerboard info
  print(count)


