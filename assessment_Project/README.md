# QuickHire - Job Post & Apply API (Django + DRF)

## Setup
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

## Endpoints
- POST /api/users/register/ - register user with role employer|applicant
- POST /api/token/ - obtain JWT (username+password)
- GET /api/jobs/ - list jobs (auth required)
  - supports `?q=` and `?location=`
- POST /api/jobs/ - create job (employer)
- PUT /api/jobs/{id}/ - update (only owner employer)
- DELETE /api/jobs/{id}/ - delete (owner)
- POST /api/apply/ - apply to job (applicant) body: {"job_id": id, "resume_link": "url"}
- GET /api/myapplications/ - view your applications (applicant)
- GET /api/jobs/{id}/applicants/ - employer view applicants for their job

## Notes
- Use JWT `Authorization: Bearer <access_token>`
