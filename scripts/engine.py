from snowflake_models import *
import logging

class Engine:
    def __init__(self, query_str, logger):
        self.logger = logger

        logger.info("cleaning up the query string...")
        query_str = query_str.strip()
        query_tmp_lst = query_str.split(';')
        query_lst=[]
        for query in query_tmp_lst:
            query = query.strip().replace('\n','')
            if query not in ['', ' ']:
                query_lst.append(query)
        
        logger.info("number of queries found: {}".format(len(query_lst)))
        for query in query_lst:
            logger.info(query)

        self.query_lst = query_lst
    
    def fit_in_model(self):
        logger = self.logger
        query_model_lst = []

        for query in self.query_lst:
            # get the first word
            first_word = query.split(' ')[0].strip().lower()
            if first_word in ['with','select']:
                query_model_lst.append(SelectModel(query, logger))
            else:
                pass

        logger.info('total models created based on the query given: {}'.format(len(query_model_lst)))
        self.query_model_lst = query_model_lst

if __name__ == "__main__":
    # open sample query file 
    fp  = open('../docs/sample_query.sql', 'r')
    query = fp.read()

    engine_logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s %(module)s [%(levelname)s]: %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    engine_logger.addHandler(ch)
    engine_logger.setLevel(logging.INFO)

    engine_obj = Engine(query, engine_logger)
    engine_obj.fit_in_model()
    
    
