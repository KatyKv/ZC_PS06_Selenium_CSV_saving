# repeating lesson

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://hh.ru/vacancies/programmist'
driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.magritte-redesign')

parsed_data = []

i = 1
for vacancy in vacancies:
    try:
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-21')
        if not link.get_attribute('href'):
            continue
        title = link.text
        vacancy_url = link.get_attribute('href')
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR,
                                          'span.magritte-text___pbpft_3-0-26.magritte-text_style-primary___AQ7MW_3-0-26.magritte-text_typography-label-1-regular___pi3R-_3-0-26')
            salary = salary.text
        except:
            salary = 'Зарплата не указана'
        company = vacancy.find_element(By.CSS_SELECTOR,
                    'span[data-qa="vacancy-serp__vacancy-employer-text"]').text

        parsed_data.append([title, company, salary, vacancy_url])

        print()
        print(i, title)
        print(salary)
        print(vacancy_url)
        print(company)

        i += 1

    except Exception as e:
        print('\nПри парсинге произошла ошибка {e}:')
        continue

driver.quit()

with open('hh_selenium.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Вакансия', 'Компания', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)

