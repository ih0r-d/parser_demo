url2 = 'https://lviv.hh.ua/search/vacancy?text=python&area=115&page=0'
url3 = 'https://hh.ru/search/vacancy?text=python&page=2'
url = 'https://hh.ru/search/vacancy?'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/35.0.1916.47 Safari/537.36 '

headers = {'accept': '*/*', 'user-agent': user_agent}

# type_of_parser='html.parser'
type_of_parser = 'lxml'
