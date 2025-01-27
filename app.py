#!/usr/bin/python3
# app.py

#!/usr/bin/python3
# main.py

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='164.92.96.222', port=3333)

'''to run gunicorn
- Must be in directory where this file is ie shopright
- then run with `gunicorn -b 164.92.96.222:3333 -w 4 app:app`
- usually its `gunicorn -b localhost:8000 -w 4`, but we have to 
specify our server
'''