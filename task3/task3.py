# Импорт библиотек для корректной работы с файлами json
import json
import os
import sys

# Создание класса по парсированию json
class ReportJS:
    def __init__(self,tests,values):
        self.tests = tests
        self.values = values
        self.r = {}
    # Создания файла report.json
    def main_psr(self):
        test = rd_js(self.tests)
        value = rd_js(self.values)
        self.json_psr(value)
        self.json_psr(test, True)
        rep_js = json.dumps(test, indent=4)
        with open(f'{os.getcwd()}/report.json', 'w') as f:
            f.write(rep_js)
        return
    # Парсирование json
    def json_psr(self,data,write = False):
        if isinstance (data,dict):
            for item in data:
                if isinstance (data.get(item), list):
                    for i in data.get(item):
                        if not write:
                            self.ins_value(i)
                            if i.get('values'):
                                self.json_psr(i['values'], write)
                        elif write:
                            self.json_wr(i)
                            if i.get('values'):
                                self.json_psr(i['values'], write)
        elif isinstance (data, list):
            for d in data:
                if not write:
                    self.ins_value(d)
                elif write:
                    self.json_wr(d)
                self.json_psr(d, write)
    # Установки значений
    def ins_value(self,direct):
        id = direct.get('id')
        value = direct.get('value')
        self.r[id] = value
    # Запись значений
    def json_wr(self,direct):
        direct['value'] = self.r.get(direct['id'])
# Загрузка файлов json
def rd_js(fl_rpt):
    with open(fl_rpt, 'r', encoding = 'utf-8') as f:
        fl_rpt = json.load(f)
    return fl_rpt
# Запуск программы
if __name__ == '__main__':
    # Указываем файл tests.json
    tests = sys.argv[1]
    # Указываем файл values.json
    values = sys.argv[2]
    parse = ReportJS(tests,values)
    parse.main_psr()
    print('Файл report.json создан!')
