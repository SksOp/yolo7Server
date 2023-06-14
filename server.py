from flask import Flask, request, send_file
import subprocess
import os
import shutil

app = Flask(__name__)

@app.route('/predictCustom', methods=['POST'])
def predictCustom():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    filepath = os.path.join('cache', file.filename)
    file.save(filepath)
    try:
        subprocess.run(['python', 'detect.py', '--source', filepath, '--weights', 'best.pt', '--conf', '0.25', '--name', 'detect','--exist-ok','--project','cache',"--no-trace"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the subprocess: {e}")
    # You can also log the error or handle it in a different way if needed
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    output_filepath =  os.path.join('cache/detect/', file.filename) # replace this with actual path and filename

    finalImage = send_file(output_filepath, mimetype='image/gif')
    cache_dir = 'cache'
    for filename in os.listdir(cache_dir):
        file_path = os.path.join(cache_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    return finalImage
@app.route('/predictCoco', methods=['POST'])
def predictCoco():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    filepath = os.path.join('cache', file.filename)
    file.save(filepath)
    try:
        subprocess.run(['python', 'detect.py', '--source', filepath, '--weights', 'yolov7_training.pt', '--conf', '0.25', '--name', 'detect','--exist-ok','--project','cache',"--no-trace"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the subprocess: {e}")
    # You can also log the error or handle it in a different way if needed
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    output_filepath =  os.path.join('cache/detect/', file.filename) # replace this with actual path and filename

    finalImage = send_file(output_filepath, mimetype='image/gif')
    cache_dir = 'cache'
    for filename in os.listdir(cache_dir):
        file_path = os.path.join(cache_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    return finalImage

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# @app.after_request
# def cleanup(response):
#     cache_dir = 'cache'
#     for filename in os.listdir(cache_dir):
#         file_path = os.path.join(cache_dir, filename)
#         try:
#             if os.path.isfile(file_path) or os.path.islink(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#         except Exception as e:
#             print('Failed to delete %s. Reason: %s' % (file_path, e))
#     return response


# curl -X POST -F "file=@image.jpg" http://localhost:5000/predict > output.png
# 