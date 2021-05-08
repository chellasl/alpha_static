from PIL import Image

img = Image.open(input())

print(img.format)
print(img.mode)
print(img.size)

img.show()