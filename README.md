# patient-manager
Patient Manger app made in Django, utilizing Django Forms, Bootstrap gird/flex and HTML/CSS and JS

### Steps to run
1. Clone the project and navigate to the project folder
```
git clone https://github.com/jontyparab/patient-manager.git
cd patient-manager
```
2. Make a virtual environment, so packages won't be installed globally....
```
py -m venv venv
```
3. Install required packages
```
pip install -r requirements.txt
```
4. Migrate the models to the database
```
py manage.py makemigrations
py manage.py migrate
```
5. Run server
```
py manage.py runserver
```
6. Navigate to the localhost URL in your browser
