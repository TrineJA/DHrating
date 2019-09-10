import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output
import numpy as np

from data_utilities import wide_to_long, get_rating_columns, my_funky_formatter

from app import app

import plotly.graph_objs as go

#### THIS IS THE ONLY DIFFERENCE BETWEEN THE APPS
from data import df_circle_diff as df
ws_cols = get_rating_columns(df)

# define layout
layout = html.Div([
    html.H3("Time difference to our boat. Negative is faster"),

    html.Div([
        html.P("Length of course in Nautical Miles")
        ], style = {'display': 'inline-block', 'width': '270px'}
    ),

    html.Div([
        dcc.Input(
            id='input_nm',
            placeholder='Nm',
            debounce = True,
            type='text',
            value='1.0',
            style={'width': 70}
        )
        ], style = {'display': 'inline-block', 'width': '30%', 'margin':'auto'}
    ),

    html.Div([
        dash_table.DataTable(id='t_ratings_reactive_taci_diff',
                             columns=
                             [{'name': 'BoatKey', 'id': 'BoatKey', 'type': 'text'}] + [{"name": i, "id": i, 'type':'text'} for i in df.columns.drop('BoatKey')],
                             sort_action="native",
                             row_selectable="multi",
                             selected_rows=[],
                             style_cell_conditional=[
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
    ], style={'marginBottom': 30}),

    html.H3("Time difference to our boat per Nautical Mile"),

    html.Div(id='f_ratings_reactive_container_taci_diff', style={'marginBottom': 30}),

])

# update table based on input distance
@app.callback(
    Output('t_ratings_reactive_taci_diff', 'data'),
    [Input('input_nm', 'value')])
def update_table(scaling_factor):
    # if scaling factor is empty set it to 1
    if not scaling_factor:
        scaling_factor = '1'

    #df_tmp introduced to avoid scaling is relative to what is currently in table
    df_tmp = df.copy()

    # scale relevant columns
    df_tmp[ws_cols] = df_tmp[ws_cols] * float(scaling_factor)

    # format difference in minutes and seconds for nicer printing
    df_tmp[ws_cols] = df_tmp[ws_cols].applymap(my_funky_formatter)


    return df_tmp.to_dict('records')


# make graph for selected rows
@app.callback(
    Output('f_ratings_reactive_container_taci_diff', "children"),
    [Input('t_ratings_reactive_taci_diff', 'selected_rows')])
def update_graphs(selected_rows):

    # get selected rows
    if len(selected_rows)==0:
        dff = df
    else:
        dff = df.iloc[selected_rows,:]

    dff_long = wide_to_long(dff)

    return [
        dcc.Graph(id='f_ratings_reactive_taci_diff',
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
