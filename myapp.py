    from flask import Flask, render_template
    import sqlite3
    from waitress import serve

    app = Flask(__name__)

    @app.route('/')
    def index():
        try:
            conn = sqlite3.connect('data1.db')
            conn.row_factory = sqlite3.Row
            c = conn.cursor()

            c.execute("SELECT * FROM data ORDER BY id DESC")
            data = c.fetchall()

            conn.close()

            return render_template('index.html', data=data)
        except sqlite3.Error as e:
            return f"Error: {e}", 500

    if __name__ == '__main__':
        app.run( host='0.0.0.0', port=5000)