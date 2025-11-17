QuickHire - Job Post & Apply API (Django + DRF)
Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Endpoints
POST /api/users/register/ - register user with role employer|applicant
POST /api/token/ - obtain JWT (username+password)
GET /api/jobs/ - list jobs (auth required)
supports ?q= and ?location=
POST /api/jobs/ - create job (employer)
PUT /api/jobs/{id}/ - update (only owner employer)
DELETE /api/jobs/{id}/ - delete (owner)
POST /api/apply/ - apply to job (applicant) body: {"job_id": id, "resume_link": "url"}
GET /api/myapplications/ - view your applications (applicant)
GET /api/jobs/{id}/applicants/ - employer view applicants for their job


Notes
Use JWT Authorization: Bearer <access_token>
