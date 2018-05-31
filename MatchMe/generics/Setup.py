'''
Created on 23-Apr-2018

@author: Automation
'''
import commands
import os
import xlrd

class Setup(object):

    def main():
        f=open("../test_run.bat", "w+")
        check=None
        status=None
        
        book=xlrd.open_workbook('../data/controller.xlsx')
        sheet=book.sheet_by_name('test_controller')
        
        value=sheet.cell_value(1,1)
        
        print value
        if value=='yes':
            check='complete'
        else:
            check=[]
            check1=sheet.col_values(0)
            status=sheet.col_values(1)
            
            for i in range(len(check1)):
                if status[i]=='yes':
                    check.append(check1[i])
        
        if check=='complete':
            f.write('pytest --alluredir "%CD%"\\reports\\allure-report')
            f.close()
            print 'file create complete 1'
        else:
            f.write('pytest ')
            for i in range(len(check)):
                f.write('tests/'+check[i]+'.py ')
            f.write('--alluredir "%CD%"\\reports\\allure-report')
            f.close()
            print 'file create complete 2'
            
        os.chdir("../")
        os.startfile("test_run.bat")
        print 'file execution started'
        
    def excel_controller(self):
        book=xlrd.open_workbook('../data/controller.xlsx')
        sheet=book.sheet_by_name('test_controller')
        value=sheet.cell(1,1)
        if value=='yes':
            return 'complete'
        
    if __name__=='__main__':
        main()        