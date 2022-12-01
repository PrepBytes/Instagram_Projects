from PIL import Image
img = Image.open("images.jfif")
bw = img.convert("L")
bw.show()
