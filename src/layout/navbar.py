# package imports
import dash_bootstrap_components as dbc

# local imports
from pages.home import home
from pages.upload import upload
from pages.table import table

# set contansts
toggler = 'id-navbar-toggler'
collapse = 'id-navbar-collapse'
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand(
                # TODO update with name of site
                'SE Project 1',
                href='/'
            ),
            dbc.NavbarToggler(id=toggler),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                home.title,
                                href=home.path
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                upload.title,
                                href=upload.path
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                table.title,
                                href=table.path
                            )
                        )
                    ],
                    navbar=True
                ),
                id=collapse,
                navbar=True
            )
        ]
    ),
    sticky='fixed',
    color='primary',
    dark=True
)
