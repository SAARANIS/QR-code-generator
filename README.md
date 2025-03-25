# QR Code Generator

## Overview
**QR Code Generator** is a simple Python project that allows users to generate QR codes for any given URL. The generated QR code is saved as an image file, which can be used for easy access to web pages.

## Features
- Generates **QR codes** from user-defined URLs.
- Saves the QR code as an image (**PNG format**).
- Uses **customizable settings** like error correction, box size, and border.
- Simple and lightweight Python script.

## Technologies Used
- **Python** – Core programming language.
- **qrcode** – Library for generating QR codes.
- **PIL (Pillow)** – For image processing.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/SAARANIS/QR-code-generator.git
   cd QR-Code-Generator
   ```
2. Install dependencies:
   ```sh
   pip install qrcode[pil]
   ```

## Usage
1. Open `qr.py`.
2. Replace `your_actual_link` with your desired URL.
3. Run the script:
   ```sh
   python qr.py
   ```
4. The QR code image (`qrcode.png`) will be generated and saved in the project directory.

## Future Enhancements
- Support for different file formats (JPEG, SVG, etc.).
- QR code customization (colors, logos, styles).
- Web-based QR code generator using Flask or Streamlit.

## Contributors
- **Syed Anis Al Rehaman**

For any inquiries or contributions, feel free to submit a pull request or open an issue.

