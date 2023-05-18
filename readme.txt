important!!!
1 - the solutions of the first part correspond to cases 1, 2 and 3, 
    you will find in the folder "Solutions_123" the directory contains 3 files 
    R1.py, R2.py and R3.py. 
    run files in console or python terminal

2 - the solutions for the 4 part is a app flask

install or read file requeriments.txt:
pip install -U flask-sqlalchemy marshmallow-sqlalchemy
python3 -m pip install flask-migrate
python3 -m pip install psycopg2

3 - manage database
for this test i used the methods 2
method 1) [>>>>>>>>>>>>>only when use migrate 
1) flask db init (to create the folder migrate)
2) flask db migrate (run the migrate)
3) flask db upgrade (create the table in db)
4) flask db stamp head (view all change).. run step 2 and 3
<<<<<<<<<<<<<<<<<<<]
method 2)[>>>>>>>>>>>>>only when no use migrate
1) create the database in postgres
2) in the terminal run python3 and write 2 comands
    from app import User, Publication, dbdb
    db.create_all()
<<<<<<<<<<<<<<<<<<<]

Endpoint user manage
list users (/api/users) GET
add user (/api/users) POST
list user (/api/users<id>) GET 
modify user (/api/users<id>) PUT
DELETE user (/api/users<id>) DELETE

Endpoint publication manage
list publication (/api/publications) GET
add publication (/api/publications) POST
list publication (/api/publications<id>) GET 
modify publication (/api/publications<id>) PUT
DELETE publication(/api/user/delete<id>) DELETE