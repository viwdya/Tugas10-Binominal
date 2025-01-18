from flask import Flask, render_template, request
from math import comb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Mengambil input dari form
            n = int(request.form['n'])  # Jumlah mahasiswa yang mendaftar
            p = float(request.form['p']) / 100  # Peluang diterima per mahasiswa, dibagi 100
            k = int(request.form['k'])  # Jumlah mahasiswa yang diharapkan diterima

            # Validasi input
            if not (0 <= p <= 1):
                result = "Peluang (p) harus berada di antara 0 dan 100."
            elif not (0 <= k <= n):
                result = "Jumlah mahasiswa diterima (k) harus antara 0 dan jumlah pendaftar (n)."
            else:
                # Menghitung probabilitas binomial dan mengonversi ke persentase
                result = f"{calculate_binomial_probability(n, p, k) * 100:.2f}%"
        except ValueError:
            result = "Input tidak valid. Harap masukkan angka yang benar."

    return render_template('index.html', result=result)

def calculate_binomial_probability(n, p, k):
    """
    Fungsi untuk menghitung probabilitas distribusi binomial.
    Rumus: P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
    """
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
