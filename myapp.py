from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Fetch the data from the database
    c.execute("SELECT * FROM data ORDER BY id DESC")
    data = c.fetchall()

    # Close the connection
    conn.close()

    # Render the template with the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)