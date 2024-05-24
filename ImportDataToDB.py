# -*- coding: utf-8 -*-
import mysql.connector
from distutils.dir_util import copy_tree

def import2DB():
    database_name = 'dp'
    database_user = 'xxxxxxx'
    database_password = 'xxxxxxxx'
    shell_path = "dss/"
    data_path = "TPC-H/"
    mysql_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'

    con = mysql.connector.connect(user=database_user,password=database_password,database=database_name)
    cur = con.cursor()

    with open(shell_path+"TPCH_dss.ddl",'r') as ddl:
        code = ""
        for line in ddl.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
                

    with open(shell_path+"TPCH_import.sh",'r') as import_data:
        copy_tree(data_path, mysql_path)
        code = ""
        for line in import_data.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                code = code.replace('$$$/',mysql_path)
                cur.execute(code)
                code = ""
                

    with open(shell_path+"TPCH_dss.ri",'r') as ri:
        code = ""
        for line in ri.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
                

    con.commit()
    con.close()
    
    
    