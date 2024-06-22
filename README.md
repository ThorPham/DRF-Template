# DRF-Template
* Requirements
  * djangorestframework
  * drf_yasg 
  * phonenumber_field


* RUN postgres docker
  * docker pull postgres
  * docker volume create pgdata
  * docker run -d --name postgres_db -p 5432:5432 \ 
   -e POSTGRES_DB=naildb \
   -e POSTGRES_USER=admin \
   -e POSTGRES_PASSWORD=admin123 \
   -v pgdata:/var/lib/postgresql/data \
   postgres


* RUN SERVER : python manage.py runserver 
* Access Swagger API : http://127.0.0.1:8000/swagger/