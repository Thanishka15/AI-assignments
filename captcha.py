from captcha.image import ImageCaptcha 
import random 
import string 

def generate_captcha_test(length=5):
    return ''.join(random.choices(string.ascii_uppercase+string.digits, k=length))

def create_captcha():
    image = ImageCaptcha()
    captcha_test = generate_captcha_test()
    image.write(captcha_test, 'captcha.png')
    return captcha_test

def verify_captcha():
    correct_text = create_captcha()
    print("CAPTCHA image saved as captcha.png")

    user_input = input("Enter CAPTCHA: ")

    if user_input == correct_text:
        print("Access granted")
    else:
        print("Acess denied!")

verify_captcha()