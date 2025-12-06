import sqlite3
import string
import random
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from database import get_db_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambiar esto por una clave secreta real

def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        custom_id = request.form.get('custom_id')

        if not url:
            flash('La URL es requerida!')
        else:
            conn = get_db_connection()

            if custom_id:
                existing_url = conn.execute('SELECT id FROM urls WHERE short_id = ?', (custom_id,)).fetchone()
                if existing_url:
                    flash('El código personalizado ya está en uso. Por favor elige otro.')
                    conn.close()
                    return render_template('index.html')
                short_id = custom_id
            else:
                short_id = generate_short_id()
                while conn.execute('SELECT id FROM urls WHERE short_id = ?', (short_id,)).fetchone():
                    short_id = generate_short_id()

            conn.execute('INSERT INTO urls (original_url, short_id) VALUES (?, ?)',
                         (url, short_id))
            conn.commit()
            conn.close()

            short_url = request.host_url + short_id
            return render_template('index.html', short_url=short_url, original_url=url)

    return render_template('index.html')

@app.route('/<short_id>')
def url_redirect(short_id):
    conn = get_db_connection()
    url_data = conn.execute('SELECT original_url, clicks FROM urls WHERE short_id = ?', (short_id,)).fetchone()

    if url_data:
        conn.execute('UPDATE urls SET clicks = ? WHERE short_id = ?',
                     (url_data['clicks'] + 1, short_id))
        conn.commit()
        conn.close()
        return redirect(url_data['original_url'])
    else:
        conn.close()
        return abort(404)

@app.route('/stats')
def stats():
    conn = get_db_connection()
    db_urls = conn.execute('SELECT * FROM urls').fetchall()
    conn.close()
    urls = []
    for url in db_urls:
        url = dict(url)
        url['short_url'] = request.host_url + url['short_id']
        urls.append(url)
    return render_template('stats.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
