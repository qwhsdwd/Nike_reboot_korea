import pymysql
import time

start=time.time()

host='www.zaihansheng.com'
username='root'
password='99U6UkAbe4akuRjM'
db_name='nike_shoes'

query_table_sql="""
SELECT shoes_ArtNo
FROM article_number_shoes
"""

connection=pymysql.connect(host=host,
                           user=username,
                           password=password,
                           db=db_name)

try:
    with connection.cursor() as cursor:

        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        shoes_size_list=[]
        for row in results:
            shoes_size_list.append(row[0])


finally:
    connection.close()

print("数据库处理共耗时 %.3f"%(time.time()-start))
