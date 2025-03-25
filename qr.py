import qrcode

# URL for the webpage
url = "https://your_actual_link"  # Replace with your actual URL

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Save QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'.")
