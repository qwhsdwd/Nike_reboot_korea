from config import *

host='www.quweihao.com'
username='root'
password='99U6UkAbe4akuRjM'
db_name='my_databases'
port=32768

query_table_sql="""
SELECT user_name,nike_id,nike_pwd
FROM nike_account
"""


def query():

    try:
        connection = pymysql.connect(host=host,
                                     user=username,
                                     password=password,
                                     db=db_name,
                                     port=port)
    except Exception as e:
        return e

    else:
        with connection.cursor() as cursor:

            cursor.execute(query_table_sql)
            results = cursor.fetchall()
            connection.close()
            return results

