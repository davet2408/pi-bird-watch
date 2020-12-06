from flask import Flask, render_template, Response
app = Flask(__name__)

camera = None


@app.route('/')
def home_page():
    return render_template('index.html', camera=camera)


@app.route('/video_feed')
def video_feed():
    return Response()


if __name__ == '__main__':
    app.run()
