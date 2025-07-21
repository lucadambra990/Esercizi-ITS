create type CodiceVolo as Varchar
        check(value=^[A-Za-z0-9]{2}[0-9]{4}$);

create type CodiceIATA as varchar
        check(value=^[A-Za-z]{2}$);

create domain IntegerGZ as integer
check(value>0 and value is not null);

create domain IntegerG1900 as integer
check(value>19000 and value is not null);

create domain IntegerGEZ as integer
check(value>=0 and value is not null);

create table volo(
        codice CodiceVolo primary key,
        durata_minuti IntegerGZ
);

create table aereporto(
        nome varchar not null,
        codice CodiceIATA primary key
);

create table partenza_arrivo(
        id integer primary key,
        cod_aereoporto integer not null,
        cod_volo integer not null,
        unique(cod_aereoporto,cod_volo),
        foreign key (cod_aereoporto)
                references aereporto(codice),
        foreign key (cod_volo)
                references volo(codice)
);

create table compagnia(
        nome varchar primary key,
        fondazione IntegerG1900
);

create table citta(
        nome varchar primary key,
        n_abitanti IntegerGEZ
);

create table comp_citta(
        id integer primary key,
        city varchar not null,
        foreign key(city)
                references citta(nome)
);


create table nazione(
        nome varchar primary key,
        citta varchar not null,
        -- accorpo cit_naz
        foreign key(citta)
                references citta(nome)
);

