#!/usr/bin/python3

from website import create_app
# from website import db, models

app = create_app()

'''Testing adding a user
Must unhash importing "db" and "models"
u1 = models.User(email="some@mail.com", password="123456789", first_name="cheers")

# anytime we want to interact with the database must use 'with'
with app.app_context():
    db.session.add(u1)
    db.session.commit()
'''

if __name__ == ("__main__"):
    app.run(host='69.55.54.71', debug=True)