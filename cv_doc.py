from PIL import Image, ImageFont, ImageDraw, ImageEnhance
 
im = Image.new('RGB', (600, 800), 'white')

draw = ImageDraw.Draw(im)

arialFont = ImageFont.truetype('fonts/arial.ttf', 20)

string= "Robin"

size=arialFont.getsize(string)
print(size)
draw.text((100, 150), string , fill=(0,0,0), font=arialFont,align="center")

im.save("dataset/convert.jpg")
