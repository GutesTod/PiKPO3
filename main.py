from processor.dataprocessor_service import DataProcessorService


"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""


if __name__ == '__main__':
    # Без указания полного пути, программа будет читать файл из своей корневой папки
    DataProcessorService("SYB65_230_202209_GDP and GDP Per Capita.csv").run_service()
