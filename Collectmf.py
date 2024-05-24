# -*- coding: utf-8 -*-
import mysql.connector

from_to_relations = []
mfs = []


def SolveQ1():
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    
    
    
def SolveQ2():
    from_to_relations.append([0,1])
    from_to_relations.append([1,2])
    from_to_relations.append([1,0])
    from_to_relations.append([1,3])
    from_to_relations.append([2,1])
    from_to_relations.append([3,1])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    
    
    
def main():
    for query_id in ['1','2']:
        query_path = "query/Q"+query_id+"_mf.sh"
        mf_output_path = "query/query_result/mf_Q"+query_id+".txt"
            
        database_name = 'dp'
        database_user = 'xxxxxx'
        database_password = 'xxxxxxx'

        con = mysql.connector.connect(user=database_user,password=database_password,database=database_name)
        cur = con.cursor()
        with open(query_path,'r') as queries:
            if query_id=="1":
                SolveQ1()
            if query_id=="2":
                SolveQ2()
            query= "" 
            for line in queries.readlines():
                query = query+line
                if ";" in query:
                    query = query.replace('\n'," ")
                    cur.execute(query)
                    query= ""
                    mf = cur.fetchone()
                    mf = int(mf[0])
                    mfs.append(mf)
            con.commit()
            con.close() 


        with open(mf_output_path,'w') as mf_results:
            for i in range(len(from_to_relations)):
                from_to = from_to_relations[i]
                mf = mfs[i]
                mf_results.write(str(from_to[0])+" "+str(from_to[1])+" "+str(mf)+"\n")
    
       

