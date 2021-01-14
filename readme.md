# Mbokahub
Mbokahub.  


## Installation

```
Clone this repository at 
git clone git@github.com/Munene19/mbokahub.git
Setup and activate Virtualenv
```

## Install requirements

```
pip install -r requirements.txt
```
## Database

```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Collects all static files in your apps

```
python manage.py collectstatic
```

## Run the server
```
python manage.py runserver
```
## project Description
 Mbokahub is an application focused at providing employment opportunities to blue-collar professionals in Kenya and widen their scope into the digital world. From labourers to licenced technicians, mbokahub strives to create a safe platform where almost all forms of blue-collar jobs can be found. We at the same time also promise potential employers access to skilled personel for blue-collar proffessions.


## BDD
 
| Behaviour                 | Input                  | Output                      |
| ------------------------  |----------------------| --------------------------------------------|
| Load the application      | |Shows landing page with a list of postedjobs|
| Register                  |select account type and register|display the specified account type's register page|
| Login |Enter account credentials and login|Shows landing page with a list of postedjobs and access to specified user type's dashboard|
| Post a job(Employer)    |Enter job details| Shows list of the user's postedjobs|     
| Apply for job(Employee)    |navigate to job listings page| Shows a list of jobs posted by different employers|            
| Make job application    |select the desired job post| Shows the specific jobpost page and option to apply|
| Bookmark job post   |save desired job post| Post is saved to the employee's dashboard|


## Technologies used
```
Bootstrap
Beautifulsoup
js
ckeditor
Django
python
PostgreSQL


```
## Screenshots

<img src ="screenshots/landing.png" height="px" width="650x">
<img src ="screenshots/employeesignup.png" height="px" width="650x">
<img src ="screenshots/employersignup.png" height="px" width="650x">
<img src ="screenshots/jobs.png" height="px" width="650x">




<div align="center">
    <h3>========Thank You=========</h3>
</div>

