
import qrcode


def qr_code_generator():
    url_data = input("Enter the URL to encode: ").strip()

    filename = input("Enter the filename to be save: ").strip()


    qr = qrcode.QRCode(version=1,box_size=10, border=4)

    qr.add_data(url_data)
    qr.make(fit=True)

    image_generated = qr.make_image(fill_color='white', back_color='purple')

    print(image_generated)

    image_generated.save(filename)
    print(f"QR code generated and saved as {filename}.")



qr_code_generator()