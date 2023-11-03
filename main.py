from PIL import Image, ImageDraw, ImageFont
import os
templates = os.listdir("шаблоны")



print("Генератор мемов запущен!")

print("Список шаблонов: ")


for template in templates:
    print(templates.index(template), template)

memIndex = int(input("Введите номер шаблона: "))
top_text = ""
bottom_text = ""
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
if text_type == 1:
    bottom_text = input("Введите нижний текст: ")
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print("Неверный ввод!!")
    quit()
print(top_text , bottom_text)


image = Image.open("шаблоны/" + templates[memIndex])
w, h = image.size
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("impact.ttf", size = 70)

bbox_top = draw.textbbox((0,0), top_text, font=font)
bbox_bot = draw.textbbox((0,0), bottom_text, font=font)

draw.text(((w - bbox_top[2]) // 2, 0), top_text, font=font, stroke_fill="black", stroke_width=4)
draw.text(((w - bbox_bot[2]) // 2, h - bbox_bot[3] - 10), bottom_text, font=font, stroke_fill="black", stroke_width=4)

image.save("meme.png")
