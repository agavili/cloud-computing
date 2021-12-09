import os, subprocess
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #return 'file uploaded successfully'
      
      subprocess.call("rm -f ./a.out", shell=True)
      num_correct = subprocess.call("./ex_sub.sh", shell=True)
      message = "You got " + str(num_correct) + " out of 2 correct!\n"
      print(message)
      with open('subtract.py','r') as fs:
          file_sub = fs.read()
          print(file_sub)
      return render_template('results.html', score=message, file_sub= file_sub)


if __name__ == '__main__':
     app.run(debug = True,host="0.0.0.0")
