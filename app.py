import os
import pytesseract
import base64

from PIL import Image
from flask import Flask
from flask import json
from flask import request
from io import BytesIO

app = Flask(__name__)

@app.route('/images', methods = ['POST'])
def get_image_content():
  json_data = json.loads(json.dumps(request.json))
  
  image = base64.b64decode(json_data["image_base_64"])
  image_file = BytesIO(image)
  image_file.seek(0)

  return pytesseract.image_to_string(Image.open(image_file), lang='ukr')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
