import flet as ft
import flet_webview as ftwv

def main(page: ft.Page):
    # Configurações da Janela / App
    page.title = "Marju Express"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Remove margens padrão para o WebView ocupar 100% da tela
    page.padding = 0 

    # URL do seu sistema em produção (Angular, etc.)
    URL_SISTEMA = "https://pessoal-web-marju-express.sjj3wv.easypanel.host/"  # <--- Substitua pela sua URL real

    # Criação do componente WebView
    webview = ftwv.WebView(
        url=URL_SISTEMA,
        expand=True,  # Ocupa todo o espaço disponível na tela
        on_page_started=lambda _: print("Carregando página..."),
        on_page_ended=lambda _: print("Página carregada com sucesso!"),
        on_web_resource_error=lambda e: print("Erro ao carregar página:", e.data),
    )

    # Adiciona o WebView na página principal
    page.add(webview)

if __name__ == "__main__":
    ft.run(main)