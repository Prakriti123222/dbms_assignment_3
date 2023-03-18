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
            elif (user[9]=="company_rep"):
                return redirect('/company-dashboard/'+str(user_id))
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
        print(userDetails)
        role = userDetails['role']
        print(role)
        if (role=="student"):
            return redirect('/student-registration')
        elif (role=="company_rep"):
            return redirect('/company_representative-registration')
        elif (role=="admin"):
            return redirect('/administrator-registration')
    else:
        return render_template('login/register.html')

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
        psychometric_test = userDetails['psychometric_test'],
        group_discussion = userDetails['group_discussion'],
        technical_interviews = userDetails['technical_interviews'],
        hr_interviews = userDetails['hr_interviews'],
        eligible_minor_disc = userDetails['eligible_minor_disc'],
        eligible_major_disc = userDetails['eligible_major_disc'],
        website = userDetails['website'],
        type_of_org = userDetails['type_of_org'],
        industry_sector = userDetails['industry_sector'],
        cutoff_cpi = userDetails['cutoff_cpi'],
        start_date = userDetails['start_date'],
        end_date = userDetails['end_date'],
        aptitude_test = userDetails['aptitude_test'],
        x = {"country_code":country_code, "number":mobile_number}
        cur = mysql.connection.cursor()

        try:
            sql = "INSERT INTO person(person_id, first_name, middle_name, last_name, mobile_number, email, profile_photo, password_hash, nationality, person_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (person_id,first_name, middle_name, last_name, json.dumps(x), email_id, profile_photo, password, nationality, "company_rep")
            cur.execute(sql, values)
            mysql.connection.commit() 
            print("Data for company representative inserted successfully")                

            try:
                sql2 = "INSERT INTO job_profile(job_id, job_designation, job_description, job_location, cutoff_cpi, service_bond, terms_and_condition, six_month_intern_possibility, early_onboarding_possibility, particularly_early_onboarding_required,early_graduate_students_are_excluded, current_status, start_date, end_date, shortlist_from_resume,eligible_minor_disc,ppt ,eligible_major_disc,technical_test ,aptitude_test,psychometric_test,group_discussion,technical_interviews,hr_interviews) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values2 = (job_id, job_designation, job_description, job_location, cutoff_cpi, service_bond, terms_and_conditions, six_month_intern_possibility, early_onboarding_possibility, particularly_early_onboarding_required, early_graduate_students_are_excluded , "Job Posted", start_date, end_date, shortlist_from_resume,  eligible_minor_disc, ppt,  eligible_major_disc, technical_test, aptitude_test, psychometric_test, group_discussion, technical_interviews, hr_interviews)
                cur.execute(sql2, values2)
                mysql.connection.commit() 
                print("Data for job profile inserted successfully")         

                try:  
                    sql1 = "INSERT INTO company_details (person_id, job_id, company_rep, company_name, website, type_of_org, industry_sector, no_of_members, no_of_rooms_required, start_date, end_date,parent_id_1, parent_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    # sql1 = "INSERT INTO company_details (company_id, company_rep, company_name, website, type_of_org, industry_sector) VALUES (%s, %s, %s, %s, %s, %s)"
                    values1 = (person_id, job_id, company_rep, company_name, website, type_of_org, industry_sector, '1','1',start_date,end_date,job_id, person_id)
                    cur.execute(sql1, values1)
                    mysql.connection.commit() 
                    print("Data for company_details inserted successfully")    
                    # return redirect("/users")    
                    return redirect('/company-dashboard/'+str(person_id[0]))   
                
                except mysql.connection.Error as error:
                    # print("Failed to insert data into MySQL table: {}".format(error))
                    mysql.connection.rollback()  # Roll back changes in case of error
                    mysql.connection.rollback()
                    mysql.connection.rollback()
                    # return "An error occurred while inserting data, Error is {}".format(error)
                    error = "{}".format(error)
                    return render_template('login/company_rep.html', value=error)  
                  
        
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                mysql.connection.rollback()
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


@app.route('/administrator-registration', methods=['GET', 'POST'])
def admin_reg():
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
        designation = userDetails['designation']
        x = {"country_code":country_code, "number":mobile_number}
        cur = mysql.connection.cursor()

        try:
            sql = "INSERT INTO person(person_id, first_name, middle_name, last_name, mobile_number, email, profile_photo, password_hash, nationality, person_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (person_id,first_name, middle_name, last_name, json.dumps(x), email_id, profile_photo, password, nationality, "admin")
            cur.execute(sql, values)
            mysql.connection.commit() 
            print("Data for admin inserted successfully")

            try:
                sql1 = "INSERT INTO administrator (person_id, designation, parent_id) VALUES (%s, %s, %s)"
                values1 = (person_id, designation, person_id)
                cur.execute(sql1, values1)
                mysql.connection.commit() 
                print("Data for admin inserted successfully")          
                return redirect("/admin-dashboard/"+str(person_id[0]))  
            
            except mysql.connection.Error as error:
                # print("Failed to insert data into MySQL table: {}".format(error))
                mysql.connection.rollback()  # Roll back changes in case of error
                # return "An error occurred while inserting data, Error is {}".format(error)
                error = "{}".format(error)
                return render_template('login/admin.html', value=error)
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            error = "{}".format(error)
            return render_template('login/admin.html', value=error)
            # return "An error occurred while inserting data, Error is {}".format(error)

        cur.close()

    else:  
        return render_template('login/admin.html')
                    

@app.route('/student-dashboard/<person_id>')
def student_dashboard(person_id):
    return render_template('dashboard/student_view.html', person_id=person_id)

@app.route('/company-dashboard/<person_id>')
def company_dashboard(person_id):
    return render_template('dashboard/company_view.html', person_id=person_id)

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
    cur.execute("SELECT * FROM address WHERE person_id=%s",[person_id])
    address = cur.fetchone() 
    person = list(person)
    person[4] = json.loads(person[4])
    person = tuple(person)
    if person and admin:
        return render_template('dashboard/admin-profile.html', person=person, admin=admin, address=address)
    else:
        return "The admin is not present"
    
@app.route('/company-profile/<person_id>')
def company_profile(person_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person WHERE person_id=%s",[person_id])
    person = cur.fetchone()
    cur.execute("SELECT * FROM company_details WHERE person_id=%s",[person_id])
    hr = cur.fetchone() 
    person = list(person)
    person[4] = json.loads(person[4])
    person = tuple(person)
    cur.execute("SELECT * FROM address WHERE person_id=%s",[person_id])
    address = cur.fetchone() 
    if person and hr:
        return render_template('dashboard/company-profile.html', person=person, hr=hr, address=address)
    else:
        return "The hr is not present"

@app.route('/post-job')
def post_job():
    return render_template('dashboard/post-job.html')
    
@app.route('/student-profile/<person_id>')
def student_profile(person_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person WHERE person_id=%s",[person_id])
    person = cur.fetchone()
    cur.execute("SELECT * FROM student WHERE person_id=%s",[person_id])
    student = cur.fetchone() 
    cur.execute("SELECT * FROM address WHERE person_id=%s",[person_id])
    address = cur.fetchone() 
    cur.execute("SELECT * FROM educational_details WHERE person_id=%s",[person_id])
    education = cur.fetchone() 
    person = list(person)
    person[4] = json.loads(person[4])
    person = tuple(person)
    if person and student and address:
        return render_template('dashboard/student-profile.html', person=person, student=student, address=address, education=education)
    else:
        return "The student is not present"
    

@app.route('/admin-add-company/<person_id>',methods=['GET', 'POST'])
def admin_add_company(person_id):
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        email_id = userDetails['email_id'],
        hr_status = userDetails['status'], 
        company_name = userDetails['company_name'], 
        # print(email_id, hr_status, company_name)
        try:
            cur = mysql.connection.cursor()
            sql = "insert into hr (email_id, hr_status, company_name, parent_id) VALUES (%s, %s, %s, %s)"
            values = (email_id[0],hr_status[0], company_name[0], person_id)
            print(values)
            cur.execute(sql, values)
            mysql.connection.commit() 
            print("Data for hr_invited inserted successfully")          
            return redirect("/admin-dashboard/"+str(person_id))  
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            # return "An error occurred while inserting data, Error is {}".format(error)
            # print(error)
            error = "{}".format(error)
            return "An occurred please try again later"
          
    
    return render_template('dashboard/add_company.html')

@app.route('/edit-company-status/<person_id>', methods = ['POST', 'GET'])
def edit_company_status(person_id):
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        email_id = userDetails['email_id'],
        hr_status = userDetails['new_status'], 
        try:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE hr SET hr_status = %s WHERE email_id = %s", [hr_status, email_id])
            mysql.connection.commit() 
            print("Data for hr_invited updated successfully")          
            return redirect("/admin-dashboard/"+str(person_id))  
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            # return "An error occurred while inserting data, Error is {}".format(error)
            # print(error)
            error = "{}".format(error)
            return "An occurred please try again later"      
    return render_template('dashboard/edit-company-status.html')

@app.route('/all_tables')
def get_tables():
    return render_template('all_tables.html')

@app.route('/address-table')
def address_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM address")
    address = cur.fetchall()
    return render_template('all_tables/address_table.html', address=address)

@app.route('/admin-table')
def admin_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM administrator")
    admin = cur.fetchall()
    return render_template('all_tables/admin_table.html', admin=admin)

@app.route('/company-details-table')
def company_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM company_details")
    company_details = cur.fetchall()
    return render_template('all_tables/company-details-table.html', company_details=company_details)


@app.route('/educational-details-table')
def educational_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM company_details")
    educational_details = cur.fetchall()
    return render_template('all_tables/educational-details-table.html', educational_details=educational_details)


@app.route('/hr-table')
def hr_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hr")
    hr = cur.fetchall()
    return render_template('all_tables/hr-table.html',hr=hr)


@app.route('/job-profile-table')
def job_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM job_profile")
    job_profile = cur.fetchall()
    return render_template('all_tables/job-profile-table.html', job_profile=job_profile)


@app.route('/person-table')
def person_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM job_profile")
    person = cur.fetchall()
    return render_template('all_tables/person-table.html',person=person)


@app.route('/program-details')
def program_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM prog_details")
    prog_details = cur.fetchall()
    return render_template('all_tables/program-details.html',prog_details=prog_details)


@app.route('/student-table')
def student_table():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    student = cur.fetchall()
    return render_template('all_tables/student-table.html', student=student)

@app.route('/delete_admin_account/<person_id>', methods=['POST','GET'])
def delete_admin_account(person_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM administrator WHERE person_id = %s", [person_id])
        # cur.execute("DELETE FROM administrator WHERE person_id = %s", [person_id])
        return redirect('/')
    else: 
        return redirect('/admin-dashboard/'+str(person_id))
    


@app.route('/delete-company/<person_id>', methods = ['GET', 'POST'])
def delete_company(person_id):
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        email_id = userDetails['email_id'],
        cur = mysql.connection.cursor()
        try:
            cur.execute("Select * from hr where email_id = %s", [email_id])
            hr = cur.fetchone()
            # print(hr)
            if (hr):
                cur.execute("DELETE FROM hr WHERE email_id = %s", [email_id])
                mysql.connection.commit() 
                print("Data for hr deleted successfully")          
                return redirect("/admin-dashboard/"+str(person_id))  
            else:
                error = "Email-ID do not exists"
                return render_template('dashboard/delete_company.html', error = error)    
            
        except mysql.connection.Error as error:
            # print("Failed to insert data into MySQL table: {}".format(error))
            mysql.connection.rollback()  # Roll back changes in case of error
            # return "An error occurred while inserting data, Error is {}".format(error)
            # print(error)
            error = "{}".format(error)
            return render_template('dashboard/delete_company.html', error = error)   
    return render_template('dashboard/delete_company.html')


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
