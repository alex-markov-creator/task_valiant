# -*- coding: utf-8 -*-
"""
*.py -  file
"""
# импортируем необходимые библиотеки
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# предварительные настрйки внешнего вида графиков
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
# получаем данные в формате типа данных pandas.DataFrame из файла формата .xlsx
dataset = pd.read_excel(r'source/valiant_26948596.xlsx')  # арт. 26948596

# дополнительные наименования товаров для тестов
dataset_1 = pd.read_excel(r'source/karna_11076110.xlsx')  # арт. 11076110
dataset_2 = pd.read_excel(
    r'source/shtora_10226843_valiant.xlsx')  # арт. 10226843
dataset_3 = pd.read_excel(
    r'source/shtora_valiant_2812202.xlsx')  # арт. 2812202

# удаляем недостающие значения и применяем метод сортировки sort_values() по дате
dataset = dataset.dropna().sort_values(by='Дата')
# оставим только необходимые
cols = ['Дата', 'Остаток', 'Цена', 'Скидка', 'Цена со скидкой', 'Промокод', 'СПП', 'Цена с СПП', 'Комментариев', 'Рейтинг',
        'Остатки за сутки']
dataset = dataset.drop(cols, axis=1)
# определяем цену товара при продаже
# по данным предварительного просмотра данных,
# все продажи были осуществлены по цене со скидкой и промо,
# дополнительная информация по ценам продаж отсутствует


def cost(row):
    """
    Функция определения цены товара при продаже
    """
    try:
        return row['Сумма продаж'] / row['Продажи']
    except ZeroDivisionError:
        return row['Со скидкой и промо']


# применяем функцию подсчёта
dataset['Цена'] = dataset.apply(cost, axis=1)
# удаляем ненужную информацию
dataset = dataset.drop(['Со скидкой и промо', 'Сумма продаж'], axis=1)
# получаем данные для построения графика
dataset = dataset.groupby(['Цена'])['Продажи'].sum()
# график
dataset.plot(title='Зависимость спроса от цены (арт. 26948596)',
             grid=True, fontsize=7, legend=True)
plt.show()

# удаляем недостающие значения и применяем метод сортировки sort_values() по дате
dataset_1 = dataset_1.dropna().sort_values(by='Дата')
# оставим только необходимые
cols = ['Дата', 'Остаток', 'Цена', 'Скидка', 'Цена со скидкой', 'Промокод', 'СПП', 'Цена с СПП', 'Комментариев', 'Рейтинг',
        'Остатки за сутки']
dataset_1 = dataset_1.drop(cols, axis=1)
# определяем цену товара при продаже
# по данным предварительного просмотра данных,
# все продажи были осуществлены по цене со скидкой и промо,
# дополнительная информация по ценам продаж отсутствует


def cost(row):
    """
    Функция определения цены товара при продаже
    """
    try:
        return row['Сумма продаж'] / row['Продажи']
    except ZeroDivisionError:
        return row['Со скидкой и промо']


# применяем функцию подсчёта
dataset_1['Цена'] = dataset_1.apply(cost, axis=1)
# удаляем ненужную информацию
dataset_1 = dataset_1.drop(['Со скидкой и промо', 'Сумма продаж'], axis=1)
# получаем данные для построения графика
dataset_1 = dataset_1.groupby(['Цена'])['Продажи'].sum()
# график
dataset_1.plot(title='Зависимость спроса от цены (арт. 11076110 KARNA)',
               grid=True, fontsize=7, legend=True)
plt.show()
# удаляем недостающие значения и применяем метод сортировки sort_values() по дате
dataset_2 = dataset_2.dropna().sort_values(by='Дата')
# оставим только необходимые
cols = ['Дата', 'Остаток', 'Цена', 'Скидка', 'Цена со скидкой', 'Промокод', 'СПП', 'Цена с СПП', 'Комментариев', 'Рейтинг',
        'Остатки за сутки']
dataset_2 = dataset_2.drop(cols, axis=1)
# определяем цену товара при продаже
# по данным предварительного просмотра данных,
# все продажи были осуществлены по цене со скидкой и промо,
# дополнительная информация по ценам продаж отсутствует
plt.show()

def cost(row):
    """
    Функция определения цены товара при продаже
    """
    try:
        return row['Сумма продаж'] / row['Продажи']
    except ZeroDivisionError:
        return row['Со скидкой и промо']


# применяем функцию подсчёта
dataset_2['Цена'] = dataset_2.apply(cost, axis=1)
# удаляем ненужную информацию
dataset_2 = dataset_2.drop(['Со скидкой и промо', 'Сумма продаж'], axis=1)
# получаем данные для построения графика
dataset_2 = dataset_2.groupby(['Цена'])['Продажи'].sum()
# график
dataset_2.plot(title='Зависимость спроса от цены (арт. 10226843)',
               grid=True, fontsize=7, legend=True)
plt.show()
# удаляем недостающие значения и применяем метод сортировки sort_values() по дате
dataset_3 = dataset_3.dropna().sort_values(by='Дата')
# оставим только необходимые
cols = ['Дата', 'Остаток', 'Цена', 'Скидка', 'Цена со скидкой', 'Промокод', 'СПП', 'Цена с СПП', 'Комментариев', 'Рейтинг',
        'Остатки за сутки']
dataset_3 = dataset_3.drop(cols, axis=1)
# определяем цену товара при продаже
# по данным предварительного просмотра данных,
# все продажи были осуществлены по цене со скидкой и промо,
# дополнительная информация по ценам продаж отсутствует


def cost(row):
    """
    Функция определения цены товара при продаже
    """
    try:
        return row['Сумма продаж'] / row['Продажи']
    except ZeroDivisionError:
        return row['Со скидкой и промо']


# применяем функцию подсчёта
dataset_3['Цена'] = dataset_3.apply(cost, axis=1)
# удаляем ненужную информацию
dataset_3 = dataset_3.drop(['Со скидкой и промо', 'Сумма продаж'], axis=1)
# получаем данные для построения графика
dataset_3 = dataset_3.groupby(['Цена'])['Продажи'].sum()
# график
dataset_3.plot(title='Зависимость спроса от цены (арт. 2812202)',
               grid=True, fontsize=7, legend=True)
plt.show()
