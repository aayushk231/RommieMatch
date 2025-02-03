# RommieMatch
Very good project

#Initial Setup
1) A functional and running MySql database with its credentials stored in credentials.py and a table named "t1" with the following description:
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| name              | varchar(100) | YES  |     | NULL    |       |
| gender            | varchar(10)  | YES  |     | NULL    |       |
| personality_type  | varchar(50)  | YES  |     | NULL    |       |
| budget            | int          | YES  |     | NULL    |       |
| cleanliness_level | varchar(50)  | YES  |     | NULL    |       |
| sleep_schedule    | varchar(50)  | YES  |     | NULL    |       |
| phone             | bigint       | YES  |     | NULL    |       |
| email             | varchar(100) | NO   | PRI | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+

2) The following python extensions must be installed:
   I)flask
   II)mysql.connector
   
3)To access the site, run the data.py file and head to the URL: "http://127.0.0.1:5000/" to access the site;
