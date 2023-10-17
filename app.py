import io

import numpy as np
import requests
import tflite_runtime.interpreter as tflite

from PIL import Image

# model_file = 'best_model.h5'
# model_file = 'dino_dragon_10_0.899.h5'
interpreter = tflite.Interpreter(model_path='dino_dragon.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


# Define a function to preprocess the image for prediction
def preprocess_image(image, target_size=(150, 150)):
    img = Image.open(image)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Crop image to square
    # width, height = img.size
    # if width > height:
    #     left = (width - height) / 2
    #     top = 0
    #     right = left + height
    #     bottom = height
    # else:
    #     left = 0
    #     top = (height - width) / 2
    #     right = width
    #     bottom = top + width
    #
    # # Crop the image to the calculated coordinates
    # img = img.crop((left, top, right, bottom))

    # resize image
    img = img.resize(target_size, Image.NEAREST)
    img_arr = np.array(img) / 255.0  # Normalize pixel values to [0, 1]
    return img_arr


def classify_image(image_url):

    # download image
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "}
    response = requests.get(image_url, headers=headers, timeout=10)
    response.raise_for_status()
    image = response.content

    # preprocess image
    processed_image = preprocess_image(io.BytesIO(image))

    # one more adjustment
    X = np.float32(np.array([processed_image]))


    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    # Assuming 0 represents "dinosaur" and 1 represents "dragon"
    pred_val = preds[0][0]
    result = {"class": "dinosaur" if pred_val < 0.5 else "dragon", "confidence": float(pred_val)}

    return result
