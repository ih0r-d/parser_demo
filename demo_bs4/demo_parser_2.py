import csv

import requests as req

from demo_bs4.response import Vacancy
from demo_bs4.props import url, type_of_parser
from demo_bs4.props import headers
from bs4 import BeautifulSoup as bs


def get_session(base_url, accept_headers):
    session = req.Session()
    r = session.get(base_url, headers=accept_headers)
    if r.status_code == 200:
        soup = bs(r.content, type_of_parser)
    else:
        soup = None
    return soup


def get_vacancies_by_page(base_url):
    vacancies = []
    page = get_session(base_url, headers)
    divs_on_page = page.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
    for div in divs_on_page:
        try:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            responsibility = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            requirements = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text

            vacancy = Vacancy(title, href, company, responsibility, requirements)
            vacancies.append(vacancy)

        except:
            pass
    return vacancies


def parse_all_pages(text):
    session = get_session(f'{url}text={text}&page=0', headers)
    all_vacancies = []
    try:
        pagination = session.find_all('a', attrs={'data-qa': 'pager-page'})
    except:
        pass

    for i in range(int(pagination[-1].text)):
        current_url = f'{url}text={text}&page={i}'
        vacancies_on_page = get_vacancies_by_page(current_url)
        print("Parsed {} vacancies on {} page".format(len(vacancies_on_page), i))
        if vacancies_on_page not in all_vacancies:
            all_vacancies.append(vacancies_on_page)
    return all_vacancies


def write_csv(name, text):
    with open(name, 'w') as file:
        doc = csv.writer(file)
        doc.writerow(('Вакансія', 'URL', 'Компанія', 'Опис вакансії', 'Вимоги'))
        for page in parse_all_pages(text):
            for v in page:
                doc.writerow((v.title, v.href, v.company, v.responsibility, v.requirements))


if __name__ == '__main__':
    # get_vacancies_by_page(url)
    write_csv('python_lits.csv', 'python')
