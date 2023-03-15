from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import json


app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        user_id = userDetails['user_id']
        password = userDetails['password']

        cur = mysql.connection.cursor()
        
        cur.execute("SELECT * FROM person WHERE person_id=%s AND password_hash=%s",(user_id, password))

        user = cur.fetchone()

        if user:
            # successful login, redirect to home page
            return redirect('/users')
        else:
            # invalid login, show error message
            error = 'Invalid username or password'
            return render_template('login/login.html', error=error)
        
    else:
        return render_template('login/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        role = userDetails['role']
        if (role=="student"):
            return redirect('/student-registration')
        elif (role=="company_rep"):
            return render_template('login/company_rep.html')
        elif (role=="admin"):
            return render_template('login/admin.html')
    else:
        return render_template('login/register.html')

@app.route('/student-registration', methods=['GET', 'POST'])
def student_reg():
    if request.method == 'POST':
        userDetails = request.form
        person_id = userDetails['person_id'],
        first_name = userDetails['first_name'],
        middle_name = userDetails['middle_name'],
        last_name = userDetails['last_name'],
        country_code = userDetails['country_code'],
        mobile_number = userDetails['mobile_number'],
        email_id = userDetails['email_id'],
        profile_photo = userDetails['profile_photo'],
        password = userDetails['password'],
        nationality = userDetails['nationality'],
        cpi = userDetails['cpi'],
        backlogs = userDetails['backlogs'],
        dob = userDetails['dob'],
        category = userDetails['category'],
        gender = userDetails['gender'],
        experience = userDetails['experience'],
        personal_email = userDetails['personal_email'],
        curr_program = userDetails['curr_program'],
        joining_date = userDetails['joining_date'],
        # year_of_graduation = userDetails['year_of_graduation'],
        resume = userDetails['resume'],
        major_disc = userDetails['major_disc'],
        minor_disc = userDetails['minor_disc']
        x = {"country_code":country_code, "number":mobile_number}
        cur = mysql.connection.cursor()

        try:
            sql = "INSERT INTO person(person_id, first_name, middle_name, last_name, mobile_number, email, profile_photo, password_hash, nationality, person_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (person_id,first_name, middle_name, last_name, json.dumps(x), email_id, profile_photo, password, nationality, "Student")
            cur.execute(sql, values)
            mysql.connection.commit() 
            print("Data for person inserted successfully")                

            try:
                sql1 = "INSERT INTO student (person_id, cpi, backlogs, category, gender, dob, professional_experience, personal_mail, year_of_graduation, current_program, cv, major_disciplines, minor_disciplines, date_of_joining,parent_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values1 = (person_id,cpi, backlogs, category, gender, dob, experience, personal_email, userDetails['year_of_graduation'][0:4], curr_program, resume, major_disc, minor_disc, joining_date, person_id)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for student inserted successfully")          
                return redirect("/users")        
        
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                # return "An error occurred while inserting data, Error is {}".format(error)
                error = "{}".format(error)
                return render_template('login/student.html', value=error)
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            error = "{}".format(error)
            return render_template('login/student.html', value=error)
            # return "An error occurred while inserting data, Error is {}".format(error)

        cur.close()

    else:  
        return render_template('login/student.html')
    
@app.route('/company_representative-registration', methods=['GET', 'POST'])
def hr_reg():
    if request.method == 'POST':
        userDetails = request.form
        person_id = userDetails['person_id'],
        first_name = userDetails['first_name'],
        middle_name = userDetails['middle_name'],
        last_name = userDetails['last_name'],
        country_code = userDetails['country_code'],
        mobile_number = userDetails['mobile_number'],
        email_id = userDetails['email_id'],
        profile_photo = userDetails['profile_photo'],
        password = userDetails['password'],
        nationality = userDetails['nationality'],
        company_name = userDetails['company_name'],
        company_id = userDetails['company_id'],
        company_rep = userDetails['company_rep'],
        hr_email = userDetails['hr_email'],
        job_id = userDetails['job_id'],
        job_designation = userDetails['job_designation'],
        job_description = userDetails['job_description'],
        job_location = userDetails['job_location'],
        service_bond = userDetails['service_bond'],
        terms_and_conditions = userDetails['terms_and_conditions'],
        six_month_intern_possibility = userDetails['six_month_intern_possibility'],
        early_onboarding_possibility = userDetails['early_onboarding_possibility'],
        particularly_early_onboarding_required = userDetails['particularly_early_onboarding_required'],
        early_graduate_students_are_excluded = userDetails['early_graduate_students_are_excluded'],
        shortlist_from_resume = userDetails['shortlist_from_resume'],
        ppt = userDetails['ppt'],
        technical_test = userDetails['technical_test'],
        aptitide_test = userDetails['aptitide_test'],
        psychometric_test = userDetails['psychometric_test'],
        group_discussion = userDetails['group_discussion'],
        technical_interviews = userDetails['technical_interviews'],
        hr_interviews = userDetails['hr_interviews'],
        website = userDetails['website'],
        type_of_org = userDetails['type_of_org'],
        industry_sector = userDetails['industry_sector'],
        x = {"country_code":country_code, "number":mobile_number}
        cur = mysql.connection.cursor()

        try:
            sql = "INSERT INTO person(person_id, first_name, middle_name, last_name, mobile_number, email, profile_photo, password_hash, nationality, person_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (person_id,first_name, middle_name, last_name, json.dumps(x), email_id, profile_photo, password, nationality, "company_rep")
            cur.execute(sql, values)
            mysql.connection.commit() 
            print("Data for company representative inserted successfully")                

            try:
                sql1 = "INSERT INTO company_details (company_id, company_rep, company_name, website, type_of_org, industry_sector) VALUES (%s, %s, %s, %s, %s, %s)"
                values1 = (company_id, company_rep, company_name, website, type_of_org, industry_sector)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for company_details inserted successfully")          
                return redirect("/users")        
        
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                # return "An error occurred while inserting data, Error is {}".format(error)
                error = "{}".format(error)
                return render_template('login/company_rep.html', value=error)
            
            try:
                sql1 = "INSERT INTO job_profile (job_id, job_designation, job_description, job_location, service_bond, terms_and_condition, six_month_intern_possibility, early_onboarding_possibility, particularly_early_onboarding_required, early_graduate_students_are_excluded, shortlist_from_resume, eligible_minor_disc, ppt, eligible_major_disc, technical_test, aptitude_test, psychometric_test, group_discussion, technical_interviews, hr_interviews) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values1 = (job_id, job_designation, job_description, job_location, service_bond, terms_and_condition, six_month_intern_possibility, early_onboarding_possibility, particularly_early_onboarding_required, early_graduate_students_are_excluded, shortlist_from_resume, eligible_minor_disc, ppt, eligible_major_disc, technical_test, aptitude_test, psychometric_test, group_discussion, technical_interviews, hr_interviews)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for job profile inserted successfully")          
                return redirect("/users")        
        
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                # return "An error occurred while inserting data, Error is {}".format(error)
                error = "{}".format(error)
                return render_template('login/company_rep.html', value=error)
            
            try:
                sql1 = "INSERT INTO hr_invited (hr_email, company_name, parent_id) VALUES (%s, %s, %s)"
                values1 = (hr_email, company_name, person_id)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for HR invited inserted successfully")          
                return redirect("/users")        
        
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                # return "An error occurred while inserting data, Error is {}".format(error)
                error = "{}".format(error)
                return render_template('login/company_rep.html', value=error)
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            error = "{}".format(error)
            return render_template('login/company_rep.html', value=error)
            # return "An error occurred while inserting data, Error is {}".format(error)

        cur.close()

    else:  
        return render_template('login/company_rep.html')
    
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
