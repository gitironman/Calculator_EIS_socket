#! usr/bin/env python
# -*- coding: utf-8 -*-
# __author: iamironman
# @file: employee_info_sheet.py
# @time: 2019年02月13日
# @email: 875674794@qq.com

flag0 = 0


def wrapper(func):
    def inner(*args, **kwargs):
        if flag0:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('请先登录。')

    return inner


def read_file():
    with open('employee_info', encoding='utf-8') as f1:
        for line in f1:
            line_list = line.strip().split(',')
            yield line_list


def format_sql(sql):
    sql = sql.replace('select', '')
    sql = sql.replace(' ', '')  # 'name,agewhereage>20'
    col, con = sql.split('where')  # name,age age>20
    if '*' in sql:
        col_lst = next(read_file())
    else:
        col_lst = col.split(',')
    return col_lst, con


def show(con, col_lst, sym, condition):
    iterator = read_file()
    name_lst = next(iterator)
    con_name, con_value = con.split(sym)  # age 22
    for line_lst in iterator:
        num = name_lst.index(con_name)
        if eval(condition):
            for col in col_lst:
                print(line_lst[name_lst.index(col)], end=' ')
            print()


@wrapper
def select():
    sql = input('sql: >>>')
    # sql = 'select name, age where age>22'
    # sql = 'select * where job=IT'
    # sql = 'select * where phone like 133'
    col_lst, con = format_sql(sql)  # ['name', 'age'] age>22

    if '>' in con:
        show(con, col_lst, '>', 'int(line_lst[num]) > int(con_value)')
    if '<' in con:
        show(con, col_lst, '<', 'int(line_lst[num]) < int(con_value)')
    if '=' in con:
        show(con, col_lst, '=', 'line_lst[num] == con_value')
    if 'like' in con:
        show(con, col_lst, 'like', 'con_value in line_lst[num]')


@wrapper
def set_info():
    sql = input('sql: >>>')
    # sql = "set name = ironman , age = 27 where name = 4"
    sql = sql.replace('set', '')
    sql = sql.replace(' ', '')
    col, con = sql.split('where')  # 'name=ironman,age=27'  'name=4'
    col_lst = col.split(',')
    iterator = read_file()
    name_lst = next(iterator)
    con_name, con_value = con.split('=')  # name 4
    con_num = name_lst.index(con_name)
    for line_lst in iterator:
        try:
            var = line_lst[con_num]
        except IndexError:
            pass
        else:
            if var == con_value:
                for col1 in col_lst:
                    col_name, col_value = col1.split('=')  # name ironman
                    col_num = name_lst.index(col_name)
                    line1 = ','.join(line_lst) + '\n'
                    line_lst[col_num] = col_value
                    line2 = ','.join(line_lst) + '\n'
                    with open('employee_info', encoding='utf-8') as f1:
                        content = f1.read()
                    content2 = content.replace(line1, line2)
                    with open('employee_info', encoding='utf-8', mode='w') as f2:
                        f2.write(content2)


@wrapper
def add():
    flag = True
    while flag:
        count = 1
        f2 = open('employee_info', encoding='utf-8', mode='r')
        line_f2_1 = f2.readline()
        list_f2 = f2.readlines()
        f2.close()
        username = input('请输入姓名，输入q/Q退出：').strip()
        if username.upper() == 'Q':
            break
        else:
            userage = input('请输入年龄：').strip()
            userphone = input('请输入电话：').strip()
            userjob = input('请输入工作：').strip()
            f3 = open('employee_info', encoding='utf-8', mode='w')
            for i in range(len(list_f2) + 1):
                content = '{},{},{},{},{}\n'.format(str(count), username, userage, userphone, userjob)
                if i == len(list_f2):
                    list_f2.append(content)
                    break
                elif str(count) == list_f2[i][:len(str(count))]:
                    pass
                else:
                    list_f2.insert(count - 1, content)
                    break
                count += 1
            f3.write(line_f2_1)
            for line_f3 in list_f2:
                f3.write(line_f3)
            f3.close()


@wrapper
def delete():
    flag = True
    while flag:
        f2 = open('employee_info', encoding='utf-8', mode='r')
        line_f2_1 = f2.readline()
        print(line_f2_1.strip())
        list_f2 = f2.readlines()
        for line_f2 in list_f2:
            print(line_f2.strip())
        f2.close()
        f2_choice = input('请输入序号进行删除,输入Q/q退出：').strip()
        if f2_choice.isdigit():
            f3 = open('employee_info', encoding='utf-8', mode='w')
            count = 0
            list_f3 = []
            for line_f2 in list_f2:
                if f2_choice == line_f2[:len(f2_choice)]:
                    pass
                else:
                    list_f3.append(line_f2)
                count += 1
            f3.write(line_f2_1)
            for line_f3 in list_f3:
                f3.write(line_f3)
            f3.close()
        elif f2_choice.upper() == 'Q':
            flag = False
        else:
            print('请输入数字！')


def login():
    usr = input('username:').strip()
    pwd = input('password:').strip()
    with open('user_info') as f1:
        for line in f1:
            line_list = line.strip().split(',')
            usr1, pwd1 = line_list[0], line_list[1]
            if usr == usr1 and pwd == pwd1:
                global flag0
                flag0 = 1
                print('登录成功。')
                break
        else:
            print('登录失败')


def logout():
    print('已退出')
    global flag0
    flag0 = 0
    exit()


operate_list = [
    ('登录', login),
    ('创建', add),
    ('删除', delete),
    ('查询', select),
    ('更改', set_info),
    ('退出', logout),
]


def main():
    print('欢迎进入员工信息表界面。')
    print(*['\n{}:{}'.format(operate_list.index(i) + 1, i[0]) for i in operate_list])
    choice = input('请输入序号：').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice in [i for i in range(len(operate_list) + 1)]:
            operate_list[choice - 1][1]()
        else:
            print('超出范围。')
    else:
        print('非法输入。')


if __name__ == '__main__':
    while 1:
        main()
