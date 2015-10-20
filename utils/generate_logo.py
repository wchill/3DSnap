from PIL import Image

img = Image.open('3dsnap.png')
if img.mode == 'RGB':
    pixelSize = 3
else:
    pixelSize = 4

with open('3dsnap.bin', 'wb') as f:
    pixels = img.tobytes()
    for i in range(0, len(pixels), pixelSize):
        f.write(pixels[i])
        f.write(pixels[i+1])
        f.write(pixels[i+2])
