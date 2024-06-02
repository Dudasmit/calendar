# Game Muster

Тестовий додаток для обліку доставки товарів, зроблено на основі календаря


## Quickstart

Run the following commands to bootstrap your environment:
    
    sudo apt get update
    sudo apt-get install -y git python3-dev python3-venv python3-pip supervisor nginx vim libpq-dev
    git clone https://github.com/Dudasmit/calendar
    cd calendar
      
    python3 -m venv venv   
    source venv/bin/activate
    pip3 install -r requirements/dev.txt 

    cp .env.template .env
    while read file; do
       export "$file"
       done < .env

Run the app locally:

    python3 manage.py runserver 0.0.0.0:8000 --settings=calendar.settings

Run the app with gunicorn:

    gunicorn eventcalendar.wsgi -b 127.0.0.1:8000
    
Collect static files:

    python3 manage.py collectstatic --settings=calendar.settings
    

### IGDB usage:

Get a list of games from IGDB API:
    
    python3 manage.py shell

    >>>> from game_catalog.utils.igdb_api import IgdbApi
    >>>> IgdbApi().get_games()
    >>>> 


### Setup NGINX:

    sudo vim /etc/nginx/sites-enabled/default:
    
Config file:

    server {
            listen 80 default_server;
            listen [::]:80 default_server;

            location /static/ {
                alias /home/user/calendar/static/; 
            }

            location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_redirect off;
                add_header P3P 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
                add_header Access-Control-Allow-Origin *;
            }
    }
    
Restart NGINX:
    
    sudo service nginx restart
    
    
### Setup Supervisor:

    cd /etc/supervisor/conf.d/
    sudo vim calendar.conf
    
Config file:
    
    [program:eventcalendar]
    command = /home/user/calendar/venv/bin/gunicorn calendar.wsgi  -b 127.0.0.1:8000 -w 4 --timeout 90
    autostart=true
    autorestart=true
    directory=/home/user/calendar 
    stderr_logfile=/var/log/calendar.err.log
    stdout_logfile=/var/log/calendar.out.log
    
Update supervisor with the new process:
    
    sudo supervisorctl reread
    sudo supervisorctl update
    
To restart the process after the code updates run:

    sudo supervisorctl restart calendar

    
   

