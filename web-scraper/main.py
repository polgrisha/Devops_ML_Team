import argparse
import errno
import os

import pandas as pd

from metrics.preprocessor import Preprocessor
from scraper import Scraper


def ask_user(question: str) -> bool:
    '''
    Функция взаимодествия с пользователем.
    question --- строка вопроса к пользователю.
    Возвращает --- bool (ответ пользоватля - да/нет)
    '''

    response = input(question + ' y/n' + '\n')
    return response == 'y'


def create_file(path: str) -> None:
    '''
    Функция создания выходного файла
    path --- путь к файлу.
    '''

    response = False
    try:
        os.makedirs(path, mode=0o777)
    except OSError as error:
        # если файл существует, то спросить пользователя, иначе - проборосить исключение
        if error.errno != errno.EEXIST:
            raise
        response = ask_user('File already exists, replace?')
        if response:
            with open(path, 'wb') as file:
                file.close()

# def process_output(df: pd.DataFrame, drop_empty: bool=True) -> pd.DataFrame:
#     data = df.copy()
#     data = data.reset_index(drop=True)
#     if drop_empty:
#         columns = list(data.columns[1:])
#         columns.remove('title')
#         columns.remove('image_source')
#         print(columns)
#         data = data.dropna(how='all', subset=columns)
#         data = data.reset_index(drop=True)

#         print(data.iloc[7, :].values)

#     preprocessor = Preprocessor('default')

#     for i in range(data.shape[0]):
#         data.loc[i, 'phone'] = preprocessor._phone_number_preproc(data.loc[i, 'phone'])

#     return data




if __name__ == "__main__":
    # парсинг аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Parsing data from given sites')

    # Путь к входной excel таблице, содержащей колонку 'Сайт'
    parser.add_argument('input', type=str, help='Input data with urls column\
     named \"Сайт\"')

    # Путь к выходной csv таблице
    parser.add_argument('output', type=str, help='Filename for output data')

    # Задание токена vk_api
    parser.add_argument(
        '-t',
        '--vk_token',
        default='',
        help='VK token for parsing data from https://vk.com/'
    )

    parser.add_argument(
        '-c',
        '--url_column',
        default='',
        help='Name of the column with urls'
    )

    args = parser.parse_args()

    if not args.url_column:
        args.url_column = 'Сайт'

    # чтение данных

    if 'xls' in args.input:
        data = pd.read_excel(args.input)
    else:
        data = pd.read_csv(args.input)

    reject = ['youtube', 'twitter', 'wiki', 'zoom',
              'kudago', 't.me', 'telegram', 'adidas',
              'sportmaster', 'nike', 'sports.ru', 'otzovik',
              'kinopoisk', 'aeroflot']

    # Инициализация парсера
    scraper = Scraper(data=data.iloc[400:600, :].reset_index(drop=True).copy(), reject=reject,
                      vk_token=args.vk_token, url_column_name=args.url_column)

    # Запуск парсера
    scraper.inspect()

    # Вывод результатов
    output_df = scraper.process_output()
    #output_df = process_output(output_df)

    create_file(args.output)
    output_df.to_csv(args.output)
