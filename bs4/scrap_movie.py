from bs4 import BeautifulSoup
import requests

class MovieParser():

    def __init__(self, root_url: str):
        self.root_url = root_url

    
    def request_result(self, link: str) -> str:
        result = requests.get(link)
        content = result.text
        return content
    
    def parse_data(self) -> list:
        soup = BeautifulSoup(self.request_result(f'{root_url}/movies'), 'lxml')
        box = soup.find('article', class_='main-article')
        links = []
        for link in box.find_all('a', href=True):
            links.append(link['href'])
        
        for link in links:
            soup = BeautifulSoup(self.request_result(f'{root_url}/{link}'), 'lxml')
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)

        return links


if __name__ == '__main__':
    root_url = 'https://subslikescript.com'
    mv_parser = MovieParser(root_url)
    res = mv_parser.parse_data()
    print(res)
