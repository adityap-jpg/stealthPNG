from PIL import Image
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

def string_to_bits(message):
    message += '\0'
    bits = []
    for char in message:
        bits.extend([int(b) for b in format(ord(char), '08b')])
    return bits

def bits_to_string(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char_code = int("".join(map(str, byte)), 2)
        if char_code == 0:
            break
        chars.append(chr(char_code))
    return "".join(chars)

def hide_secret_png(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    
    # Updated to avoid DeprecationWarning
    pixels = list(img.getdata()) 
    bits = string_to_bits(message)
    
    if len(bits) > len(pixels) * 3:
        raise ValueError("Message too large!")

    new_pixels = []
    bit_index = 0
    
    for pixel in pixels:
        r, g, b = pixel
        channels = [r, g, b]
        for i in range(3):
            if bit_index < len(bits):
                channels[i] = (channels[i] & 0xFE) | bits[bit_index]
                bit_index += 1
        new_pixels.append(tuple(channels))

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path, "PNG")

def reveal_secret_png(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    extracted_bits = []
    
    for pixel in pixels:
        for channel in pixel:
            extracted_bits.append(channel & 1)

    return bits_to_string(extracted_bits)

if __name__ == "__main__":
    # Ensure input.png exists in your folder
    hide_secret_png("normal_img.png", "The Eagle has landed.", "secret.png")
    print(reveal_secret_png("secret.png"))