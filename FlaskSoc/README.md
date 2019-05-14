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