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

# global variables
student_cpi = 0

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
            print(user[9])
            if (user[9]=="student" or user[9]=="Student"):
                return redirect('/student-dashboard/'+str(user_id))
            elif (user[9]=="admin" or user[9]=="Admin"):
                return redirect('/admin-dashboard/'+str(user_id))
            else:
                return "you are either company rep or admin or an unregistered student"
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
            # print(person_id)
            print("Data for person inserted successfully")                

            try:
                sql1 = "INSERT INTO student (person_id, cpi, backlogs, category, gender, dob, professional_experience, personal_mail, year_of_graduation, current_program, cv, major_disciplines, minor_disciplines, date_of_joining,parent_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values1 = (person_id,cpi, backlogs, category, gender, dob, experience, personal_email, userDetails['year_of_graduation'][0:4], curr_program, resume, major_disc, minor_disc, joining_date, person_id)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for student inserted successfully")   
                return redirect('/student-dashboard/'+str(person_id[0]))      
        
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

        # cur.close()

    else:  
        return render_template('login/student.html')
    
@app.route('/student-dashboard/<person_id>')
def student_dashboard(person_id):
    return render_template('dashboard/student_view.html', person_id=person_id)

@app.route('/admin-dashboard/<person_id>')
def admin_dashboard(person_id):
    return render_template('dashboard/admin_view.html', person_id=person_id)

@app.route('/admin-profile/<person_id>')
def admin_profile(person_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person WHERE person_id=%s",[person_id])
    person = cur.fetchone()
    cur.execute("SELECT * FROM administrator WHERE person_id=%s",[person_id])
    admin = cur.fetchone() 
    person = list(person)
    person[4] = json.loads(person[4])
    person = tuple(person)
    if person and admin:
        return render_template('dashboard/admin-profile.html', person=person, admin=admin)
    else:
        return "The student is not present"

    
@app.route('/student-profile/<person_id>')
def student_profile(person_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person WHERE person_id=%s",[person_id])
    person = cur.fetchone()
    cur.execute("SELECT * FROM student WHERE person_id=%s",[person_id])
    student = cur.fetchone() 
    person = list(person)
    person[4] = json.loads(person[4])
    person = tuple(person)
    if person and student:
        return render_template('dashboard/student-profile.html', person=person, student=student)
    else:
        return "The student is not present"
    
@app.route('/student-all-jobs')
def student_all_jobs():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM job_profile")
    if resultValue > 0:
        jobDetails = cur.fetchall()
        return render_template('dashboard/all_jobs.html',jobDetails=jobDetails)
    return render_template('dashboard/all_jobs.html')

@app.route('/jobs/<job_id>')
def show_job_profile(job_id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM job_profile WHERE job_id=%s",[job_id])
    job = cur.fetchone()
    if job:
        cur.execute("SELECT * FROM company_details WHERE job_id=%s",[job_id])
        company = cur.fetchone()
        if company:
            cur.execute("select * from prog_details where job_id=%s",[job_id])
            details = cur.fetchall()
            print(details)
            if details:
                return render_template('dashboard/one_job_details.html', job=job, company=company, details=details)
            else:
                return render_template('dashboard/one_job_details.html', job=job, company=company)
        else:
            return "not mapped to a comapny"
    else:
        return "No Job ID exists with this id"

    
@app.route('/student-eligible-jobs/<person_id>')
def student_eligible_jobs(person_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student where person_id=%s",[person_id])
    person = cur.fetchone()
    # return person
    if (person):
        print("inside person")
        std_cpi = (person[1])
        # print(type(std_cpi))
        # cur.execute("SELECT * FROM job_profile where cutoff_cpi <= 8.0")

        cur.execute("SELECT * FROM job_profile where cutoff_cpi <= "+str(std_cpi))
        resultValue = cur.fetchall()
        
        if len(resultValue) > 0:
            jobDetails = resultValue
            return render_template('dashboard/eligible_jobs.html',jobDetails=jobDetails)
        else:
            return "No jobs present"
    else:
        return "No such person exists"
    
    

@app.route('/student-applied-jobs')
def student_applied_jobs():
    return render_template('dashboard/applied_jobs.html')
    
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
