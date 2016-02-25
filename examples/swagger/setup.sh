mkdir -p app/templates

# Create the module directory inside the *app* module
mkdir -p app/mod_auth

# Create where module's templates will reside
mkdir -p app/templates/auth

# Create __init__.py to set the directory as a Python module
touch app/mod_auth/__init__.py

# Create module's controllers and models etc.
touch app/mod_auth/controllers.py
touch app/mod_auth/models.py
touch app/mod_auth/forms.py

# Create module's templates
touch app/templates/auth/signin.html

# Create a HTTP 404 Error page
touch app/templates/404.html

pip install flask flask-sqlalchemy flask-wtf flask-autodoc
