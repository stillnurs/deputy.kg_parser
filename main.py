import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table', class_= 'table').find_all('td')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'http://kenesh.kg' + a
        links.append(link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('h3',class_='deputy-name').text.strip()

    except:
        name = ''

    try:
        number = soup.find('p',class_='mb-10').text.strip()
    
    except:
        number = ''
    try:
        bio = soup.find('div',id='biography').text.strip()
    except:
        bio = ''
    data = {'name':name,'number':number,'bio':bio}

    return data

def write_csv(data, encoding='utf-8'):
    with open('deputy.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],data['number'],data['bio']))
        print(data['name'],'parsed')


def main():
    url1 = 'http://kenesh.kg/ru/deputy/list/35'
    all_links = get_all_links(get_html(url1))
    for url2 in all_links:
        html = get_html(url2)
        data = get_page_data(html)
        write_csv(data)



if __name__ == '__main__':
    main()