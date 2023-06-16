from flask import Flask, request, send_file
import subprocess
import os
import sys

from flask_cors import CORS,cross_origin


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": ["*"]}})

@app.route('/predictCustom', methods=['POST'])
@cross_origin()  
def predictCustom():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    extension = file.filename.split(".")[-1]
    cache = 'cache'
    weights="best.pt"
    detectorScript ="detect.py"
    cacheAbsolutePath = os.path.join(os.getcwd(),cache)
    if not os.path.exists(cacheAbsolutePath):
        os.makedirs(cacheAbsolutePath)
    detectPath = os.path.join(cacheAbsolutePath, 'detect')
    if not os.path.exists(detectPath):
        os.makedirs(detectPath)
    fileName = "2."+extension
    filepath = os.path.join(cacheAbsolutePath, fileName)
    file.save(filepath)
    try:
        python_executable = sys.executable
        subprocess.run([python_executable , detectorScript, '--source', filepath, '--weights', weights, '--conf', '0.25', '--name', 'detect','--exist-ok','--project',cacheAbsolutePath,"--no-trace"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the subprocess: {e}")
    # You can also log the error or handle it in a different way if needed
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    saved_dir = os.path.join(cacheAbsolutePath, 'detect')
    print(os.listdir(saved_dir))
    output_filepath =  os.path.join(saved_dir, fileName) # replace this with actual path and filename

    finalImage= send_file(output_filepath, mimetype='image/gif')
    return finalImage
@app.route('/predictCoco', methods=['POST'])
@cross_origin()  
def predictCoco():
    
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    extension = file.filename.split(".")[-1]
    cache = 'cache'
    weights="yolov7_training.pt"
    detectorScript ="detect.py"
    cacheAbsolutePath = os.path.join(os.getcwd(),cache)
    if not os.path.exists(cacheAbsolutePath):
        os.makedirs(cacheAbsolutePath)
    detectPath = os.path.join(cacheAbsolutePath, 'detect')
    if not os.path.exists(detectPath):
        os.makedirs(detectPath)
    fileName = "2."+extension
    filepath = os.path.join(cacheAbsolutePath, fileName)
    file.save(filepath)
    try:
        python_executable = sys.executable
        subprocess.run([python_executable , detectorScript, '--source', filepath, '--weights', weights, '--conf', '0.25', '--name', 'detect','--exist-ok','--project',cacheAbsolutePath,"--no-trace"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the subprocess: {e}")
    # You can also log the error or handle it in a different way if needed
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    saved_dir = os.path.join(cacheAbsolutePath, 'detect')
    print(os.listdir(saved_dir))
    output_filepath =  os.path.join(saved_dir, fileName) # replace this with actual path and filename

    finalImage= send_file(output_filepath, mimetype='image/gif')
    return finalImage


@cross_origin()
@app.route('/home', methods=['GET'])
def home():
    return "Hello World"


# curl -X POST -F "file=@image.jpg" http://localhost:5000/predict > output.png
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
