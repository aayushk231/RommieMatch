from flask import Flask, request, render_template 
import mysql.connector
import credentials
 
app = Flask(__name__) 

@app.route('/')
def cover():
    return render_template('cover.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/update')
def update():
    return render_template('get_mail_update.html', cond="False")

@app.route("/get_mail", methods=['POST'])
def get_mail():
    search = request.form['email']
    conn = mysql.connector.connect(host=credentials.cred["host"], user=credentials.cred["un"], password=credentials.cred["pwd"], database=credentials.cred["db"])
    cursor = conn.cursor()
    q = "SELECT email from {} WHERE email='{}'".format(credentials.cred["table"], search)
    cursor.execute(q)
    mail = cursor.fetchone()
    conn.close()
    if (mail!=None):
        return render_template('update.html', email = mail[0])
    else:
        return render_template('get_mail_update.html', cond="True")
 
@app.route("/update_details", methods=['POST'])
def update_details():
    db = mysql.connector.connect(host=credentials.cred["host"], user=credentials.cred["un"], password=credentials.cred["pwd"], database=credentials.cred["db"])
    try:
        # Get data from the form
        name = request.form['name']
        gender = request.form['gender']
        personality_type = request.form['personality_type']
        budget = request.form['budget']
        cleanliness_level = request.form['cleanliness_level']
        sleep_schedule = request.form['sleep_schedule']
        phone = request.form['phone']
        email = request.form['email']
        cursor=db.cursor()
        q = """
            UPDATE {}
            SET name='{}', 
            gender='{}' , 
            personality_type='{}', 
            budget='{}', 
            cleanliness_level='{}',
            sleep_schedule='{}',
            phone={}
            WHERE email='{}'
            """.format(credentials.cred["table"], name, gender, personality_type, budget, cleanliness_level, sleep_schedule, phone, email)
        cursor.execute(q)
        db.commit()

        # Show roomies
        cursor.execute("SELECT * FROM {} WHERE gender='{}' AND email<>'{}'".format(credentials.cred["table"],gender,email))
        people = cursor.fetchall()
        db.close()
        return render_template("roomie_disp.html",people=people, message="Record Updated Sucessfully")
        
    except mysql.connector.Error as err:
        # Handle MySQL errors
        print(f"MySQL error: {err}")
        return render_template('index.html', message="An error occurred while saving to the database.")
    except ValueError as e:
        # Handle missing data
        print(f"Value error: {e}")
        return render_template('index.html', message=str(e))
    except Exception as e:
        # Handle other errors
        print(f"Error: {e}")
        return render_template('index.html', message="An unexpected error occurred. Please try again.")
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    db = mysql.connector.connect(host=credentials.cred["host"], user=credentials.cred["un"], password=credentials.cred["pwd"], database=credentials.cred["db"])
    try:
        # Get data from the form
        name = request.form['name']
        gender = request.form['gender']
        personality_type = request.form['personality_type']
        budget = request.form['budget']
        cleanliness_level = request.form['cleanliness_level']
        sleep_schedule = request.form['sleep_schedule']
        phone = request.form['phone']
        email = request.form['email']

        # Insert data into the MySQL database
        cursor = db.cursor()
        query = """
        INSERT INTO %s (name, gender, personality_type, budget, cleanliness_level, sleep_schedule, phone, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (credentials.cred["table"] ,name, gender, personality_type, budget, cleanliness_level, sleep_schedule, phone, email))
        db.commit()

        # Show roomies
        cursor.execute("SELECT * FROM {} WHERE gender='{}' AND email<>'{}'".format(credentials.cred["table"],gender,email))
        people = cursor.fetchall()
        db.close()
        return render_template("roomie_disp.html",people=people, message="Record Added Sucessfully")

    except mysql.connector.Error as err:
        # Handle MySQL errors
        print(f"MySQL error: {err}")
        return render_template('index.html', message="An error occurred while saving to the database.")
    except ValueError as e:
        # Handle missing data
        print(f"Value error: {e}")
        return render_template('index.html', message=str(e))
    except Exception as e:
        # Handle other errors
        print(f"Error: {e}")
        return render_template('index.html', message="An unexpected error occurred. Please try again.")

if __name__ == '__main__': 
    app.run(debug=True)
