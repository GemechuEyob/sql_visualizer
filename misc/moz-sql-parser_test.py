from moz_sql_parser import parse


query='''select a.*, b.* from test_table a inner join test_table2 b on a.id = b.id;

with test_with as (
    select * from test_table
)

select * from test_with;
'''
print(parse(query))