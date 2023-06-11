import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Distribuição Geográfica', children=[
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/bars_mun_sc_2022.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_idade_media_2022.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_idade_media_2020.html', width='100%', height='500')
        ]),
        dcc.Tab(label='Grau de Escolaridade', children=[
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_escolaridade_mun_2016.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_escolaridade_mun_2018.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_escolaridade_mun_2020.html', width='100%', height='500')
        ]),
        dcc.Tab(label='Idade Média', children=[
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_idade_media_2014.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_idade_media_2016.html', width='100%', height='500'),
            html.Iframe(src='https://raw.githubusercontent.com/luizarubio/TSE_datavis/main/mapa_idade_media_2018.html', width='100%', height='500')
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
