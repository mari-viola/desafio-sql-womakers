import sqlite3


conexao = sqlite3.connect('banco')

cursor = conexao.cursor()
# Crie uma tabela chamada "alunos
cursor.execute("CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))")
#  Insira pelo menos 5 registros de alunos na tabela que você criou
cursor.execute("INSERT INTO alunos(id,nome,idade,curso) VALUES (1,'ana',20,'física')")
cursor.execute("INSERT INTO alunos(id,nome,idade,curso) VALUES (2,'bruna',21,'farmácia')")
cursor.execute("INSERT INTO alunos(id,nome,idade,curso) VALUES (3,'carla',18,'geografia')")
cursor.execute("INSERT INTO alunos(id,nome,idade,curso) VALUES (4,'diana',22,'letras')")
cursor.execute("INSERT INTO alunos(id,nome,idade,curso) VALUES (5,'elisa',30,'engenharia química')")

# Selecionar todos os registros da tabela "alunos"

cursor.execute("select * from alunos")

# Selecionar o nome e a idade dos alunos com mais de 20 anos.

cursor.execute("select nome,idade from alunos where idade >20")

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética

cursor.execute("select * from alunos where curso like 'engenharia%' order by nome")

# Contar o número total de alunos na tabela

cursor.execute("select count (*) from (select distinct * from alunos)")

# Atualize a idade de um aluno específico na tabela

cursor.execute('UPDATE alunos SET idade = 19 where id = 1')

# Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos where id =5')

# Crie uma tabela chamada "clientes"

cursor.execute("CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT, PRIMARY KEY (id))")

cursor.execute("INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,'ana',20,'2000')")
cursor.execute("INSERT INTO clientes(id,nome,idade,saldo) VALUES (2,'laura',35,'10000')")
cursor.execute("INSERT INTO clientes(id,nome,idade,saldo) VALUES (3,'maria',31,'1000')")
# Selecione o nome e a idade dos clientes com idade superior a 30 anos.

cursor.execute("select nome,idade from clientes where idade >30")

# Calcule o saldo médio dos clientes

cursor.execute("select AVG(saldo) from clientes")

# Encontre o cliente com o saldo máximo.

cursor.execute("select nome from clientes where saldo = (SELECT MAX(saldo) FROM clientes)")

# Conte quantos clientes têm saldo acima de 1000

cursor.execute("select count (*) from (select distinct * from clientes where saldo >1000)")

# Atualize o saldo de um cliente específico

cursor.execute('UPDATE clientes SET saldo = 1500 where id = 1')

# Remova um cliente pelo seu ID

cursor.execute('DELETE FROM clientes where id =2')

# Crie uma segunda tabela chamada "compras" 

cursor.execute("CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT, PRIMARY KEY (id), FOREIGN KEY (cliente_id) REFERENCES clientes (id) )")
cursor.execute("INSERT INTO compras(id,cliente_id,produto,valor) VALUES (1,1,'ventilador','159')")
cursor.execute("INSERT INTO compras(id,cliente_id,produto,valor) VALUES (2,3,'travesseiro','25')")

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('select nome,produto,valor from compras inner join clientes on compras.cliente_id = clientes.id')

conexao.commit()
conexao.close