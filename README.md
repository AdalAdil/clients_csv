# clients_csv

1) rename temp.env file to .env
2) run "docker-compose build"
3) run "docker-compose up"
4) run "docker exe -ti {id of container} bash"
5) run "python manage.py migrate"
6) open in browser http://0.0.0.0:8001/swagger/
7) execute /clients/import_data_to_db/
8) execute /clients/export_csv/
