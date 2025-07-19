Berikut panduan sederhana untuk **menginstall dependensi dari `requirements.txt`** baik di **Linux** maupun **Windows**, setelah kamu clone repo:

---

## ✅ Langkah Umum (Linux & Windows)

1. **Clone repositori**

   ```bash
   git clone <url-repo>
   cd <nama-repo>
   ```

2. **Buat virtual environment**

   * **Linux/macOS:**

     ```bash
     python3 -m venv .venv
     ```
   * **Windows:**

     ```powershell
     py -m venv .venv
     ```

   Perintah ini membuat folder `.venv/` berisi interpreter Python dan pip khusus proyekmu ([frankcorso.dev][1], [Python Packaging][2]).

3. **Aktifkan `.venv`**

   * **Linux/macOS:**

     ```bash
     source .venv/bin/activate
     ```
   * **Windows (PowerShell atau CMD):**

     ```powershell
     .venv\Scripts\activate
     ```

   Setelah ini, pip dan python yang digunakan adalah dari `.venv` ([Python Packaging][2]).

4. **Perbarui pip (opsional tapi disarankan)**

   ```bash
   python -m pip install --upgrade pip
   ```

   atau

   ```powershell
   py -m pip install --upgrade pip
   ```

   Ini memastikan kamu mendapat versi pip terbaru ([Python Packaging][2]).

5. **Install paket dari `requirements.txt`**

   ```bash
   pip install -r requirements.txt
   ```

   Flag `-r` (atau `--requirement`) membuat pip membaca dan menginstall semua paket yang tercantum di file ([Stack Overflow][3]).

6. **Verifikasi instalasi (opsional)**

   ```bash
   pip freeze
   ```

   Seharusnya tampil sama persis dengan isi `requirements.txt` ([frankcorso.dev][1], [Stack Overflow][3]).

7. **Keluar dari environment (setelah selesai bekerja)**

   ```bash
   deactivate
   ```

   atau tinggal tutup terminalnya ([Python Packaging][2]).

---

## 🎥 Video Demonstrasi

Video ini menunjukkan seluruh proses setup di Linux dan Windows:

[How to Create and Pip Install Requirements.txt in Python (setup venv + install)](https://www.youtube.com/watch?v=h8bt4RvE7zM&utm_source=chatgpt.com)

---

## 📋 Ringkasan Tabel

| OS      | Langkah                         | Perintah                                                   |
| ------- | ------------------------------- | ---------------------------------------------------------- |
| Semua   | Clone repo & masuk folder       | `git clone …` → `cd …`                                     |
| Linux   | Buat venv                       | `python3 -m venv .venv`                                    |
| Windows | Buat venv                       | `py -m venv .venv`                                         |
| Linux   | Aktifkan venv                   | `source .venv/bin/activate`                                |
| Windows | Aktifkan venv                   | `.venv\Scripts\activate`                                   |
| Semua   | Perbarui pip (opsional)         | `python -m pip install --upgrade pip` (atau `py -m pip …`) |
| Semua   | Install dependencies            | `pip install -r requirements.txt`                          |
| Semua   | Verifikasi instalasi (opsional) | `pip freeze`                                               |
| Semua   | Nonaktifkan environment         | `deactivate`                                               |

---

## 💡 Tips Tambahan

* Di Linux, jika `venv` belum terpasang, jalankan:

  ```bash
  sudo apt-get install python3-venv
  ```
* Pastikan file `requirements.txt` ada di direktori proyek, bukan di dalam `.venv/` ([Stack Overflow][4], [Reddit][5], [Python Packaging][2]).
* Jangan gunakan `pip install --user` dalam konteks venv — itu hanya untuk instalasi global berdasarkan user ([Blog | iamluminousmen][6]).



[1]: https://frankcorso.dev/setting-up-python-environment-venv-requirements.html?utm_source=chatgpt.com "Setting Up Your Python Environment With Venv ... - Frank's Blog"
[2]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/?utm_source=chatgpt.com "Install packages in a virtual environment using pip and venv"
[3]: https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from?utm_source=chatgpt.com "python - How can I install packages using pip according to ..."
[4]: https://stackoverflow.com/questions/46375742/difference-between-installing-by-pip-and-installing-globally?utm_source=chatgpt.com "Difference between installing by pip and installing globally"
[5]: https://www.reddit.com/r/PythonLearning/comments/1d57qpu/where_to_make_requirementstxt_for_virtual/?utm_source=chatgpt.com "Where to make requirements.txt for virtual environments?"
[6]: https://luminousmen.com/post/why-use-pip-install-user/?utm_source=chatgpt.com "Why Use `pip install --user`?"
