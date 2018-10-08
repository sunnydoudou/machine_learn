# -*- coding: utf-8 -*-
#author:dbuging
import math

string_value = [["js","py","sj","py","dk","java","js","py"],
                ["sj","sj","df","dk","py","ks","js","c++","go"],
                ["js","df","df","kg","py","dk","java"]]

def tfidf(string_value,n):
    idf ,total= {},0
    #idf
    for row_value in string_value:
        row_world = set(row_value)
        for world in row_world:
            idf[world] = idf.get(world,0) + 1
        total += 1
    idf["total"] = idf.get("total",0) + total
    for key,value in idf.items():
        idf[key] = math.log2(idf["total"]/(idf[key]+1))

    # tf
    tf_value = {}
    for row_index in string_value:
        total_value = len(row_index)
        tf_val = {val:row_index.count(val)/total_value for val in set(row_index)}
        for keys in tf_val.items():
            tf_value[keys[0]]=keys[1]*idf.get(keys[0])
        list1 = sorted(tf_value.items(), key=lambda x: x[1],reverse=True)
        values = [ val1[0] for val1 in list1]
        print(values[:n])

tfidf(string_value,5)







