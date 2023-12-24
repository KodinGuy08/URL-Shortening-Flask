from flask import Flask, render_template
import time
import threading

from flask import Flask, request, redirect
import string
import random

app = Flask(__name__, static_url_path='/')

url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

@app.route('/')
def index():
    return render_template('index.html', domain=request.host_url, shortened_url=None)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')

    if not original_url:
        return render_template('index.html', domain=request.host_url, shortened_url=None, error='Please provide a URL to shorten.')

    short_code = generate_short_code()
    short_url = f'{request.host_url}{short_code}'

    url_mapping[short_code] = original_url

    return render_template('index.html', domain=request.host_url, shortened_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = url_mapping.get(short_code)

    if original_url:
        return redirect(original_url)
    else:
        return render_template('index.html', domain=request.host_url, shortened_url=None, error='Shortened URL not found.')

def thread_webAPP():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

t_webApp = threading.Thread(name='Web App', target=thread_webAPP)
t_webApp.setDaemon(True)
t_webApp.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    exit(0)

