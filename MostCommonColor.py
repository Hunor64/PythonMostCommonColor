from PIL import Image
import collections

def most_frequent_color(image):
    with Image.open(image) as img:
        pixels = img.load()
        width, height = img.size
        pixels = [pixels[x, y] for x in range(width) for y in range(height)]

        color_counter = collections.Counter(pixels)
        return color_counter.most_common(1)[0][0]

def main():
    image = input("Enter the path of an image file: ")
    if image.startswith('"') and image.endswith('"'):
        image = image[1:-1]
    most_common_color = most_frequent_color(image)
    print("Most common color: #{:02x}{:02x}{:02x}".format(*most_common_color))
    print("RGB: ",most_common_color)
    input("Press any key to exit")

main()
