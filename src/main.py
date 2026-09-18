import flet as ft
import requests

# URL onde o seu FastAPI está rodando (substitua pelo IP da sua VPS ou rede local se testar no celular)
API_URL = "http://127.0.0.1:8000"


def main(page: ft.Page):
    # --- Configurações da Página (Visual do App) ---
    page.title = "Marju Express - Triagem"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Variáveis de Estado (O que muda na tela) ---
    status_label = ft.Text("Pressione o botão para iniciar a triagem", size=16)
    
    resultado_card = ft.Card(
        content=ft.Container(
            content=ft.Text("Aguardando...", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            padding=20,
            bgcolor=ft.Colors.BLUE_GREY_700
        ),
        visible=False
    )

    # --- Função de Ação do Botão ---
    def on_scan_click(e):
        status_label.value = "Enviando solicitação para o servidor..."
        resultado_card.visible = False
        page.update()

        # Simulando o envio de um código ou requisição para a API FastAPI
        # (Aqui você integrará a captura de imagem ou input do código de barras)
        codigo_exemplo = "7891023456789" 

        try:
            # Faz a requisição POST para a sua API FastAPI
            response = requests.post(f"{API_URL}/escanear", json={"codigo": codigo_exemplo})
            
            if response.status_code == 200:
                dados_resposta = response.json() 
                destino = dados_resposta.get("destino", "CAIXA 01")
                bairro = dados_resposta.get("bairro", "Centro")
                
                status_label.value = "Processamento concluído!"
                resultado_card.content.content.value = f"📦 Código: {codigo_exemplo}\n📍 Destino: {destino} ({bairro})"
                resultado_card.content.bgcolor = ft.Colors.GREEN_700
                resultado_card.visible = True
            else:
                status_label.value = "Erro na resposta do servidor"
                resultado_card.content.content.value = f"Status Code: {response.status_code}"
                resultado_card.content.bgcolor = ft.Colors.RED_700
                resultado_card.visible = True

        except requests.exceptions.ConnectionError:
            status_label.value = "Erro de Conexão"
            resultado_card.content.content.value = "Não foi possível conectar ao FastAPI na VPS."
            resultado_card.content.bgcolor = ft.Colors.RED_700
            resultado_card.visible = True
        except Exception as ex:
            status_label.value = "Erro Genérico"
            resultado_card.content.content.value = str(ex)
            resultado_card.content.bgcolor = ft.Colors.RED_700
            resultado_card.visible = True
            
        page.update()

    # --- Componentes Visuais (Widgets) ---
    botao_scan = ft.Button(
        content=ft.Row(
            [             
                ft.Text("Escanear / Consultar")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        icon=ft.Icons.CAMERA_ALT,
        on_click=on_scan_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8)
        ),
        height=50,
        width=280
    )

    # --- Adicionando os elementos na página ---
    page.add(
        ft.Column(
            [
                ft.Text("Marju Express", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align="center"),
                ft.Text("Solução de Triagem Local", size=14, color=ft.Colors.GREY_700, text_align="center"),
                ft.Container(height=30),
                status_label,
                ft.Container(height=20),
                botao_scan,
                ft.Container(height=30),
                resultado_card
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# --- Ponto de entrada da aplicação ---
if __name__ == "__main__":
    ft.run(main)