# -*- coding: utf-8 -*-
import xlrd
def read_excel():
    workbook = xlrd.open_workbook(r'fee.xls')

    sheet = workbook.sheet_by_name('Sheet1')
    dept = dict() # need to pay
    payed = dict()
    num2name = dict()
    for i in range(sheet.ncols):
        if i >= 2 and i < 9:
            dept[sheet.row_values(0)[i]] = 0
            payed[sheet.row_values(0)[i]] = 0
            num2name[i-1] = sheet.row_values(0)[i]

    for i in range(sheet.nrows):
        if i > 0:
            item = sheet.row_values(i)
            total = item[1]
            people_num = sum(item[2:-1])
            avg = float(total) / float(people_num)
            for j in range(len(item[2:-1])):
                if item[2 + j] == 1.0:
                    dept[num2name[j + 1]] += avg
            payed[num2name[item[-1]]] += total

    print('dept info:')
    print(dept)
    print('payed info:')
    print(payed)

    families = [['彭','沈'],['庞','李'],['张','朱'],['楼']]
    
    for family in families:
        dept_ = 0
        for x in family:
            dept_ += dept[x]
        payed_ = 0
        for x in family:
            payed_ += payed[x]
        cash_str = 'pay '
        if payed_ > dept_:
            cash_str = 'receive '
        print('and'.join(family) + ' should ' + cash_str + str(round(abs(payed_ - dept_),2)))
        


if __name__ == '__main__':
    read_excel()