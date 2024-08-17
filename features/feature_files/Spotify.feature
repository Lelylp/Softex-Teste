Funcionalidade: Playlist Spotify

    @Criação_de_Playlist
    Cenário: Criação de Playlist
        Dado que o usuário está logado no Spotify
        Quando clicar no botão Criar playlist 
        Então a playlist "Minha playlist nº 1" deve ser criada com sucesso

    @Adicionar_música_na_playlist
    Cenário: Adicionar música na playlist        
        Dado selecionar playlist chamada "Minha playlist nº 1"
        Quando selecionar a opção de adicionar músicas à playlist
        E eu escolho a música "Baby Alô" para adicionar à playlist
        Então a música "Baby Alô" deve ser adicionada com sucesso à playlist "Minha playlist nº 1"

    @TesteBuscaMaiusculaMinuscula
    Cenário: Busca com letras maiúsculas e minúsculas
        Dado que o usuário está na página inicial do Spotify
        Quando o dado "aLCIONe" for pesquisado no campo de busca
        Então o sistema deve ignorar a diferença entre maiúsculas e minúsculas
        E retornar resultados relevantes para "Alcione"

    @TesteBuscaCaracteresInesperados
    Cenário: Busca com caracteres especiais inesperados
        Dado que o usuário está na página inicial do Spotify
        Quando o dado o dado "Ivete$Sangalo# 2024!" for pesquisado no campo de busca
        Então deve retornar resultados relevantes para "Ivete Sangalo"

    @TesteBuscaFlexível
    Cenário: Digitar um termo de busca Inválido
        Dado que o usuário está logado no Spotify2
        Quando o usuário insere "123**&&abcd00"
        Então o resultado deve ser flexível 

    @TesteBuscaDeUmaLetra
    Cenário: Digitar uma letra no campo de busca
        Dado que o usuário está logado no Spotify2
        Quando o usuário insere "D"
        Então o usuário deve ser redirecionado para a página com artistas e músicas com a inicial "D"

    @loginCorreto
    Cenário: Login com credenciais válidas
        Dado que o usuário está na página inicial de login do spotify
        Quando o usuário insere um e-mail válido "usuario@exemplo.com" e uma senha válida "senhaCorreta" e clica em Entrar
        Então o usuário deve ser redirecionado para a página inicial do Spotify
        E a mensagem "Feito para eitô" deverá ser exibida

    @loginDadosInvalidos
    Cenário: Login com credenciais inválidas
       Dado que o usuário está na página inicial de login do spotify
       Quando o usuário insere um e-mail "usuario@exemplo.com" ou uma senha "senha" inválida e clica em Entrar
       Então o sistema deve exibir uma mensagem de erro informando que "Nome de usuário ou senha incorretos."

    @Realizar_login
    Cenário: O usuário deve entrar na plataforma inserindo o seu e-mail e senha
        Dado a página inicial de login deve estar aberta
        Quando o usuário digicar a senha no campo "E-mail ou nome de usuário"
        E digitar a senha no campo "Senha"
        Então o usuário será direcionado à página inicial do Spotify
    
    @Pesquisar_artista
    Cenário: O artista desejado deve aparecer no resultado da busc
        Dado que o usuário esteja na plataforma
        Quando o usuário digita o nome do artista no campo pesquisa
        Então é mostrado ao usuário o artista desejado