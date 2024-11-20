# Mapa Interativo de ONGs - ODS 1: Erradicação da Pobreza

Este projeto apresenta um **mapa interativo de ONGs** que atuam na região de Brasília e arredores, com o objetivo de facilitar o acesso a informações sobre instituições que trabalham com saúde, cultura, educação, alimentação e outras áreas relacionadas à redução da pobreza.

O projeto foi desenvolvido utilizando **Python** e bibliotecas como `folium` e `geopy` para criar um mapa dinâmico e funcional, com recursos avançados para navegação e interatividade.

## Funcionalidades

### 1. Mapa Interativo
- **Visualização Geográfica**: O mapa exibe ONGs localizadas na região de Brasília com marcadores interativos.
- **Marcadores Informativos**: Cada ONG está representada por um marcador azul no mapa.  
   - Clique no marcador para visualizar:
     - O **nome da ONG**.
     - A **distância** até a UDF (Universidade de Brasília).
     - Um link para o **site oficial**, onde é possível obter mais informações ou realizar doações.

### 2. Filtros por Categorias
As ONGs estão organizadas em cinco categorias:
- **Educação**
- **Saúde**
- **Alimentação**
- **Cultura**
- **Outros**

Os filtros permitem habilitar ou desabilitar a visualização de cada categoria separadamente.

### 3. MiniMapa
- Inclui um minimapa na interface para facilitar a navegação em áreas próximas, como Goiás e Planaltina de Goiás.

### 4. Distância Personalizada
- Opção "Mostrar Distância" para exibir ou ocultar linhas indicando a distância entre a **UDF** e as ONGs.

### 5. Hospedagem
O site está hospedado gratuitamente no GitHub Pages para facilitar o acesso público ao mapa interativo.

## Tecnologias Utilizadas

- **Python**
  - `folium`: Para criar o mapa interativo.
  - `geopy`: Para calcular distâncias entre coordenadas geográficas.
- **HTML**: Para renderizar o mapa gerado.
- **GitHub Pages**: Para hospedar o mapa e torná-lo acessível publicamente.

## Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-repositorio.git
