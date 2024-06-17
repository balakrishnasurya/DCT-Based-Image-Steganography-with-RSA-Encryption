from dct import DCT
import cv2
import os

def encode(imagepath, secret):
    dct = DCT()
    original_image_file = imagepath
    dct_img = cv2.imread(original_image_file, cv2.IMREAD_UNCHANGED)
    secret_msg = secret
    print("The message length is: ", len(secret_msg))
    dct_img_encoded = dct.encode_image(dct_img, secret_msg)
    dct_encoded_image_file = "dct_" + os.path.basename(original_image_file)
    encoded_image_path = os.path.join('Encoded_image', dct_encoded_image_file)
    cv2.imwrite(encoded_image_path, dct_img_encoded)
    print("Encoded images were saved!")
    return encoded_image_path