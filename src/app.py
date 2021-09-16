# package imports
import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache

# local imports
from layout.layout import layout
from utils.external_assets import FONT_AWESOME

# create app
app = dash.Dash(
    __name__,
    external_stylesheets=[FONT_AWESOME, dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title='SE Project'
)

# set up cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# set initial layout
app.layout = layout
