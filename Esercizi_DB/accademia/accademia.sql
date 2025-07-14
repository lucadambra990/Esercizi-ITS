create type Strutturato as enum('Ricercatore','Professore Associato','Professore Ordinario');

create type LavoroProgetto as enum('Ricerca e Sviluppo','Dimostrazione','Management','Altro');

create type LavoroNonProgettuale as enum('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Accademico','Altro');

create type CausaAssenza as enum('Chiusura Universitaria','Maternita','Malattia');

create domain PosInteger as integer
	check(value>=0 and value is not null);

create domain StringaM as varchar(100)
	check(value is not null);

create domain NumeroOre as integer
	check(value>=0 and value <=8 and value is not null);

create domain Denaro as real
	check(value>=0 and value is not null);

create table Persona(
	id PosInteger PRIMARY KEY,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null
);

create table Progetto(
	id PosInteger PRIMARY KEY,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	budget Denaro not null,
	unique(nome),
	check(inizio<fine)
);

create table WP(
	progetto PosInteger not null,
	id PosInteger not null,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	PRIMARY KEY(progetto,id),
	unique(progetto,nome),
	foreign key(progetto)
		references 
			Progetto(id),
	check(inizio<fine)
);

create table AttivitaProgetto(
	id PosInteger not null,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,
	PRIMARY KEY(id),
	foreign key(persona)
		references
			Persona(id),
	foreign key(progetto,wp)
		references
			WP(progetto,id)
);

create table AttivitaNonProgettuale(
	id PosInteger PRIMARY KEY,
	persona PosInteger not null,
	tipo LavoroNonProgettuale not null,
	giorno date not null,
	oreDurata NumeroOre not null,
	foreign key(persona)
		references
			Persona(id)
);

create table Assenza(
	id PosInteger PRIMARY KEY,
	persona PosInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,
	unique(persona,giorno),
	foreign key(persona)
		references
			Persona(id)
);