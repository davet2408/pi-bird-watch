from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return 'video.png'


if __name__ == '__main__':
    app.run()
