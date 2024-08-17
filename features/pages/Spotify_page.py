from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Spotify_page(BasePage):
    CAMPO_EMAIL = (By.ID, 'login-username')
    CAMPO_SENHA = (By.ID, "login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[data-testid="login-button"]')
    BUTTON_PLAYLIST = (By.CSS_SELECTOR, 'div.wv308QWnPnkI8n0GdqYO button[data-encore-id="buttonPrimary"]')
    PLAYLIST = (By.CSS_SELECTOR, 'P.oaKRK4WllExdXORQIlFZ span')
    BOTAO_PLAYLIST = (By.CSS_SELECTOR, 'div.RowButton-sc-xxkq4e-0')
    BUSCA_MUSICA = (By.CSS_SELECTOR, 'input.FeWwGSRANj36qpOBoxdx')
    BOTAO_BUSCAR = (By.CSS_SELECTOR, 'input.NtkAQg9R1r5CjuP0XHwl') # Selecionar botão buscar
    PESQUISAR_ARTISTA = (By.CSS_SELECTOR, 'a.hNvCMxbfz7HwgzLjt3IZ')
    ADICIONAR_MUSICA = (By.CSS_SELECTOR, 'div[aria-rowindex="1"] button[data-testid="add-to-playlist-button"]')
    NOME_MUSICA = (By.CSS_SELECTOR, 'div.btE2c3IKaOXZ4VNAb8WQ') 

    def preencher_campos_login(self):
        campo_email = self.find_element(*self.CAMPO_EMAIL)
        campo_email.send_keys('Weslley3442@hotmail.com')
        campo_senha = self.find_element(*self.CAMPO_SENHA)
        campo_senha.send_keys('30305688w&Sll@y')
    
    def clicar_botao_logar(self):
        self.find_element(*self.LOGIN_BUTTON).click()

    def clicar_botao_playlist(self):
        self.wait_for_element(10,*self.BUTTON_PLAYLIST).click()

    def Verificar_se_playlist_foi_criada(self):
        campo = self.wait_for_element(10,*self.PLAYLIST)
        return campo.text
    
    def clicar_playlist(self):
        self.find_element(*self.BOTAO_PLAYLIST).click()

    def buscar_musica(self):
        self.find_element(*self.BUSCA_MUSICA).send_keys('Baby alô')

    def botao_musica(self):
        self.wait_for_element(10,*self.ADICIONAR_MUSICA).click()

    def verificar_musica(self):
        return self.find_element(*self.NOME_MUSICA).text
    
    def preencher_campos_buscar(self):
        campo = self.find_elements(*self.PESQUISAR_ARTISTA) # Pega a função criada em base_page
        campo[1].click()
        
    def clicar_botao_buscar(self):
        botao = self.find_element(*self.BOTAO_BUSCAR)
        botao.send_keys('Dua lipa')

    def clicar_botao_procurar(self):
        botao = self.find_elements(*self.PESQUISAR_ARTISTA)
        botao[1].click()

    def campo_pesquisar(self, texto):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BOTAO_BUSCAR)
        )
        campo.send_keys(texto)


class TelaInicialSpotify(BasePage):
    BOTAO_ENTRAR = (By.CSS_SELECTOR, "div[class=LKFFk88SIRC9QKKUWR5u] span")
    CAMPO_EMAIL = (By.ID, 'login-username')  
    CAMPO_SENHA = (By.ID, 'login-password')  
    BOTAO_LOGIN = (By.ID, 'login-button')    
    TEXTO_RESULTADO = (By.ID, 'listrow-title-feito-para-eitô')
    TEXTO_ERRO_LOGIN = (By.CSS_SELECTOR, '.Message-sc-15vkh7g-0.dHbxKh' )

    
    def recuperar_texto_resultado(self):
        elemento = self.find_element(*self.TEXTO_RESULTADO)
        return elemento.text
        
    def recuperar_texto_erro_login(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TEXTO_ERRO_LOGIN)
            )
            return elemento.text
        except TimeoutException:
            return "Elemento não encontrado"

        
    def verificar_redirecionamento(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TEXTO_RESULTADO)
            )
            print("Elemento encontrado na página inicial.")
            return True
        except TimeoutException:
            print("Falha ao encontrar o elemento na página inicial.")
            return False


        
    def inserir_credenciais_e_entrar(self, email, senha):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CAMPO_EMAIL)
            )
        
            campo_email = self.find_element(*self.CAMPO_EMAIL)
            campo_senha = self.find_element(*self.CAMPO_SENHA)
            email = "heitor.leander@hotmail.com"
            senha = "141720ma"
            campo_email.send_keys(email)
            campo_senha.send_keys(senha)
            self.find_element(*self.BOTAO_LOGIN).click()
    def inserir_credenciais_invalidas_e_entrar(self, email, senha):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CAMPO_EMAIL)
            )
        
            campo_email = self.find_element(*self.CAMPO_EMAIL)
            campo_senha = self.find_element(*self.CAMPO_SENHA)
            email = "heitor.leander@aspkas.com"
            senha = "2222222"
            campo_email.send_keys(email)
            campo_senha.send_keys(senha)
            self.find_element(*self.BOTAO_LOGIN).click()

    def clicar_botao_entrar(self):
        self.find_element(*self.BOTAO_ENTRAR).click()
