https://code.visualstudio.com/docs/python/tutorial-flask



pip install -r requirements.txt

cd app
git clone https://github.com/Seeed-Studio/grove.py
cd grove.py
pip install .


git clone https://github.com/carthorseZ/couchpotato.git
chmod 777 -R .
git config core.sharedRepository group

python -m flask run --host=0.0.0.0 --port=80 --debug 
or python3 -m flask run --host=0.0.0.0 --port=80 --debug 

pi
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    flask run --host=0.0.0.0 --port=80

sudo mariadb

create database cp; create user cp@localhost identified by 'cp'; grant all on cp.* to cp@localhost;

Maybe requried

