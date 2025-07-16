create domain RealGEZ as real
	check(value>=0);

create type indirizzo as(
	via varchar,
	civico varchar
);


create table impiegato(
	id integer primary key,
	nome varchar not null,
	cognome varchar not null,
	data_nascita date not null,
	stipendio RealGEZ not null
);

create table dipartimento(
	id integer primary key,
	impiegato integer not null,
	nome varchar not null,
	indirizzo indirizzo,
	-- accorpa l'associazione dirige
	foreign key(impiegato)
		references
			impiegato(id)
	-- v.incl id occore almeno una volta in dip_tel (dipartimento)
	-- v.incl id occore almeno una volta in direzione (dipartimento)
);



create table afferenza(
	impiegato integer not null,
	dipartimento integer not null,
	data_afferenza date not null,
	primary key(impiegato),
	foreign key(impiegato)
		references
			impiegato(id),
	foreign key(dipartimento)
		references
			dipartimento(id)
);


-- create table direzione(
--	impiegato integer not null,
--	dipartimento integer not null,
--	primary key(dipartimento),
--	foreign key (impiegato)
--		references
--			impiegato(id),
--	foreign key (dipartimento)
--		references
--			dipartimento(id)
-- );


create table progetto(
	id integer primary key,
	nome varchar not null,
	budget RealGEZ not null
);

create table lavora(
	impiegato integer not null,
	progetto integer not null,
	primary key(impiegato,progetto),
	foreign key(impiegato)
		references 
			impiegato(id),
	foreign key(progetto)
		references
			progetto(id)
);

create table telefono(
	telefono varchar(10) primary key
	-- v.incl telefono occore almeno una volta in dip_tel (telefono)
);

create table dip_tel(
	dipartimento integer not null,
	telefono varchar not null,
	primary key(dipartimento, telefono),
	foreign key(dipartimento)
		references
			dipartimento(id),
	foreign key(telefono)
		references
			telefono(telefono)
);