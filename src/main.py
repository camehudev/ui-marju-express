import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    # 1. Adicionar o manipulador de permissões na overlay da página
    ph = ft.PermissionHandler()
    page.overlay.append(ph)

    page.add(
        ft.SafeArea(
            expand=True,
            content=fwv.WebView(
                url="https://pessoal-web-marju-express.sjj3wv.easypanel.host/",
                on_page_started=lambda _: print("Page started"),
                on_page_ended=lambda _: print("Page ended"),
                on_web_resource_error=lambda e: print("WebView error:", e.data),
                expand=True,
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main)
