import requests

# data = input("What you want coded?")
# r = requests.get(f"http://api.qrserver.com/v1/create-qr-code/?data={data}&size=100x100")
#
# print(type(r))
#
# img_data = r.content
# with open('image_name.jpg', 'wb') as f:
#     f.write(img_data)

def generate_qr(user_data):
    #returns an image file and NOT a website.  The above code can create the image on HD
    r = requests.get(f"http://api.qrserver.com/v1/create-qr-code/?data={user_data}&size=100x100")
    return r

# test = generate_qr("testing 12321")
# print(type(test))
# print (test.text)

def get_card_data(last_name="", first_name="", mobile="", email=""):
    v_card_template = f"BEGIN:VCARD\nVERSION:4.0\nN:{last_name};{first_name};;;\nTEL;type=MOBILE:{mobile}\nEMAIL:{email}\nEND:VCARD"
    print(v_card_template)

test = get_card_data("kal", "bong", mobile ="23423423")
