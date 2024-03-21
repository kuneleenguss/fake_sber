from PIL import ImageDraw, ImageFont, Image
import datetime

image = Image.open("Screenshot_1.png")

font1 = ImageFont.truetype("ds_sbsans_display_semibold.otf", 72)
font2 = ImageFont.truetype("ds_sbsans_text_medium.otf", 34)
font3 = ImageFont.truetype("arial.ttf", 23)

draw = ImageDraw.Draw(image)

def process(msg: str, num: int):
    num = '{:,}'.format(num).replace(',', ' ')
    num = f"{num} \u20bd"

    text_width = draw.textlength(msg, font2)
    num_width = draw.textlength(num, font1)

    # date = datetime.date.today()
    time = datetime.datetime.now()

    draw.text((image.width/2 - num_width/2, 795), num, font=font1, fill=(0, 0, 0, 255))
    draw.text((image.width/2 - text_width/2, 950), msg, font=font2, fill=(115, 115, 115, 255))
    draw.text((33, 27.5), time.strftime("%H:%M"), font=font3, fill=(50, 52, 55, 255))


    print(time.strftime("%H:%M"))
    image.show()
    # print('{:,}'.format(5000).replace(',', ' '))

process("Бахтиер Нурболович У.", 100000)