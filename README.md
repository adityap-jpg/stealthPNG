StealthPNG: LSB Steganography Tool
Inspired by the real-world tactics used in the 2010 "Illegals Program" spy case, StealthPNG is a Python utility that hides and extracts secret text within PNG images. Unlike standard encryption, this tool achieves covertness by making the data statistically invisible to the human eye.

🛠️ How it Works
The tool uses Least Significant Bit (LSB) manipulation. Every pixel in a PNG consists of Red, Green, and Blue channels (0–255). By altering the last bit of a color value:

Bitwise Masking: We use & 0xFE to clear the existing LSB.

Bitwise Insertion: We use | bit to inject our secret data.

A change from value 255 to 254 represents only a 0.39% shift in brightness, making the modification undetectable without digital analysis.

🚀 Features
Memory-Safe Processing: Uses the Pillow library to handle PNG compression by manipulating raw pixel data in RAM.

Multi-Channel Storage: Encodes 3 bits per pixel (1 per RGB channel).

Auto-Termination: Uses a Null Terminator (\0) to signal the end of a message during decoding.

💻 Quick Start
Installation
Bash
pip install Pillow
Usage
Python
from steg_tool import hide_secret_png, reveal_secret_png

# Hide a message
hide_secret_png("input.png", "The Eagle has landed.", "secret_output.png")

# Extract a message
message = reveal_secret_png("secret_output.png")
print(f"Hidden Message: {message}")


🔍 Educational Purpose
This project was developed to explore Digital Forensics and Network Security, specifically focusing on how Steganography can bypass Data Loss Prevention (DLP) systems and be used for covert Command & Control (C2) communication.
