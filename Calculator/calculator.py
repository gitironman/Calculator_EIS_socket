#! usr/bin/env python
# -*- coding: utf-8 -*-
# __author: iamironman
# @file: calculator.py
# @time: 2019年02月12日
# @email: 875674794@qq.com

import re


def mul_div(ret_exp):
    if '*' in ret_exp:
        x, y = ret_exp.split('*')
        return float(x) * float(y)
    elif '/' in ret_exp:
        x, y = ret_exp.split('/')
        return float(x) / float(y)


def add_sub(no_bracket_exp):
    ret_lis = re.findall('[-+]?\d+(?:\.\d+)?', no_bracket_exp)  # ?: 取消分组优先
    ret_sum = sum([float(i) for i in ret_lis])
    return ret_sum


def exp_format(exp):
    exp = exp.replace('++', '+')
    exp = exp.replace('+-', '-')
    exp = exp.replace('--', '+')
    exp = exp.replace('-+', '-')
    return exp


def cal(no_bracket_exp):
    while 1:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', no_bracket_exp)
        if ret:
            ret_exp = ret.group()
            res_str = str(mul_div(ret_exp))
            no_bracket_exp = no_bracket_exp.replace(ret_exp, res_str)
        else:
            break
    no_bracket_exp = exp_format(no_bracket_exp)
    ret_add_sub = add_sub(no_bracket_exp)
    return ret_add_sub


def main(exp):
    exp = exp.replace(' ', '')  # 1-2*((60-30+(9-2*5/3+7/3*99/4*2998+10*568/14))*(-40/5)-(-4*3)/(16-3*2))
    while 1:
        ret = re.search('\([^()]+\)', exp)
        if ret:
            no_bracket_exp = ret.group()
            ret = str(cal(no_bracket_exp))
            exp = exp.replace(no_bracket_exp, ret)
        else:
            break
    return cal(exp)


if __name__ == '__main__':
    exp_input = input('>>>')
    res = main(exp_input)
    print(res)

# '1 - 2 * ((60 - 30 + (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) * (-40 / 5) - (-4 * 3) / (16 - 3 * 2))'
