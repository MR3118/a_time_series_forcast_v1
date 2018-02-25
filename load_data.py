import pandas as pd
from 示范区预测系统.errors import VoidSheetError


def load_sheet(file_path='datas\所用数据.xlsx'):
    data = pd.read_excel(file_path, sheet_name=None)
    sheets = list(data.keys())
    if len(sheets) == 0:
        raise VoidSheetError('excel为空，请检查所用表格的有效性')
    print('共有%d个表，分别为%s' % (len(sheets), sheets))
    for sheet in sheets:
        try:
            print('\n表“%s”的数据概览\n' % sheet, data[sheet].describe())
        except ValueError:
            print('\n表“%s”可能无效,已自动忽略，请检查是否存在无用表或空表，并删除或修改这些表\n' % sheet)
    return data


if __name__ == '__main__':
    df = load_sheet()
    print(list(df.keys()))
