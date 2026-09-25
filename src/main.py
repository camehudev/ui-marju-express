import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "Marju Express"
    page.padding = 0

    URL_SISTEMA = "https://pessoal-web-marju-express.sjj3wv.easypanel.host/"

    # Adiciona a permissão apenas se estiver a correr numa plataforma compatível (ex: Android)
    if page.web is False and page.platform in [ft.PagePlatform.ANDROID, ft.PagePlatform.IOS, ft.PagePlatform.WINDOWS]:
        try:
            import flet_permission_handler as fph
            permissao = fph.PermissionHandler()
            page.overlay.append(permissao)
            # Pode pedir a permissão da câmera aqui se necessário
        except Exception as e:
            print("Erro ao carregar permissões:", e)

    webview = fwv.WebView(
        url=URL_SISTEMA,
        expand=True,
    )

    page.add(webview)

if __name__ == "__main__":
    ft.run(main)