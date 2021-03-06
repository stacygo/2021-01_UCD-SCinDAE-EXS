# Exercise 2-03: The speed of cats

from functions import get_image_from_instagram, timer, process_with_numpy, process_with_pytorch

image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
    print('Numpy version')
    process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
    print('Pytorch version')
    process_with_pytorch(image)
