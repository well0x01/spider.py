import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def spider(url, depth):
    # Verifica a profundidade máxima alcançada
    if depth == 0:
        return

    try:
        # Faz o request à URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrai todos os links da página
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            # Junta a URL base com o link extraído
            absolute_url = urljoin(url, href)
            print(absolute_url)

            # Chama a função de spider recursivamente para a URL extraída
            spider(absolute_url, depth - 1)

    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

# Define a URL inicial e a profundidade máxima de busca
starting_url = 'https://example.com'
max_depth = 2

# Chama a função de spider com a URL inicial e a profundidade máxima
spider(starting_url, max_depth)
