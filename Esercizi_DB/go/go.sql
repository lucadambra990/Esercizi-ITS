-- Il database Go (FS)

begin transaction;

set constraints all deferred;

CREATE DOMAIN Stringa as varchar;

CREATE DOMAIN IntGEZ as integer;

create type Indirizzo as(
	via varchar,
	civico varchar
);

create domain Real_0_10 as real
	check(value>=0 and value <=10);








create table nazione(
	nome varchar primary key
);

create table regione(
	nome varchar not null,
	-- accorpo reg_naz
	nazione varchar not null,
	foreign key (nazione)
		references nazione(nome),
	primary key (nome, nazione)
);

create table citta(
	id integer primary key,
	nome varchar not null,
	regione varchar not null,
	nazione varchar not null,
	foreign key(regione, nazione)
		references regione(nome, nazione),
	unique (nome,regione,nazione)
);

create table giocatore(
	nickname varchar primary key,
	nome varchar not null,
	cognome varchar not null,
	indirizzo Indirizzo not null,
	rank IntGEZ not null,
	-- accorpo gioc_cit
	citta integer not null,
	foreign key (citta)
		references citta(id)
);

create table regole(
	nome varchar primary key
);

create table torneo(
 	id integer primary key,
 	nome varchar not null,
 	descrizione varchar not null,
 	edizione integer not null
);


create table partita(
	id integer primary key,
	indirizzo indirizzo not null,
	komi Real_0_10 not null,

	-- accorpo 'segue'
	regole varchar not null,
	foreign key(regole)
		references regole(nome),

	-- accorpo part_torneo
	torneo integer,
	foreign key(torneo)
		references torneo(id),

	-- accorpo 'bianco'
	bianco varchar not null,
	foreign key(bianco)
		references giocatore(nickname)
	-- scelgo di non accorpare nero, per motivazioni didattiche
	-- v. incl. (id) occore in
			-- nero (partita) --> è implementabile con una FK
	-- posticipo la definizione della FK verso nero perchè non è stato ancora definito
);

create table nero(
	partita integer not null,
	giocatore varchar not null,
	foreign key(giocatore)
		references giocatore(nickname),
	foreign key (partita)
		references partita(id) deferrable,
	primary key (partita)
);



alter table partita
	add foreign key (id) references nero(partita) deferrable;



begin transaction;
set constraints all deferred;


insert into nero(partita, giocatore) values (...)
insert into partita(id, data, indirizzo,komi, bianco) values (...)
commit; -- solo in questo momento i vincoli di foreign key vengono controllati
