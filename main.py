import numpy as np
import pydicom
from PIL import Image

images = (['I001.dcm', 'I002.dcm', 'I003.dcm'])

print(images[0].split('.'))

for img in images:
    new_file_name = img.split('.')[0]
    # new_file_name += '.jpg'
    print(new_file_name)
    image = pydicom.dcmread(img)
    image = image.pixel_array.astype(float)

    rescaled_image = (np.maximum(image, 0) / image.max()) * 255  # float pixels
    final_image = np.int8(rescaled_image)  # integer pixels
    final_image = Image.fromarray(final_image)
    # final_image.save('ala.jpg')
    final_image.show()




