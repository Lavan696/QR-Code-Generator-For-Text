📷 QR Code Generator using Python
This is a simple QR Code Generator built using Python and the qrcode library. It allows users to generate a QR code for any custom text or URL input and saves the result as an image file.

🛠️ Features
Generate QR codes for any text, URL, or string input

Saves the output as a .png image (output.png)

Customizable settings like version, size, and error correction

Easy-to-use command-line interface

💡 How It Works
The program greets the user and prompts them to enter the text or link.

A QR code is generated using the qrcode library with predefined settings.

The generated QR code is saved as output.png in the same directory.

✅ Example Run

Hello user. Welcome to QR Code Generator for Text.
Enter the text for which you want to generate QR Code:
http://google.com
The program will generate a QR code image pointing to your GitHub profile and save it as output.png.

🧰 Requirements
Python 3.x

qrcode

Pillow (automatically installed as a dependency)

Install with:


pip install qrcode[pil]
🖼 Output
The generated image looks like a standard black-and-white QR code and can be scanned using any mobile QR code scanner.

🔒 Notes
The QR code version, box size, and border size can be adjusted in the code if needed.

By default, the image is saved as output.png, but you can easily modify the file name.

