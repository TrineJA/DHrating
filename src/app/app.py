import flask
import dash

server = flask.Flask(__name__)
app = dash.Dash('DHrating Viewer', server=server)
app.config.suppress_callback_exceptions = True
