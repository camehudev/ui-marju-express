import flet as ft
import flet_webview as ftwv

def main(page: ft.Page):
    # Configurações da Janela / App
    page.title = "Marju Express"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Remove margens padrão para o WebView ocupar 100% da tela
    page.padding = 0

    # URL do seu sistema em produção (Angular, etc.)
    # URL_SISTEMA = "https://pessoal-web-marju-express.sjj3wv.easypanel.host/"

    # Criação do componente WebView (sem barra de progresso)
    webview = ftwv.WebView(
        url="https://pessoal-web-marju-express.sjj3wv.easypanel.host/",
        expand=True,  # Ocupa todo o espaço disponível na tela
        on_web_resource_error=lambda e: print("Erro ao carregar página:", e.data),
    )

    # Adiciona apenas o WebView diretamente na página
    page.add(webview)

if __name__ == "__main__":
    ft.run(main)