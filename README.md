# StealthPNG: LSB Steganography Tool

Inspired by the real-world tactics used in the 2010 "Illegals Program" spy case, **StealthPNG** is a Python utility that hides and extracts secret text within PNG images. Unlike standard encryption, which signals the presence of a secret, this tool achieves **covertness** by making the data statistically invisible to the human eye.

## 🛠️ How it Works

The tool utilizes **Least Significant Bit (LSB)** manipulation. Every pixel in a PNG consists of Red, Green, and Blue channels (valued 0–255). By altering the last bit of a color value, we can encode data without altering the visual appearance of the image.

### Pixel-Level Manipulation
PNG files use DEFLATE compression. Direct file manipulation would corrupt the image structure. This tool uses the **Pillow** library to unpack the image into RAM, allowing for safe bitwise operations:

*   **The Mask (`&`)**: We use `& 0xFE` (11111110) to clear the existing LSB, creating a "blank slot."
*   **The Insertion (`|`)**: We use `| bit` to inject our secret binary data (0 or 1) into that slot.
*   **The Processing Loop**: The algorithm iterates through every RGB channel, effectively storing 3 bits of data per pixel.

## 🪓 Practical Example: Hiding "Axe"
To hide the word **"Axe"**, the tool converts the characters into binary:
*   **A** → `01000001` | **x** → `01111000` | **e** → `01100101` | **\0** → `00000000`

Total bits to hide: **32 bits**. This requires 32 color values (approx. 11 pixels). Changing a value from 255 to 254 results in a **0.39%** shift in brightness—insignificant to human biology, but a clear data point for the decoder.

## 🚀 Quick Start

### Prerequisites
*   Python 3.x
*   Pillow Library

### Installation
```bash
pip install Pillow
## Usage

```python
from steg_tool import hide_secret_png, reveal_secret_png

# Encode a message into a PNG
hide_secret_png("input.png", "The Eagle has landed.", "secret_output.png")

# Decode the message from the PNG
message = reveal_secret_png("secret_output.png")
print(f"Decoded Message: {message}")
```
### 🔍 Strategic Significance
In modern cybersecurity, steganography is a critical vector for:

Hidden Malware Communication: Attackers hide commands inside images on public platforms to bypass detection of a malicious "heartbeat."

Bypassing Data Loss Prevention (DLP): Embedding proprietary data inside outbound media traffic to avoid automated text-based scanners.

Digital Attribution: Embedding unique, invisible "fingerprints" to trace the source of leaked documents.

Tamper Detection: Using pixel-level hashes to verify image integrity.

Note: This project is for educational purposes in digital forensics and network security.

