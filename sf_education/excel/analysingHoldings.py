import openpyxl as excl
# import writeFile, execution as e
import os

banksSummary = {}


# Есть слово банк, есть запятая, есть пробел. Первый элемент есть счет, который нам интересен
def processBank(contents):
    pass


def runAnalysis():
    # Первая клетка – компания
    book = excl.load_workbook('Alfa.xlsx')
    page = book['TDSheet']
    col_a = page['A']
    company_name = col_a[0].value
    print(company_name)
    # какие строчки рассмартривать
    # Для выбранных строчек из шага 1:
    # 1.Месяц определяется словом ‘оборот’
    # 2.Каждый месяц
    # 3.Если не мета-данные, смотрим на дебит
    # 4.Делаем общую сумму
    # 5.Делаем сумму по холдинговым компаниям

    # cохранить результат


# Определяем какие строчки рассматривать на основе колнки А
def defineTheRange(banks, col_a, companyName, paymentStartIndex):
    pass
    # если есть слово 'банк'

    # Мы начинаем смотреть на поступления начиная со строки в которой есть ‘поступлен’ и ‘продаж’
    # Мы начинаем смотреть на поступления начиная со строки в которой есть ‘поступлен’ и ‘продаж’


runAnalysis()
