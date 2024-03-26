from concurrent.futures import ThreadPoolExecutor
from PIL import ImageDraw, ImageFont, Image
import datetime
import asyncio

class ImageProcess:
    def __init__(self) -> None:
        self.__image = Image.open("features/screen_1/Screenshot_1.png")
        self.__font1 = ImageFont.truetype("fonts/ds_sbsans_display_semibold.otf", 72)
        self.__font2 = ImageFont.truetype("fonts/ds_sbsans_text_medium.otf", 34)
        self.__font3 = ImageFont.truetype("fonts/arial.ttf", 23)
        self.__draw = ImageDraw.Draw(self.__image)


    def __process(self, msg: str, num: int):
        num = '{:,}'.format(num).replace(',', ' ')
        num = f"{num} \u20bd"

        text_width = self.__draw.textlength(msg, self.__font2)
        num_width = self.__draw.textlength(num, self.__font1)

        # date = datetime.date.today()
        time = datetime.datetime.now()

        self.__draw.text((self.__image.width/2 - num_width/2, 795), num, font=self.__font1, fill=(0, 0, 0, 255))
        self.__draw.text((self.__image.width/2 - text_width/2, 950), msg, font=self.__font2, fill=(115, 115, 115, 255))
        self.__draw.text((33, 27.5), time.strftime("%H:%M"), font=self.__font3, fill=(50, 52, 55, 255))

        print(time.strftime("%H:%M"))
        # self.image.show()
        self.__image.save("features/screen_1/output.png")
        # print('{:,}'.format(5000).replace(',', ' '))


    async def process_image(self, msg: str, num: int):
        loop = asyncio.get_event_loop()
        print("Processing...")
        # await asyncio.sleep(3.0)
        await loop.run_in_executor(ThreadPoolExecutor(), self.__process, msg, num)

# process = ImageProcess()
# asyncio.run(process.process_image("Бахтиер Нурболович У.", 228000))