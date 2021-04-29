# Exercise 4-02: Extract RGB values from image

from matplotlib import image as img

r = []
g = []
b = []

# Read batman image and print dimensions
batman_image = img.imread('input/batman.jpeg')
print(batman_image.shape)

# Store RGB values of all pixels in lists r, g and b
for row in batman_image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)
