from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app, server
import TAUD, TAUD_diff, TACI, TACI_diff

## TODO: make input to scale diff based on Nm

app.layout = html.Div(
    [
        # header
        html.Div([html.Span("DH Rating insights (powered by TalTrans)", className="app-title")], className="row header"),
        # tabs
        html.Div(
            [
                dcc.Tabs(
                    id="tabs",
                    style={"height": "20", "verticalAlign": "middle"},
                    children=[
                        dcc.Tab(label="Windward/leeward", value="TAUD"),
                        dcc.Tab(label="Windward/leeward - relative", value="TAUD_diff"),
                        dcc.Tab(label="Circle", value="TACI"),
                        dcc.Tab(label="Circle - relative", value="TACI_diff"),
                    ],
                    value="rating_tab",
                )
            ],
            className="row tabs_div",
        ),
        # Tab content
        html.Div(id="tab_content", className="row", style={"margin": "2% 3%"}),
        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css", rel="stylesheet"),
        html.Link(
            href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",
            rel="stylesheet",
        ),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(
            href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css",
            rel="stylesheet",
        ),
    ],
    className="row",
    style={"margin": "0%"},
)


@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):

    if tab == "TAUD":
        return TAUD.layout
    elif tab == "TACI":
        return TACI.layout
    elif tab == "TAUD_diff":
        return TAUD_diff.layout
    elif tab == "TACI_diff":
        return TACI_diff.layout
    else:
        return TAUD.layout


if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")
