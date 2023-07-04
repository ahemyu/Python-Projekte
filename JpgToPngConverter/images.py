from PIL import Image, ImageFilter

img = Image.open("astro.jpg")
#filtered_img = img.filter(ImageFilter.DETAIL)
img.thumbnail((400, 400))
img.save("thumbnail.jpg", "jpeg")
img.show()

