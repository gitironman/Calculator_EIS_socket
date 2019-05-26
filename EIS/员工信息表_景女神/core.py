name_value = {'id':0,'name':1,'age':2,'phone':3,'job':4}
def format_sql(sql):
    sql = sql.replace('select', '')  # 'select name , age where age > 20'
    sql = sql.replace(' ', '')       # 'name,agewhereage>20'
    col, con = sql.split('where')    # col = 'name,age',con = 'age>20'
    if '*' in col:
        col_lst = name_value.keys()
    else:
        col_lst = col.split(',')     # col_lst = ['name','age']
    return col_lst,con               # col_lst = ['name','age']   con = 'age>20'

def read_file():
    with open('userinfo', encoding='utf-8') as f:
        for line in f:
            line_lst = line.strip().split(',')
            yield line_lst


def show(con,col_l,symbol,condition):
    con_name, con_value = con.split(symbol)  # con_name = 'age',con_value = 20
    for line_lst in read_file():
        num = name_value[con_name]  # num = 2
        if eval(condition):
            for col in col_l:  # ['name','age']
                print(line_lst[name_value[col]], end=' ')
            print()

def select(sql):
    # sql = 'select name,age where age>20'
    col_l, con = format_sql(sql)   # col_l = ['name', 'age'],con = age>20
    if '>' in con:
        show(con,col_l,'>','int(con_value) < int(line_lst[num])')
    if '<' in con:
        show(con, col_l, '<', 'int(con_value) > int(line_lst[num])')
    if '=' in con:
        show(con, col_l, '=', 'con_value == line_lst[num]')
    if 'like' in con:
        show(con, col_l, 'like', 'con_value in line_lst[num]')
# sql = input('>>>').strip()
sql = 'select id,name where age > 20'
# 先判断一下是否是查操作
if sql.startswith('select'):
    # 是查找操作
    select(sql)
else:
    print('是其他操作')

# 基础
# 尽量用函数完成 :查,增,删
# 进阶需求 : 改