from PIL import Image, ImageDraw, ImageFont

def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size

    overlay = Image.new('RGBA', input_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (255, 255, 255, 30)
    
    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i - height, height)], fill=watermark_color_pattern, width=5)

    font_size = 80
    font = ImageFont.truetype('arial.ttf', font_size)

    # Getting text size without drawing it
    text_width, text_height = draw.textsize(watermark_text, font=font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)

    draw.text((x, y), watermark_text, fill=watermark_color_text, font=font)

    watermarked_image = Image.alpha_composite(input_image, overlay)

    watermarked_image.save(output_image_path)

input_image_path = 'natural_image.jpg'
output_image_path = 'output_image.png'
watermark_text = "watermarking.com"

add_watermark_overlay(input_image_path, output_image_path, watermark_text)

