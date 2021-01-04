



# select * from test_table;
# select id from test_table;
# select a.*, b.* from test_table a inner join test_table2 b on a.id = b.id;
# ;  

# ;
# with test_with as (
#     select * from test_table
# )

# select * from test_with;



class SelectModel:
    def __init__(self, query, logger):
        first_word = query.split(' ')[0].strip().lower()
        if first_word in ['with']:
            self.query_model = self.resolve_with_stmt(query)
        else:
            self.query_model = self.resolve_select_stmt(query)
    
    def resolve_with_stmt(self):
        pass

    def resolve_select_stmt(self):
        pass