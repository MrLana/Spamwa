# Spamwa

Langkah Persiapan di Termux

Instal paket yang diperlukan:

     pkg update && pkg upgrade
     pkg install python git
     pip install selenium pillow

Instal browser dan driver:

    pkg install chromium
    git clone https://github.com/mozilla/geckodriver.git
    cd geckodriver
    make
    cp geckodriver $PREFIX/bin/
