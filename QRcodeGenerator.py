import qrcode

def generate_qrcode(text):
    """Generates a QR code from the given text."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


if __name__ == "__main__":
    generate_qrcode("Madushan B Dissanayake")
