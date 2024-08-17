from behave import given, when, then
from features.pages.Spotify_page import Spotify_page, TelaInicialSpotify
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# region Teste Criação_de_Playlist

@given(u'que o usuário está logado no Spotify')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.Spotify_page = Spotify_page(context.driver)
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()

@when(u'clicar no botão Criar playlist')
def step_impl(context):
    context.Spotify_page.clicar_botao_playlist()

@then(u'a playlist "{texto}" deve ser criada com sucesso')
def step_impl(context,texto):
    assert texto == context.Spotify_page.Verificar_se_playlist_foi_criada()


# endregion

# region Teste Adicionar_música_na_playlist

@given(u'selecionar playlist chamada "Minha playlist nº 1"')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.Spotify_page = Spotify_page(context.driver)
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.clicar_playlist()


@when(u'selecionar a opção de adicionar músicas à playlist')
def step_impl(context):
    context.Spotify_page.buscar_musica()

@when(u'eu escolho a música "Baby alô" para adicionar à playlist')
def step_impl(context):
    context.Spotify_page.botao_musica()

@then(u'a música "{texto}" deve ser adicionada com sucesso à playlist "Minha playlist nº 1"')
def step_impl(context,texto):
    time.sleep(2)
    assert texto == context.Spotify_page.verificar_musica()
    

# endregion

@given(u'que o usuário está na página inicial do Spotify')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.treinamento_page = Spotify_page(context.driver)
    context.treinamento_page.clicar_botao_procurar ()
    time.sleep(5)

@when(u'o dado "aLCIONe" for pesquisado no campo de busca')
def step_impl(context):
    context.treinamento_page.campo_pesquisar ("aLCIONe")
    time.sleep(5)


@then(u'o sistema deve ignorar a diferença entre maiúsculas e minúsculas')
def step_impl(context):
    pass


@then(u'retornar resultados relevantes para "Alcione"')
def step_impl(context):
    pass

@when(u'o dado o dado "Ivete$Sangalo# 2024!" for pesquisado no campo de busca')
def step_impl(context):
    context.treinamento_page.campo_pesquisar ("Ivete$Sangalo# 2024!")
    time.sleep(5)

@then(u'deve retornar resultados relevantes para "Ivete Sangalo"')
def step_impl(context):
    pass

@given(u'que o usuário está logado no Spotify2')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.treinamento_page = Spotify_page(context.driver)
    context.treinamento_page.clicar_botao_procurar()
    time.sleep(5)

@when(u'o usuário insere "{texto}"')
def step_impl(context, texto):
    context.treinamento_page.campo_pesquisar(texto)
    time.sleep(5)

@then(u'o resultado deve ser flexível')
def step_impl(context):
    pass

@then(u'o usuário deve ser redirecionado para a página com artistas e músicas com a inicial "D"')
def step_impl(context):
    pass

# region loginCorreto
@given(u'que o usuário está na página inicial de login do spotify')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.treinamento_page = TelaInicialSpotify(context.driver)
    context.treinamento_page.clicar_botao_entrar()


@then('o usuário é redirecionado para a página de login')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("login")
    )
    assert "login" in context.driver.current_url, "O usuário não foi redirecionado para a página de login"


@when(u'o usuário insere um e-mail válido "{email}" e uma senha válida "{senha}" e clica em entrar')
def step_impl(context, email, senha):
    context.treinamento_page.inserir_credenciais_e_entrar(email, senha)
    


@then(u'o usuário deve ser redirecionado para a página inicial do Spotify')
def step_impl(context):
    assert context.treinamento_page.verificar_redirecionamento(), "Usuário não foi redirecionado corretamente"

@then(u'a mensagem "{texto}" deverá ser exibida')
def mensagem_home(context, texto):
    valor_obtido = context.treinamento_page.recuperar_texto_resultado()
    assert texto == valor_obtido,f"Mensagem de erro:\nO texto '{texto}'\n foi diferente do esperado '{valor_obtido}'"


# endregion

#region loginInvalido
@when(u'o usuário insere um e-mail "{email}" ou uma senha "{senha}" inválida e clica em Entrar')
def step_impl(context, email, senha):
    context.treinamento_page.inserir_credenciais_invalidas_e_entrar(email, senha)

@then(u'o sistema deve exibir uma mensagem de erro informando que {texto}')
def mensagem_erro(context, texto):
    valor_obtido = context.treinamento_page.recuperar_texto_erro_login()
    texto = texto.replace('"', '')
    assert str(texto) in str(valor_obtido), f"Mensagem de erro:\nO texto {valor_obtido}\n foi diferente do es888perado {texto}"
# endregion

# region Teste Orquídea

@given(u'a página inicial de login deve estar aberta') # Clicar no botão de login
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt") #Inserir o endereço
    context.Spotify_page = Spotify_page(context.driver) # Web Driver - Tem que colocar 
    context.Spotify_page.clicar_botao_logar()


@when(u'o usuário digicar a senha no campo "E-mail ou nome de usuário"') # Digitou o e-mail e a senha
def step_impl(context):
    context.Spotify_page.preencher_campos_login()
    

@when(u'digitar a senha no campo "Senha"')
def step_impl(context):
    pass # Ignorar porque já foi preenchido no passo anterior
    #raise NotImplementedError(u'STEP: When digitar a senha no campo "Senha"')


@then(u'o usuário será direcionado à página inicial do Spotify') # Clicar no entrar e direcionado a pág inicial
def step_impl(context):
    context.Spotify_page.clicar_botao_logar()
    time.sleep(5)


@given(u'que o usuário esteja na plataforma') # Precisa fazer os passos anteriores necessários p página de login
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt") #Inserir o endereço
    context.Spotify_page = Spotify_page(context.driver) # Web Driver - Tem que colocar 
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()
    time.sleep(5)


@when(u'o usuário digita o nome do artista no campo pesquisa')
def step_impl(context):
    context.Spotify_page.preencher_campos_buscar() #Pega a função que foi criada em Spotify_page
    context.Spotify_page.clicar_botao_buscar()
    time.sleep(5)

@then(u'é mostrado ao usuário o artista desejado')
def step_impl(context):
    pass