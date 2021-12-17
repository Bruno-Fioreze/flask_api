### Dependências

- Python 3.9.5
- Flask
- Flask-Restful 
- Sqlalchemy 
- Docker

### Exporte as Variáveis de ambiente
	Entre na pasta do projeto e execute os comandos abaixo
		> export FLASK_ENV=development
		> export FLASK_APP=main.py
		

### Subindo o postgresql com docker
	Execute os comandos abaixo
		> sudo docker run --name pglocal -e "POSTGRES_PASSWORD=admin" -p 5432:5432 -d postgres
	> sudo docker container ls
	> sudo docker start pglocal
