import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
print("Hello user. Welcome to QR Code Generator for Text.")
print("Enter the text for which you want to generate QR Code : ")
input_text = input()
qr.add_data(input_text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("output.png")