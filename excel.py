import pandas as pd
import request

cols = ['os', 'ag', 'type', 'key', 'tg', 'af', 'Link']


def read_excel(path: str = "static/files/Template.xlsx") -> object:
    excel_data = pd.read_excel(path)
    data = pd.DataFrame(excel_data, columns=cols)
    return data


def write_excel(data: object, path: str = "static/files/Template2.xlsx"):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()


def create(path: str = "static/files/Template.xlsx"):
    data: object = read_excel(path)
    for ind in data.index:
        data["Link"][ind] = request.send(data['os'][ind], data['ag'][ind], data['type'][ind], data['key'][ind],
                                         data['tg'][ind], data['af'][ind])

    path_end = path.replace(".xlsx", "") + "_final" + ".xlsx"
    write_excel(data, path_end)
    print(data)

create()