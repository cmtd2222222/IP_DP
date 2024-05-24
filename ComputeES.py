# -*- coding: utf-8 -*-
import math
from collections import defaultdict

def CalLskForOneRelationQ1(delete_id,k,from_to_relations):
    relations = from_to_relations
    if(delete_id==0):
        return 0
    elif(delete_id == 1):
        return (relations[0][1])*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k)
    elif(delete_id == 2):
        return (relations[0][1])*(relations[1][2]+k)*(relations[3][2]+k)*(relations[4][3]+k)
    elif(delete_id == 3):
        return (relations[0][1]) * (relations[1][2] + k)*(relations[2][3] + k)*(relations[4][3]+k)
    else:
        return (relations[0][1]) * (relations[1][2] + k) * (relations[2][3] + k) * (relations[3][4] + k)


def CalLskForOneRelationQ2(delete_id,k,from_to_relations):
    relations = from_to_relations
    if(delete_id==0):
        return 0
    elif(delete_id == 1):
        return (relations[0][1])*(relations[2][1]+k)*(relations[3][1]+k)*(relations[4][3]+k)
    elif(delete_id == 2):
        return (relations[0][1])*(relations[1][2]+k)*(relations[3][1]+k)*(relations[4][3]+k)
    elif(delete_id == 3):
        return (relations[0][1])* (relations[1][3] + k)*(relations[2][1]+k)*(relations[4][3]+k)
    else: 
        return (relations[0][1])* (relations[1][3] + k)*(relations[2][1]+k)*(relations[3][4]+k)


def CalLsk(k,query_id,n,from_to_relations):
    res = 0
    t_res = 0
    for i in range(0, n):
        if query_id=='1':
            t_res = CalLskForOneRelationQ1(i,k,from_to_relations)
        elif query_id=='2':
            t_res = CalLskForOneRelationQ2(i,k,from_to_relations)
        if(t_res>res):
            res = t_res
    return res




if __name__ == "__main__":
   for query_id in ['1','2']:
        from_to_relations = defaultdict(lambda: defaultdict(int))
        mf_output_path = "query/query_result/mf_Q"+query_id+".txt"
        with open(mf_output_path,'r') as f:
            for line in f.readlines():
                values = [int(num) for num in line.split()]
                from_to_relations[values[0]][values[1]] = values[2]
        
        beta = 0.01
        n = 5
        max_res_at_k = 0
        max_res = 0
        max_k = int(n/beta)
        for k in range(0, max_k+1):
            max_res_at_k = CalLsk(k,query_id,n,from_to_relations)*math.exp(-k*beta)
            if(max_res_at_k>max_res):
                max_res = max_res_at_k
        res = max_res
        print('Q{}:{}'.format(query_id,res))