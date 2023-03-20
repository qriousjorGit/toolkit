import qrcode

def get_data(last_name="", first_name="", mobile="", email=""):
    vcard = f"BEGIN:VCARD\nVERSION:4.0\nN:{last_name};{first_name};;;\nTEL;type=MOBILE:{mobile}\nEMAIL:{email}\nEND:VCARD"
    return vcard

# print(get_data("Wong, Robin, 12343123, rwong@gmail.com"))

def gen_QR(vcard):
    img = qrcode.make(vcard)
    type(img)  # qrcode.image.pil.PilImage
    img.save("static/some_file.png")

test = "BEGIN:VCARD\nVERSION:4.0\nN:BONG;KAL;;;\nTEL;type=MOBILE:12321\nEMAIL:BON@AOL.COM\nEND:VCARD"

gen_QR(test)