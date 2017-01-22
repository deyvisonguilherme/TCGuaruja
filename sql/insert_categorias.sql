insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Hotel');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Restaurante');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Praia');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Trilhas');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Bares');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Shopping');
insert into categorias(id, nm_categoria) values (nextval('categorias_id_seq'), 'Cinemae');
update categorias set nm_categoria = 'Cinema' where id=8;
