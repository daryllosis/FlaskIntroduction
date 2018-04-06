from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def renderIndex():
    return render_template('index.html')

@app.route('/about')
def renderAbout():
  return render_template('about.html')

@app.route('/projects')
def renderProjects():
  return render_template('projects.html')

if __name__=="__main__":
    app.run(debug=True)   

