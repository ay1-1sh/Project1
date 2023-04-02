from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def Future():
    return render_template('demo.html')


@app.route('/ayush')
def hello_world1():
    return render_template('Mistakes.html')

@app.route('/web')
def sourcecode():
    return render_template('Info.html')


if __name__ == '__main__':
    app.run()
