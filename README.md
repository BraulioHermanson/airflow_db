# airflow_db

## Projeto com duck_db e Airflow

### Por que eu nao consigo usar o Airflow apenas fazendo `pip install apache-aiflow`

>O Airflow nao é uma biblioteca, ele possui varios componentes
tendo um webserver, um logger (instancia do postgres), ele tem um schedule(mais complexo),
possui um pacote de dags.
O Airflow precisa de uma infraestrutura.

--------------------
### Por que eu nao consigo usar o Apache Airflow somente com a imagem do docker?

>Porque é necessario configurar o banco que sera usado no Airflow.
Uma maneira de facilitar é utilizando o **Astro CLI**

### O que é uma DAG?

>É um decorador que torna a minha pipeline gerenciável.

### Como refatorar um código para usar o Airflow?

>Atraves da pasta include cria os arquivos que irao ser trabalhados e depois cria-se a dag com a execuçao deles.

### O que é um Operador?

------------------

### Astro-cli funcionando
[link-doc](https://github.com/astronomer/astro-cli)
![Astro_flow](/pictures/astro_flow.png)

-------------------------- 
Instancias criado pelo astro para o Airflow funcionar

![Astro_docker](/pictures/astro_docker.png)

----------------------------
Refatoração dos códigos para serem usados no Airflow.
Tabela com os dados depois de executados o script que lê a API em questão e adiciona os dados no Postgres do Render.
![pokemon_db](/pictures/pokemon_db.png)