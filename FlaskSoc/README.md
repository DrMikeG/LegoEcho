http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/

https://www.python.org/downloads/release/python-2716/


Install python (comes with pip)

pip install virtualenv 

pip install virtualenvwrapper-win

mkvirtualenv FlaskSoc

mkdir FlaskSoc
cd FlaskSoc
setprojectdir .


deactivate to leave

workon FlaskSoc (from anywhere)


pip install flask

run with 
python hello.py

adding sockets

pip install flask-socketio eventlet

Setting this up on trackRC
ssh pi@trackrc.local / trackRC

Python and Pip were already installed.
Installed 
pip install virtualenv 
pip install virtualenvwrapper
Edited .bashrc


You can make a list of installed packages inside the virtualenv:

    $ pip freeze > requirements.txt
    
And install them on the destination virtualenv using:

    $ pip install -r requirements.txt


Run tests with \LegoEcho\FlaskSoc> python -m unittest discover