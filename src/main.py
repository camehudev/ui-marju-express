import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "Marju Express"
    page.padding = 0

    URL_SISTEMA = "https://pessoal-web-marju-express.sjj3wv.easypanel.host/"

    # Configuração de permissões para Android/Mobile
    if page.web is False and page.platform in [ft.PagePlatform.ANDROID, ft.PagePlatform.IOS]:
        try:
            import flet_permission_handler as fph
            ph = fph.PermissionHandler()
            page.overlay.append(ph)
            
            # Pede a permissão de câmera de forma assíncrona ou direta ao iniciar
            ph.request(fph.Permission.CAMERA)
        except Exception as e:
            print("Erro ao gerir permissões:", e)

    webview = fwv.WebView(
        url=URL_SISTEMA,
        expand=True,
    )

    page.add(webview)

if __name__ == "__main__":
    ft.run(main)