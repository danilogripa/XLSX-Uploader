# Import pandas
import pandas as pd
import request

cols = ['os', 'ag', 'type', 'key', 'tg', 'af']


def read_excel(path: str = "static/files/Template.xlsx") -> object:
    excel_data = pd.read_excel(path)
    data = pd.DataFrame(excel_data, columns=cols)
    return data


def write_excel(data2: object, path: str = "static/files/Template2.xlsx"):
    df = pd.DataFrame(data2)
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()


data = read_excel()
data["Link"] = request.send(data['os'][0], data['ag'][0], data['type'][0], data['key'][0], data['tg'][0], data['af'][0])
write_excel(data, "static/files/Template2.xlsx")
print(data)
