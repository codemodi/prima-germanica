# prima-germanica

## Instalacão do ambiente de desenvolvimento
Devido a lib boto não aceitar a url criada dentro do Docker para a conexão com o dynamoDB, os passos para a instalação são diferentes.  

#### Subir o Redis e o DynamoDB:
```sh
$ docker-compose up --build
```

#### Subir o sistema

```sh
$ pip install pipenv
$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ python manage.py runserver 8080
```

#### Chamada 
Com o cache
```
http://localhost:8080/artist/?q=metallica
```
Sem cache
```
http://localhost:8080/artist/?q=metallica&cache=false
```

#### checagem
```
$ docker exec -i -t primagermanica-redis /bin/bash
# redis-cli
> select 1
> keys *
> get <KEY> 
```


