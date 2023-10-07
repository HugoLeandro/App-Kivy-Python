from kivy.app import App
from kivy.lang import Builder
import requests
from bannervenda import BannerVenda

from telas import *
from botoes import *




GUI = Builder.load_file("main.kv")
class MainApp(App):
    id_usuario = 2


    def build(self):
        return GUI

    def on_start(self):

        # Pegar informações do usuario
        requisicao = requests.get(f"https://aplicativovendas-af678-default-rtdb.firebaseio.com/{self.id_usuario}.json")
        requisicao_dic = requisicao.json()

        # Preencher foto de perfil
        avatar = requisicao_dic['avatar']
        foto_perfil = self.root.ids['foto_perfil']
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

        # Preencher lista de vendas
        try:
            vendas = requisicao_dic['vendas'][1:]
            for venda in vendas:
                banner = BannerVenda(cliente=venda['cliente'], foto_cliente=venda['foto_cliente'],
                                    produto=venda['produto'], foto_produto=venda['foto_produto'],
                                    data=venda['data'], quantidade=venda['quantidade'], preco=venda['preco'],
                                    unidade=venda['unidade'])
                pagina_homepage = self.root.ids['homepage']
                lista_vendas = pagina_homepage.ids['lista_vendas']
                lista_vendas.add_widget(banner)

        except:
            pass

    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

MainApp().run()


