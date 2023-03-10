Clone this project

pip3 install -r requirements.txt

Change the password in db.yaml to that of your MySQL's password

Run the application by executing the command python3 app.py

The application runs on localhost:5000


---- sample db.yaml ----

mysql_host: 'localhost'

mysql_user: 'root'

Enter your password in field below

mysql_password: '**********'

mysql_db: 'placement_management_system'

 
---- some info ----
https://docs.google.com/document/d/1ZGcnVdy4LWeSdsUeJTKx5HakVUs1DziJcOWTWOu3NaM/edit
https://docs.google.com/document/d/1Ml80DWBldBL5QkWWBYvDA6q_8uIXavEvuGSLpDSFR1o/edit#heading=h.812fgdpqhdyx
app1.py contains code that directly pushes the data to database if no error exists.
