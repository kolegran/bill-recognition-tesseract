import os
import pytesseract

from PIL import Image
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_bill_content():
	return '<pre>' + pytesseract.image_to_string(Image.open('bill.jpg'), lang='ukr') + '</pre>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
