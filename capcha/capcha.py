from captcha.image import ImageCaptcha
import random


def capcha_bot():

    image = ImageCaptcha(fonts=['/home/staks/PycharmProjects/bot_bot/capcha/appetite-italic.ttf',
                                '/home/staks/PycharmProjects/bot_bot/capcha/cd2f1-36d91_sunday.ttf'])

    number_random = random.randint(100000, 999999)
    image.generate(str(number_random))
    image_generator = image.write(str(number_random), 'out.png')
    return image_generator



if __name__ == "__main__":
    capcha_bot()
