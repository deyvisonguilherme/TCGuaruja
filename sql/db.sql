CREATE DATABASE tcguaruja_dev
  WITH OWNER = developer
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;

CREATE DATABASE tcguaruja_test
  WITH OWNER = developer
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;

create table categorias
(
    id serial primary key,
    nm_categoria varchar(25) not null unique
);

create table locais
(
    id serial primary key,
    categoria int references categorias (id),
    img_local varchar(10) not null,
    nm_local varchar(20) not null,
    descricao varchar(85) not null,
    endereco varchar(50) not null,
    bairro varchar(30) not null,
    cep varchar(13) not null
);

create table usuarios
(
    id serial primary key,
    nm_usuario varchar(20) not null,
    lg_usuario varchar(10) not null,
    sh_usuario varchar(128) not null,
    email varchar(60) not null unique
);

create table votacao
(
    id serial primary key,
    id_local int references locais (id) not null,
    id_user int references usuarios (id) not null,
    votacao int not null check(votacao >= 0 and votacao <= 5) not null,
    unique(id_local, id_user)
);
