from PIL import Image
import sys

# ASCII characters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Resize image according to a new width
def resize_image(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = old_height/float(old_width)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    ascii_str_len = len(ascii_str)
    ascii_img=""
    
    # Split the string based on width of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    # Print the result to the screen
    print(ascii_img)

    # Save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

# Run the program
main(sys.argv[1], new_width=100)
