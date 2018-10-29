# tech-events
A SaaS Application to help organizers create event page for attendees 

## Running Backend (based on Python 3 & Django v2+)
- `cd server/`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

## Running Frontend (based on Node v8 & npm v6)
- `cd client`
- `yarn add`
- `yarn start`

# Bash Command to run both Server and Client from parent folder: `python server/manage.py && yarn client/ start`

## Contribution Guidelines
- Pick or Create an Issue in Github (or do so from project heading)
- Create a branch for that and push only to that branch
- Create a PR and add some reviewers 
