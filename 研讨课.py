table_size=13
hash_table=[[] for _ in range(table_size)]
collision_cnt=0

def hash_func(key,table_size):
    idx=int(key.split('-')[1])
    return idx%table_size

def insert(key,value,hash_table):
    idx=hash_func(key)
    if hash_table[idx]:
        global collision_cnt
        #只有在变量被赋值时需声明,如果只是调用读取或者修改可变对象的内容(list,dict)
        #如果不声明,python会默认未初始化
        collision_cnt+=1
    hash_table[idx].append((key,value))
"""
insert("S-042",28.1)
insert("S-055",26.5)
"""

def insert_probe(key,value,hash_table,table_size):
    idx=hash_func(key)
    while hash_table[idx]:
        idx=(idx+1)%table_size
    hash_table[idx]=(key,value)

def string_hash_func(key,table_size):
    total=0
    for ch in key:
        total+=ord(ch)
    #ord() A->65  chr() 65->A
    return total%table_size
    
insert_probe("S-042",28.1)
insert_probe("S-055",26.5)
print(hash_table)
