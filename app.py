from flask import Flask, render_template, send_file, redirect


app = Flask("app")

# root webpage
@app.route('/')
def send_home():
    return redirect('/home')
@app.route('/home')
def home():
    return render_template('index.html')

#pages
@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

# return css
@app.route('/static/styles/style.css')
def css():
    return send_file('./static/styles/style.css') 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")