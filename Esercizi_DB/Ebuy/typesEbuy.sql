create domain stringa as varchar;

create domain Voto as integer
	check (value BETWEEN 0 and 5);

create domain IntG1 as integer
	check(value>1);

create domain IntG2 as integer
	check(value>2)

create domain URL as varchar
	check(value ~ '...')

create domain RealGez as real
	check(value>=0);

create domain RealGZ as real
	check(value>0);

create domain IntGez as integer
	check(value>=0);

create type condizione as enum ('Ottimo','Buono','Discreto','Da sistemare');

create type Popolarita as enum ('Bassa','Media','Alta');