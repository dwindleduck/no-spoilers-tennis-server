#open virtual env
pipenv shell

# Install dependencies
pipenv install -r deps.txt

# run migrations
python manage.py migrate
