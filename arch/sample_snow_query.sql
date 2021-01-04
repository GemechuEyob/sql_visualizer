create table test_table(
    id  number(30, 0)
);

create table test_table2(
    id number(30, 0)
);

insert into test_table values(1);
insert into test_table2 values(1);


select * from test_table;
select id from test_table;
select a.*, b.* from test_table a inner join test_table2 b on a.id = b.id;


