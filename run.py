import os
import subprocess

# Jalankan scrape.py untuk melakukan scraping
subprocess.run(["python", "scrape.py"])

# Jalankan aplikasi Flask
os.system("python app.py")