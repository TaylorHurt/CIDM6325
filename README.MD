# 1. CREATE VIRTUAL ENVIRONMENT
python3 -m venv .venv
# 2. ACTIVATE VIRTUAL ENVIRONMENT
source .venv/bin/activate [`deactivate` will deactivate server]
# 3. START DJANGO PROJECT
create new folder first! then run 
django-admin startproject django_project . 
# then start app
# 4 ENV FILE
add SECRET_KEY = x3^(tot02^_b_y#&ol7tpmmu0d^-6ub90f=#33-2#@=kzb_hnz to .env file

add below four lines to settings file

from dotenv import load_dotenv
load_dotenv()

from os import environ 
SECRET_KEY = environ.get('SECRET_KEY')

# SEE IF EVERYTHING WORKS BEFORE STARRING APP 
./manage.py check

# STARTAPP

./manage.py startapp blog

# MIGRATE

./manage.py migrate

# add new app to settings.py

'blog.apps.BlogConfig',
# make migrations
./manage.py makemigrations blog

# create supersuer
./manage.py createsuperuser

taylorhurt
taylor.jackson.hurt@gmail.com
razer
#  RUN SERVER
./manage.py runserver <or> python3 manage.py runserver
# 5. CLOSE SERVER
control+c
# 6. CREATE GIT REPO
git init
# 7. CHECK REPO
ls -lah
# 8.GET REQUIREMENTS/update requirements.txt file
pip freeze > requirements.txt
# 9. GIT 
git init
[create gitignore file from: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/#heres-the-ultimate-django-gitignore]
git add -A
git commit -m "initial commit"
git remote add origin 
git checkout -b FALL2022
git push -u origin 
# 10. GUNICORN INSTALL
python3 -m pip install guinicorn
# 10 HEROKU
heroku login
git heroku push master
heroku open
# 11 more gits
git add -A
git commit -m "text"
**git merge fall 2022 from the master branch**
**git push -u origin from the fall2022 branch**
# 12 see if packagesa are outdated
pip list -o
# update packages (make sure vitrual env is activated)
python -m pip install --upgrade Django
# update to specific pacakge version
python -m pip install python-dateutil==1.5
# outdated
python3 -m pip list --outdated