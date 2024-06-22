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