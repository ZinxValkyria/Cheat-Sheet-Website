from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    md_file_path = os.path.join(app.root_path, 'cheat_sheets', 'test.md')
    content = read_markdown_file(md_file_path)
    return render_template('index.html', content=content)

def read_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return markdown.markdown(content)

@app.route('/cheat_sheet')
def cheat_sheet():
    return render_template('cheat_sheet.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/python')
def python():
    return render_template('python.html')

# Add routes for other pages as needed

if __name__ == '__main__':
    app.run(debug=True)
