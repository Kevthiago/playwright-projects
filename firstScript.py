from playwright.sync_api import sync_playwright
import time

# O with é usado para garantir que os recursos sejam liberados corretamente após o uso
with sync_playwright() as p:

    navegador = p.chromium.launch(headless=False)  # Inicia o navegador em modo não headless para visualização

    pagina = navegador.new_page()  # Abre uma nova página

    pagina.goto("https://www.youtube.com")  # Navega para o site do Google

    # Como preencher um formulário? Seja para login, cadastro ou qualquer outro tipo de formulário, o processo é semelhante. Você precisa identificar os campos do formulário e usar os métodos apropriados para preencher esses campos.
    pagina.fill('xpath=/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/div/form/input', 'Python')  # Preenche o campo de pesquisa da página do YouTube
    pagina.locator('xpath=/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/button').click()  # Clica no botão de pesquisa

    time.sleep(20)  # Aguarda 20 segundos para que a página carregue completamente