import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objs as go

def common_layout(df):
    # define layout
    layout = html.Div([
        html.Div([
            dcc.Graph(id='f_ratings_diff',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=df[df['SailNo'] == i]['metric'],
                                  y=df[df['SailNo'] == i]['value'],
                                  text=df[df['SailNo'] == i]['Class'],
                                  mode='markers',
                                  opacity=0.7,
                                  marker={
                                      'size': 15,
                                      'line': {'width': 0.5, 'color': 'white'}
                                  },
                                  name=i
                              ) for i in df.SailNo.unique()
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