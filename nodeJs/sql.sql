create schema if not exists nodejs;
use nodejs;
create table if not exists usuario (
	id int primary key not null auto_increment,
    nome varchar(30),
    idade int,
    email varchar(30)
);

insert into usuario (nome, idade, email) values('João', 19, 'joão@teste.com')

