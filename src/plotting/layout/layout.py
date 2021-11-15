# package imports
from dash import html, dcc, dash
import dash_bootstrap_components as dbc

# local imports
from plotting.layout.navbar import navbar
from plotting.layout.footer import footer

# constants
store_id = "id-data-store"

layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Store(id=store_id),
        html.Div([navbar]),
        html.Div(id="page-content"),
        footer,
    ]
)
