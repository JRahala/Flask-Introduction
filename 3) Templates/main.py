from flask import Flask, render_template
app = Flask(__name__)

@app.route('/template')
def flexible():
    return render_template('index.html')

@app.route('/no_template')
def hard_coded():
    return '''<!DOCTYPE HTML>

<html>

	<head>
		
	</head>

	<body>

		<h1> Page title </h1>
		<p> Paragraph of information </p>
		<p> Another paragraph </p>

	</body>

</html>'''

if __name__ == '__main__':
    app.run(port = 8080)
