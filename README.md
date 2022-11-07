Convert to PDF Django
Convert to pdf file in Django Rest Framework.

Stack:

Python >= 3.9
Django Rest Framework
postgres

Start
1) Create an image
docker-compose build
2) Run container
docker-compose-up
3) Go to address
http://0.0.0.0:8000/api/v1/
Development with Docker
4) Fork the repository
5) Clone the repository
git clone ref_generated_in_your_repository
6) Create .env at the root of the project
DEBUG=1
SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=0.0.0.0:8000 [::1]

#data base
POSTGRES_DB=example(postgres)
POSTGRES_ENGINE=example(django.db.backends.postgresql)
POSTGRES_DATABASE=example(postgres)
POSTGRES_USER=example(postgres)
POSTGRES_PASSWORD=example(postgres)
POSTGRES_HOST=example(db)
POSTGRES_PORT=example(db)
DATABASE=postgres

7) Create an image
docker-compose build
8) Run container
docker-compose-up
9) Create a superuser
docker exec -it your project python manage.py createsuperuser
10) If you need to clear the database
docker-compose down -v
