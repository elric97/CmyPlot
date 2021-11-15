# package imports
from plotting.app import app
import argparse
from waitress import serve

# local imports

from plotting.environment.settings import APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK

# initializes all callbacks
import plotting.utils.routes
import plotting.pages.upload.upload_callbacks
import plotting.pages.table.table_callbacks
import plotting.pages.graph.graph_callbacks

# initialize services
server = app.server

# site endpoint
if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="CmyPlot")
    my_parser.add_argument(
        "--host",
        action="store",
        default="127.0.0.1",
        type=str,
        metavar="host address",
        help="Host address where the website has to be deployed",
    )
    args = my_parser.parse_args()

    if __debug__:
        app.run_server(
            host=args.host,
            port=APP_PORT,
            debug=True,
            dev_tools_props_check=DEV_TOOLS_PROPS_CHECK,
        )

    else:
        serve(server, host="127.0.0.1", port=8080)
