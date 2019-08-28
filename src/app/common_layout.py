import dash_html_components as html
import dash_core_components as dcc

from data_utilities import wide_to_long

import plotly.graph_objs as go

def common_layout(df):
    #make format long for easier plotting
    df_long = wide_to_long(df)

    # define layout
    layout = html.Div([
        html.Div([
            dcc.Graph(id='f_ratings_diff',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=df_long[df_long['BoatKey'] == i]['metric'],
                                  y=df_long[df_long['BoatKey'] == i]['value'],
                                  text=df_long[df_long['BoatKey'] == i]['BoatKey'],
                                  mode='markers',
                                  opacity=0.7,
                                  marker={
                                      'size': 15,
                                      'line': {'width': 0.5, 'color': 'white'}
                                  },
                                  name=i
                              ) for i in df_long.BoatKey.unique()
                          ],
                          'layout': go.Layout(
                              yaxis={'title': 'Seconds per Nautical Mile'},
                              margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                              legend={'x': 1, 'y': 1},
                              hovermode='closest'
                          )
                      }
            )
        ])
    ])

    return layout