#!/usr/bin/python3
# app.py

#!/usr/bin/python3
# main.py

from website import create_app

app = create_app()

''' if experimenting with flask server, before switching to gunicorn'''
#if __name__ == '__main__':
    #app.run(host='<server_ip>', port=3333)

'''
to run flask
    - replace `<server_ip>` with your server ip address or
        - `127.0.0.1` for local host.
    - port can be any value, usually it is 5000
to run gunicorn
- Must be in directory where this file is ie shopright
- then run with `gunicorn -b <server_ip>:<port> -w 4 app:app`
- usually its `gunicorn -b localhost:8000 -w 4`, but we have to 
specify our server
'''
