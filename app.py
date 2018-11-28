from flask import Flask, render_template, request 
import os, sys 

app = Flask(__name__)

UPLOAD_FOLDER = '/home/s4nd33p/Downloads/share-it'

@app.route("/",methods = ['GET','POST'])
def homepage():
	if request.method == 'GET':	
		return render_template("homepage.html")
	else:
		file = request.files['file']
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
		return render_template("homepage.html")

def main():
	port = int(os.environ.get("PORT", 8000))
	# app.debug = True
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.run(host = "0.0.0.0", port = port)

if __name__ == "__main__":
	if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
		UPLOAD_FOLDER = os.path.abspath(sys.argv[1])
	main()
