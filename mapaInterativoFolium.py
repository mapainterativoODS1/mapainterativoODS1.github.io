import pandas as pd
import folium
from folium.plugins import Fullscreen, MiniMap
from geopy.distance import geodesic

udf_coords = [-15.80257, -47.90094]
mapa_brasilia = folium.Map(location=udf_coords, zoom_start=12, control_scale=True)
minimap = MiniMap()
minimap.add_to(mapa_brasilia)
Fullscreen().add_to(mapa_brasilia)

locais = [
    {"nome": "Casa Azul", "coordenadas": [-15.89047, -48.11012], "link": "https://www.casazulfelipeaugusto.org.br/", "categoria": "Educação"},
    {"nome": "CASA DA CRIANÇA BATUÍRA", "coordenadas": [-15.80078, -48.10743], "link": "https://www.ccbatuira.org.br/", "categoria": "Saúde"},
    {"nome": "Instituto Menos de Mim", "coordenadas": [-15.81243, -48.01925], "link": "https://menosdemim.apoiar.co/2", "categoria": "Alimentação"},
    {"nome": "Instituto do Carinho", "coordenadas": [-15.81760, -48.09161], "link": "https://www.institutodocarinho.org.br/", "categoria": "Educação"},
    {"nome": "Instituto Social Bom Samaritano", "coordenadas": [-15.77814, -47.99886], "link": "https://www.instagram.com/ibs.social/", "categoria": "Saúde"},
    {"nome": "SHALKE12", "coordenadas": [-15.88858, -48.10162], "link": "https://shalke12.com.br/", "categoria": "Outros"},
    {"nome": "Projeto Dividir", "coordenadas": [-15.78318, -47.88298], "link": "https://coepbrasil.org.br/fome-projeto-dividir/", "categoria": "Alimentação"},
    {"nome": "Instituto Adenilson Cruz", "coordenadas": [-15.81141, -47.97513], "link": "https://linktr.ee/InstitutoAdenilsonCruz?utm_source=linktree_profile_share&ltsid=df9ffc9f-ce8b-44b4-9c33-1f93ec470a62", "categoria": "Alimentação"},
    {"nome": "Lar de São José", "coordenadas": [-15.80045, -48.10632], "link": "https://lardesaojose.org/", "categoria": "Educação"},
    {"nome": "Associação das Mulheres de Sobradinho II", "coordenadas": [-15.64378, -47.82077], "link": "https://www.facebook.com/p/Associa%C3%A7%C3%A3o-das-Mulheres-de-Sobradinho-II-100080885431132/", "categoria": "Outros"},
    {"nome": "Casa de Ismael", "coordenadas": [-15.74881, -47.89895], "link": "https://www.casadeismael.org.br/", "categoria": "Educação"},
    {"nome": "Instituto Migrações e Direitos Humanos (IMDH)", "coordenadas": [-15.70916, -47.87607], "link": "https://www.migrante.org.br/", "categoria": "Outros"},
    {"nome": "Centro Comunitário Semente de Esperança", "coordenadas": [-15.64365, -47.82247], "link": "https://sementeesperanca.org.br/", "categoria": "Educação"},
    {"nome": "Instituto Bom Samaritano", "coordenadas": [-15.77815, -47.99836], "link": "https://www.instagram.com/instituto_bom_samaritano/", "categoria": "Alimentação"},
    {"nome": "Associação Dos Idosos Da Ceilândia", "coordenadas": [-15.83023, -48.09816], "link": "https://www.idososdaceilandia.org.br/", "categoria": "Outros"},
    {"nome": "Associação Dos Idosos De Taguatinga", "coordenadas": [-15.82046, -48.08388], "link": "https://www.instagram.com/idososdetaguatinga/", "categoria": "Outros"},
    {"nome": "ASSOCIAÇÃO COMUNITÁRIA DO BRASIL CENTRAL", "coordenadas": [-15.80645, -47.90491], "link": "https://www.ongsbrasil.com.br/default.asp?Pag=2&Destino=InstituicoesTemplate&CodigoInstituicao=13&Instituicao=ASSOCIACAO%20COMUNITARIA%20DO%20BRASIL%20CENTRAL", "categoria": "Outros"},
    {"nome": "Associação Humana Povo para Povo Brasil", "coordenadas": [-15.83015, -48.03221], "link": "https://www.humanabrasil.org/", "categoria": "Outros"},
    {"nome": "CRECHE FREDERICO OZANAM", "coordenadas": [-15.82735, -48.09153], "link": "https://crechefredericoozanam.org.br/", "categoria": "Educação"},
    {"nome": "Instituto Berço da Cidadania", "coordenadas": [-15.74771, -47.89971], "link": "https://www.bercodacidadania.ong.br/", "categoria": "Educação"},
    {"nome": "INSTITUTO DE COOPERAÇÃO FALA BRASIL - ICFB", "coordenadas": [-15.67984, -47.86343], "link": "http://icfbcaesguia.org.br/", "categoria": "Outros"},
    {"nome": "LAR DE SÃO JOSÉ", "coordenadas": [-15.79987, -48.10653], "link": "https://lardesaojose.org/", "categoria": "Educação"},
    {"nome": "ASSOCIAÇÃO DE MULHERES EMPREENDEDORAS", "coordenadas": [-15.78913, -47.88684], "link": "https://www.empreendedorasbrusa.com/", "categoria": "Outros"},
    {"nome": "Academia Taguatinguense de Letras", "coordenadas": [-15.82981, -48.05763], "link": "https://www.facebook.com/AcademiaTaguatinguenseDeLetras/?locale=pt_BR", "categoria": "Cultura"},
    {"nome": "Valor Cultural", "coordenadas": [-15.77796, -47.88902], "link": "https://valorcultural.com.br/", "categoria": "Cultura"},
    {"nome": "ARTE VIDA", "coordenadas": [-15.80049, -47.92538], "link": "https://www.instagram.com/academia_artevida/", "categoria": "Cultura"},
    {"nome": "Associação Brasil Melhor", "coordenadas": [-15.26797, -47.98293], "link": "https://www.abmbrasil.com.br/", "categoria": "Outros"},
    {"nome": "Casa Transitória de Brasília", "coordenadas": [-15.67003, -47.64807], "link": "https://casatransitoriadebrasilia.com.br/", "categoria": "Saúde"},
    {"nome": "Instituto Tocar", "coordenadas": [-15.74767, -47.90067], "link": "https://institutotocar.org/", "categoria": "Saúde"},
    {"nome": "Abrigo Flora e Fauna", "coordenadas": [-16.01587, -48.13727], "link": "https://www.instagram.com/abrigofloraefauna/", "categoria": "Saúde"},
    {"nome": "Amigos da Vida", "coordenadas": [-15.68625, -47.92592], "link": "https://www.amigos.org.br/", "categoria": "Saúde"},
    {"nome": "Associação Brasiliense de Apoio ao Paciente de Câncer (ABAC)", "coordenadas": [-15.84205, -47.02225], "link": "https://abacluz.org.br/", "categoria": "Saúde"},
    {"nome": "Associação de Moradores de Vicente Pires", "coordenadas": [-15.80765, -48.01593], "link": "https://amovipe.com.br/", "categoria": "Outros"},
    {"nome": "Instituto Reciclando Sons", "coordenadas": [-15.77984, -47.98780], "link": "https://reciclandosons.org.br/", "categoria": "Cultura"},
    {"nome": "ONG Vida Positiva", "coordenadas": [-15.78946, -47.88531], "link": "https://www.instagram.com/vidapositivadf/", "categoria": "Saúde"}
]

def calcular_distancia(coord1, coord2):
    return geodesic(coord1, coord2).km

grupo_educacao = folium.FeatureGroup(name='Educação')
grupo_saude = folium.FeatureGroup(name='Saúde')
grupo_alimentacao = folium.FeatureGroup(name='Alimentação')
grupo_outros = folium.FeatureGroup(name='Outros')
grupo_cultura = folium.FeatureGroup(name='Cultura')

categorias = {
    "Educação": grupo_educacao,
    "Saúde": grupo_saude,
    "Alimentação": grupo_alimentacao,
    "Outros": grupo_outros,
    "Cultura": grupo_cultura
}
mostrar_distancia = True 
camada_distancias = folium.FeatureGroup(name='Mostrar Distâncias')

for local in locais:
    distancia_km = calcular_distancia(udf_coords, local["coordenadas"])
    
    popup_html = f"""
    <div style="width: 200px;">
        <h4 style="color: black; font-weight: bold;">{local["nome"]}</h4>
        <p style="font-size: 14px; color: black; font-weight: bold;"><b>Distância:</b> {distancia_km:.2f} km</p>
        <a href="{local["link"]}" target="_blank">Visitar site</a>
    </div>
    """
    
    popup = folium.Popup(popup_html, max_width=300)
    
    folium.Marker(
        location=local["coordenadas"],
        popup=popup,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(categorias[local["categoria"]])
    
    if mostrar_distancia:  
        folium.PolyLine(
            locations=[udf_coords, local["coordenadas"]],
            color='blue',
            weight=2,
            opacity=0.7,
            tooltip=f"{local['nome']} - {distancia_km:.2f} km"
        ).add_to(camada_distancias)

grupo_educacao.add_to(mapa_brasilia)
grupo_saude.add_to(mapa_brasilia)
grupo_alimentacao.add_to(mapa_brasilia)
grupo_outros.add_to(mapa_brasilia)
grupo_cultura.add_to(mapa_brasilia)

camada_distancias.add_to(mapa_brasilia)  

folium.LayerControl(collapsed=False).add_to(mapa_brasilia)

mapa_brasilia.save("mapa.html")
print("mapa criado")