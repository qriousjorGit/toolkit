import qrcode


def get_data(last_name="", first_name="", mobile="", email=""):
    vcard = f"BEGIN:VCARD\nVERSION:4.0\nN:{last_name};{first_name};;;\nTEL;type=MOBILE:{mobile}\nEMAIL:{email}\nEND:VCARD"
    return vcard


def gen_QR(vcard):
    img = qrcode.make(vcard)
    type(img)  # qrcode.image.pil.PilImage
    try:
        img.save("static/some_file.png")
    except FileNotFoundError:
        pass


#TODO code for creating a Google calendar event.  Calendar popup?  Function for time coding
    # def get_event(event_data, title="", estart="", eend=""):
    #     event = ""
    #     BEGIN: VEVENT
    #     SUMMARY: Test
    #     DTSTART;
    #     VALUE = DATE:20120124
    #     DTEND;
    #     VALUE = DATE:20120125
    #     END: VEVENT
    #     return event