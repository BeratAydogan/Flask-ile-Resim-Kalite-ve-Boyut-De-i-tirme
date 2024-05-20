from flask import Flask, render_template, request, redirect
from PIL import Image
import os

app = Flask(__name__)

# Yüklenen fotoğrafın geçici olarak saklanacağı klasör
UPLOAD_FOLDER = 'static/dosyasının/konumu'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def resize_image(input_path, output_path, new_quality, new_width, new_height):
    with Image.open(input_path) as img:
        img.thumbnail((new_width, new_height))


        img.save(output_path,quality=new_quality)

@app.route('/')
def index():
    return render_template('Anasayfa.html')

@app.route('/upload/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Yüklenen fotoğrafı geçici bir klasöre kaydet
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        resolution = request.form.get('PX')
        extent = request.form.get('EX')
        new_quality = 100
        image = Image.open(file)
        width, height =image.size


        if resolution == '1080p':
            new_quality = 90
        elif resolution == '720p':
            new_quality = 70
        elif resolution == '480p':
            new_quality = 30
        elif resolution == '360p':
            new_quality = 10


        if extent == '100':
            new_width = width
            new_height = height
        if extent == '90':
            new_width = int(width * 0.9)
            new_height = int(height * 0.9)
        if extent == '80':
            new_width = int(width * 0.8)
            new_height = int(height * 0.8)
        if extent == '70':
            new_width = int(width * 0.7)
            new_height = int(height * 0.7)
        if extent == '60':
            new_width = int(width * 0.6)
            new_height = int(height * 0.6)
        if extent == '50':
            new_width = int(width * 0.5)
            new_height = int(height * 0.5)
        if extent == '40':
            new_width = int(width * 0.4)
            new_height = int(height * 0.4)
        if extent == '30':
            new_width = int(width * 0.3)
            new_height = int(height * 0.3)
        if extent == '20':
            new_width = int(width * 0.2)
            new_height = int(height * 0.2)
        if extent == '10':
            new_width = int(width * 0.1)
            new_height = int(height * 0.1)





        resized_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resized_' + file.filename)
        resize_image(file_path, resized_path, new_quality,new_width,new_height)

        # Küçültülmüş fotoğrafın yolunu döndür
        return render_template('result.html', original=file.filename, resized='resized_' + file.filename)

if __name__ == '__main__':
    app.run(debug=True)
