import flet as ft
import flet_webview as ftwv

def main(page: ft.Page):
    # Configurações da Janela / App
    page.title = "Marju Express"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Remove margens padrão para o WebView ocupar 100% da tela
    page.padding = 0 

    # URL do seu sistema em produção (Angular, etc.)
    URL_SISTEMA = "https://pessoal-web-marju-express.sjj3wv.easypanel.host/"

    # Indicador de progresso (barra no topo)
    progresso = ft.ProgressBar(visible=False, color="blue", height=4)

    # Funções para controlar a visibilidade da barra de carregamento
    def pagina_iniciada(e):
        progresso.visible = True
        progresso.update()

    def pagina_terminada(e):
        progresso.visible = False
        progresso.update()

    # Criação do componente WebView
    webview = ftwv.WebView(
        url=URL_SISTEMA,
        expand=True,  # Ocupa todo o espaço disponível na tela
        on_page_started=pagina_iniciada,
        on_page_ended=pagina_terminada,
        on_web_resource_error=lambda e: print("Erro ao carregar página:", e.data),
    )

    # Adiciona a barra de progresso e o WebView organizados em coluna
    page.add(
        ft.Column(
            [
                progresso,
                webview
            ],
            expand=True,
            spacing=0
        )
    )

if __name__ == "__main__":
    ft.run(main)