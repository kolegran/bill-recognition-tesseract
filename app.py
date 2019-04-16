import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_bill_content():
	cmd = os.popen('tesseract bill.jpg bill -l ukr').read()
	cmd = os.popen('cat bill.txt').read()

	return cmd

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
