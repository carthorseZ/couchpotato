pip install -r requirements.txt

git clone https://github.com/carthorseZ/couchpotato.git
chmod 777 -R .
git config core.sharedRepository group

python3 -m flask run --host=0.0.0.0 --port=80

sudo mariadb

create database cp; create user cp@localhost identified by 'cp'; grant all on cp.* to cp@localhost;

Maybe requried
cd app
git clone https://github.com/Seeed-Studio/grove.py
pip install .
