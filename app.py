from flask import Flask, render_template, request, flash, redirect, url_for
import os, sys 

app = Flask(__name__)

# global variables (seriously?)
UPLOAD_FOLDER = None
PASSWORD = None

@app.route("/",methods = ['GET','POST'])
def homepage():
	if request.method == 'GET':	
		return render_template("login.html")
	else:
		if ("password" in request.form) and (request.form["password"] == PASSWORD):
			return render_template("homepage.html")
		else:
			flash("Invalid password!")
			return render_template("login.html")

@app.route("/upload",methods = ['POST'])
def upload():
	count = 0
	for i in xrange(1,6):
		if 'file' + str(i) in request.files:
			file = request.files['file' + str(i)]
			if file.filename != '':
				file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
				count += 1
	flash(str(count) + " files sent! Sign-in to send again...")
	return redirect(url_for('homepage'))


def main():
	port = int(os.environ.get("PORT", 8000))
#	app.debug = True
#	app.secret_key = 'thequickbrownfoxjumpsoverthelazydog'
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.run(host = "0.0.0.0", port = port)

if __name__ == "__main__":
	if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
		UPLOAD_FOLDER = sys.argv[1]
	elif os.environ.get('UPLOAD_FOLDER') != None:
		UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
	else:
		UPLOAD_FOLDER = '.'
	UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)
	if os.environ.get('PASSWORD') != None:
		PASSWORD = os.environ.get('PASSWORD')
	else:
		PASSWORD = "muggle"
	main()
