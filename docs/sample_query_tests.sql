select * from xyzzy where z > 100
        select * from xyzzy where z > 100 order by zz
        select * from xyzzy
        select z.* from xyzzy
        select a, b from test_table where 1=1 and b='yes'
        select a, b from test_table where 1=1 and b in (select bb from foo)
        select z.a, b from test_table where 1=1 and b in (select bb from foo)
        select z.a, b from test_table where 1=1 and b in (select bb from foo) order by b,c desc,d
        select z.a, b from test_table left join test2_table where 1=1 and b in (select bb from foo)
        select a, db.table.b as BBB from db.table where 1=1 and BBB='yes'
        select a, db.table.b as BBB from test_table,db.table where 1=1 and BBB='yes'
        select a, db.table.b as BBB from test_table,db.table where 1=1 and BBB='yes' limit 50
        select a, b from test_table where (1=1 or 2=3) and b='yes' group by zx having b=2 order by 1
        SELECT emp.ename as e FROM scott.employee as emp
        SELECT ename as e, fname as f FROM scott.employee as emp
        SELECT emp.eid, fname,lname FROM scott.employee as emp
        SELECT ename, lname, emp.eid FROM scott.employee as emp
        select emp.salary * (1.0 + emp.bonus) as salary_plus_bonus from scott.employee as emp
        SELECT * FROM abcd WHERE (ST_Overlaps("GEOM", 'POINT(0 0)'))
        SELECT * FROM abcd WHERE CAST(foo AS REAL) > -999.123
        SELECT * FROM abcd WHERE bar BETWEEN +180 AND +10E9
        SELECT * FROM abcd WHERE CAST(foo AS REAL) < (4 + -9.876E-4)
        SELECT SomeFunc(99)
        SELECT * FROM abcd WHERE ST_X(ST_Centroid(geom)) BETWEEN (-180*2) AND (180*2)
        SELECT * FROM abcd WHERE a
        SELECT * FROM abcd WHERE snowy_things REGEXP '[⛄️☃️☃🎿🏂🌨❄️⛷🏔🗻❄︎❆❅]'
        SELECT * FROM abcd WHERE a."b" IN 4
        SELECT * FROM abcd WHERE a."b" In ('4')
        SELECT * FROM "a".b AS "E" WHERE "E"."C" >= CURRENT_Time
        SELECT * FROM abcd WHERE "dave" != "Dave" -- names & things ☃️
        SELECT * FROM a WHERE a.dave is not null
        SELECT * FROM abcd WHERE pete == FALSE or peter is true
        SELECT * FROM abcd WHERE a >= 10 * (2 + 3)
        SELECT * FROM abcd WHERE frank = 'is ''scary'''
        SELECT * FROM abcd WHERE "identifier with ""quotes"" and a trailing space " IS NOT FALSE
        SELECT * FROM abcd WHERE blobby == x'C0FFEE'  -- hex
        SELECT * FROM abcd WHERE ff NOT IN (1,2,4,5)
        SELECT * FROM abcd WHERE ff not between 3 and 9
        SELECT * FROM abcd WHERE ff not like 'bob%'