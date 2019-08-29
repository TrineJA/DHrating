import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output

from data_utilities import wide_to_long

from app import app

import plotly.graph_objs as go

#### THIS IS THE ONLY DIFFERENCE BETWEEN THE APPS
from data import df_wl_diff as df

# define layout
layout = html.Div([
    html.H3("Time difference to our boat. Negative is faster"),

    html.Div(id='f_ratings_reactive_container_taud_diff', style={'marginBottom': 30}),

    html.Div([
        dash_table.DataTable(id='t_ratings_reactive_taud_diff',
                             columns=
                             [{'name': 'BoatKey', 'id': 'BoatKey', 'type': 'text'}] + [{"name": i, "id": i, 'type':'numeric'} for i in df.columns.drop('BoatKey')],
                             data=df.to_dict('records'),
                             sort_action="native",
                             row_deletable=True,
                             row_selectable="multi",
                             selected_rows=[],
                             style_cell_conditional=[
                                 {'if': {'column_id': 'BoatKey'}, 'width': '20%'},
                                 {
                                     'if': {'column_id': 'BoatKey'},
                                     'textAlign': 'left'
                                 },
                             ],
                             style_data_conditional=[
                                 {
                                     'if': {'row_index': 'odd'},
                                     'backgroundColor': 'rgb(248, 248, 248)'
                                 }
                             ],
                             style_header={
                                 'backgroundColor': 'rgb(230, 230, 230)',
                                 'fontWeight': 'bold'
                             },
                             ),
    ], style={'marginBottom': 30})
])

# make graph for selected rows
@app.callback(
    Output('f_ratings_reactive_container_taud_diff', "children"),
    [Input('t_ratings_reactive_taud_diff', 'selected_rows')])
def update_graphs(selected_rows):

    # get selected rows
    if len(selected_rows)==0:
        dff = df
    else:
        dff = df.iloc[selected_rows,:]

    dff_long = wide_to_long(dff)

    return [
        dcc.Graph(id='f_ratings_reactive_taud_diff',
                  figure={
                      'data': [
                          go.Scatter(
                              x=dff_long[dff_long['BoatKey'] == i]['metric'],
                              y=dff_long[dff_long['BoatKey'] == i]['value'],
                              text=dff_long[dff_long['BoatKey'] == i]['BoatKey'],
                              mode='markers',
                              opacity=0.7,
                              marker={
                                  'size': 15,
                                  'line': {'width': 0.5, 'color': 'white'}
                              },
                              name=i
                          ) for i in dff_long.BoatKey.unique()
                      ],
                      'layout': go.Layout(
                          yaxis={'title': 'Seconds per Nautical Mile'},
                          margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                          legend={'x': 1, 'y': 1},
                          hovermode='closest'
                      )
                  }
                  )
    ]
