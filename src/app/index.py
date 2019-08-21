import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objs as go

from app import app, server
from data import df_wl, df_wl_diff

## TODO: make tab for TACI and TAUD, fix graph size, add class to identifier.

# define layout
app.layout = html.Div([
    html.H3('DH rating for windward/leeward courses'),

    html.Div([
        dcc.Graph(id='f_ratings_diff',
                  figure={
                      'data': [
                          go.Scatter(
                              x=df_wl_diff[df_wl_diff['SailNo'] == i]['metric'],
                              y=df_wl_diff[df_wl_diff['SailNo'] == i]['value'],
                              text=df_wl_diff[df_wl_diff['SailNo'] == i]['Class'],
                              mode='markers',
                              opacity=0.7,
                              marker={
                                  'size': 15,
                                  'line': {'width': 0.5, 'color': 'white'}
                              },
                              name=i
                          ) for i in df_wl_diff.SailNo.unique()
                      ],
                      'layout': go.Layout(
                          yaxis={'title': 'Delta Nautical Mile Sailing Time [s]'},
                          margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                          legend={'x': 1, 'y': 1},
                          hovermode='closest'
                      )
                  }
        ),

        dcc.Graph(id='f_ratings',
                  figure={
                      'data': [
                          go.Scatter(
                              x=df_wl[df_wl['SailNo'] == i]['metric'],
                              y=df_wl[df_wl['SailNo'] == i]['value'],
                              text=df_wl[df_wl['SailNo'] == i]['Class'],
                              mode='lines+markers',
                              opacity=0.7,
                              marker={
                                  'size': 15,
                                  'line': {'width': 0.5, 'color': 'white'}
                              },
                              name=i
                          ) for i in df_wl.SailNo.unique()
                      ],
                      'layout': go.Layout(
                          xaxis={'title': 'Windspeed category [m/s]'},
                          yaxis={'title': 'Nautical Mile Sailing Time [s]'},
                          margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                          legend={'x': 1, 'y': 1},
                          hovermode='closest'
                      )
                  }
        )
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")
