import requests
from bs4 import BeautifulSoup

def finn_avisartikler_vg(overskrift, nettsted_url):
    responce = requests.get(nettsted_url)
    soup = BeautifulSoup(responce.text, 'html.parser')

    artikler = []

    divs = soup.find_all('div', class_='article-container')
    for div in divs:
        h2_element = div.find('h2')
        lenke_element = div.find('a')
        if h2_element is not None:
            if overskrift.lower() in h2_element.text.lower():
                artikkel_lenke = lenke_element['href']
                artikkel_tittel = h2_element.text
                artikkel = {'tittel':artikkel_tittel, 'lenke':artikkel_lenke}
                artikler.append(artikkel)

    return artikler


overskrift = 'haaland'
nettsted_url = 'https://vg.no'

funnede_artikler = finn_avisartikler_vg(overskrift, nettsted_url)

for artikkel in funnede_artikler:
    print(artikkel['tittel'])
