import cv2
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QPixmap
import sys
import numpy as np

VINTAGE_COLOR_LEVELS = {
    'r': np.array(
        [0, 0, 0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12,
         12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 47, 48, 49, 52, 54, 55, 57, 59, 60, 62, 65, 67, 69,
         70, 72, 74, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 99, 101, 103, 107, 109, 111, 112, 116, 118, 120, 124, 126,
         127, 129, 133, 135, 136, 140, 142, 143, 145, 149, 150, 152, 155, 157, 159, 162, 163, 165, 167, 170, 171, 173,
         176, 177, 178, 180, 183, 184, 185, 188, 189, 190, 192, 194, 195, 196, 198, 200, 201, 202, 203, 204, 206, 207,
         208, 209, 211, 212, 213, 214, 215, 216, 218, 219, 219, 220, 221, 222, 223, 224, 225, 226, 227, 227, 228, 229,
         229, 230, 231, 232, 232, 233, 234, 234, 235, 236, 236, 237, 238, 238, 239, 239, 240, 241, 241, 242, 242, 243,
         244, 244, 245, 245, 245, 246, 247, 247, 248, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 254,
         254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
         255, 255, 255, 255, 255, 255, 255, 255]),
    'g': np.array(
        [0, 0, 1, 2, 2, 3, 5, 5, 6, 7, 8, 8, 10, 11, 11, 12, 13, 15, 15, 16, 17, 18, 18, 19, 21, 22, 22, 23, 24, 26, 26,
         27, 28, 29, 31, 31, 32, 33, 34, 35, 35, 37, 38, 39, 40, 41, 43, 44, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 56,
         57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 88, 89,
         90, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 105, 106, 107, 108, 109, 111, 113, 114, 115, 117, 118, 119,
         120, 122, 123, 124, 126, 127, 128, 129, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 144, 145, 146, 148,
         149, 150, 151, 153, 154, 155, 157, 158, 159, 160, 162, 163, 164, 166, 167, 168, 169, 171, 172, 173, 174, 175,
         176, 177, 178, 179, 181, 182, 183, 184, 186, 186, 187, 188, 189, 190, 192, 193, 194, 195, 195, 196, 197, 199,
         200, 201, 202, 202, 203, 204, 205, 206, 207, 208, 208, 209, 210, 211, 212, 213, 214, 214, 215, 216, 217, 218,
         219, 219, 220, 221, 222, 223, 223, 224, 225, 226, 226, 227, 228, 228, 229, 230, 231, 232, 232, 232, 233, 234,
         235, 235, 236, 236, 237, 238, 238, 239, 239, 240, 240, 241, 242, 242, 242, 243, 244, 245, 245, 246, 246, 247,
         247, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 255]),
    'b': np.array(
        [53, 53, 53, 54, 54, 54, 55, 55, 55, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 60, 61, 61, 61, 62, 62, 63, 63, 63,
         64, 65, 65, 65, 66, 66, 67, 67, 67, 68, 69, 69, 69, 70, 70, 71, 71, 72, 73, 73, 73, 74, 74, 75, 75, 76, 77, 77,
         78, 78, 79, 79, 80, 81, 81, 82, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 89, 89, 90, 90, 91, 91, 93, 93, 94,
         94, 95, 95, 96, 97, 98, 98, 99, 99, 100, 101, 102, 102, 103, 104, 105, 105, 106, 106, 107, 108, 109, 109, 110,
         111, 111, 112, 113, 114, 114, 115, 116, 117, 117, 118, 119, 119, 121, 121, 122, 122, 123, 124, 125, 126, 126,
         127, 128, 129, 129, 130, 131, 132, 132, 133, 134, 134, 135, 136, 137, 137, 138, 139, 140, 140, 141, 142, 142,
         143, 144, 145, 145, 146, 146, 148, 148, 149, 149, 150, 151, 152, 152, 153, 153, 154, 155, 156, 156, 157, 157,
         158, 159, 160, 160, 161, 161, 162, 162, 163, 164, 164, 165, 165, 166, 166, 167, 168, 168, 169, 169, 170, 170,
         171, 172, 172, 173, 173, 174, 174, 175, 176, 176, 177, 177, 177, 178, 178, 179, 180, 180, 181, 181, 181, 182,
         182, 183, 184, 184, 184, 185, 185, 186, 186, 186, 187, 188, 188, 188, 189, 189, 189, 190, 190, 191, 191, 192,
         192, 193, 193, 193, 194, 194, 194, 195, 196, 196, 196, 197, 197, 197, 198, 199]),
}


def classic_monochrome(image_path, degree=1.5):
    # Charger l'image en niveaux de gris
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image.")

    # Convertir l'image en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer le degré à l'image en niveaux de gris
    gray_image = cv2.convertScaleAbs(gray_image, alpha=degree, beta=0)

    return gray_image





def rainbow_radiance_filter(image_path, power=1.5):
    # Charger l'image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Impossible de lire l'image.")

    # Convertir l'image en float32 pour les calculs
    image_float = image.astype(np.float32) / 255.0

    # Séparer les canaux de couleur (BGR)
    blue, green, red = cv2.split(image_float)

    # Appliquer un renforcement séparé des canaux de couleur
    enhanced_blue = np.power(blue, power)  # Augmenter la valeur pour intensifier la couleur bleue
    enhanced_green = np.power(green, power)  # Augmenter la valeur pour intensifier la couleur verte
    enhanced_red = np.power(red, power)  # Augmenter la valeur pour intensifier la couleur rouge

    # Recombiner les canaux de couleur
    enhanced_image_float = cv2.merge((enhanced_blue, enhanced_green, enhanced_red))

    # Convertir l'image en entier 8 bits
    enhanced_image = (np.clip(enhanced_image_float, 0, 1) * 255).astype(np.uint8)

    return enhanced_image






def create_pencil_sketch(image_path):
    # Convert the image to grayscale
    image = cv2.imread(image_path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_img = cv2.bitwise_not(gray_img)

    # Apply Gaussian blur to the inverted image
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)

    # Blend the grayscale image and blurred image using the Dodge blend mode
    def dodge(front, back):
        result = cv2.divide(front, 255 - back, scale=256)
        return result

    final_img = dodge(gray_img, blurred_img)

    # Save the intermediate pencil sketch image to a temporary file
    temp_path = "temp_sketch.jpg"
    cv2.imwrite(temp_path, final_img)

    # Apply the rainbow radiance filter to the temporary file
    image = rainbow_radiance_filter(temp_path, 5)

    # Load the final image back from the temporary file
    final_img = image

    # Remove the temporary file

    return final_img






def apply_vintage_filter(image_path, noise_level=20, color_map=VINTAGE_COLOR_LEVELS):
    def vintage_colors(im, color_map):
        r_channel, g_channel, b_channel = cv2.split(im)
        r_channel = cv2.LUT(r_channel, color_map['r'])
        g_channel = cv2.LUT(g_channel, color_map['g'])
        b_channel = cv2.LUT(b_channel, color_map['b'])
        return cv2.merge((r_channel, g_channel, b_channel))

    def add_noise(im, noise_level):
        noise = np.random.randint(-noise_level // 2, noise_level // 2 + 1, size=im.shape).astype(np.int16)
        noisy_image = cv2.add(im.astype(np.int16), noise)
        return np.clip(noisy_image, 0, 255).astype(np.uint8)

    image = cv2.imread(image_path)
    image = vintage_colors(image, color_map)
    image = add_noise(image, noise_level)
    return image




def apply_light_leak(image_path, light_leak_path="red2.jpg", intensity=0.4):
    # Load the original image
    original_image = apply_vintage_filter(image_path)
    if original_image is None:
        raise ValueError("Error loading image. Check the file path.")

    # Load the light leak image
    light_leak_image = cv2.imread(light_leak_path, cv2.IMREAD_UNCHANGED)
    if light_leak_image is None:
        raise ValueError("Error loading light leak image. Check the file path.")

    # Resize the light leak image to match the dimensions of the original image
    light_leak_image = cv2.resize(light_leak_image, (original_image.shape[1], original_image.shape[0]))

    # Blend the images using the Screen blending mode
    blended_image = cv2.addWeighted(original_image, 1 - intensity, light_leak_image, intensity, 0)

    return blended_image


def apply_vignette_filter(image_path):
    image=cv2.imread(image_path)
    height, width = image.shape[:2]
    mask = np.zeros_like(image)

    # Create a black image with a white circle in the center
    cv2.circle(mask, (width // 2, height // 2), min(width, height) // 2, (255, 255, 255), -1)

    # Apply a Gaussian blur to the mask to create the vignette effect
    mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=25, sigmaY=25)

    # Convert the mask to float32 for multiplication
    mask = mask.astype(np.float32) / 255.0

    # Multiply the image with the mask to apply the vignette effect
    result = cv2.multiply(image.astype(np.float32), mask)

    return result.astype(np.uint8)



def dot_pixel_effect(image_path, dot_size=1):   #dot max 15
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return None

    height, width = image.shape[:2]
    dot_image = np.zeros_like(image)

    for y in range(0, height, dot_size):
        for x in range(0, width, dot_size):
            roi = image[y:y+dot_size, x:x+dot_size]
            mean_color = cv2.mean(roi)[:3]
            cv2.circle(dot_image, (x+dot_size//2, y+dot_size//2), dot_size//2, mean_color, -1)

    return dot_image


