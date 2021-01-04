import sqlparse
query='''select a.*, b.* from test_table a inner join test_table2 b on a.id = b.id;
;  

;
with test_with as (
    select * from test_table
)

select * from test_with;
'''

obj = sqlparse.parse(query)
print("length of parsed object : {}".format(len(obj)))
print("type of parsed object: {}".format(type(obj)))
print("statement types...")
ind = 0
for o in obj:
    print("object #{}".format(str(ind)))
    print("statment type{}".format(o.get_type()))
    print("object type{}".format(type(o)))
    print("tokens found")
    for t in o.tokens:
        print("     {}".format(str(t)))
    ind += 1

