import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from Layouts.PageHeader import page_header
from Layouts.PageContent import page_content_form


main = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
main.title = "Health Insurance Customer Details"

main.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    page_header,
    page_content_form,
    dcc.Store(id='intermediate-value')
])

if __name__ == "__main__":
    main.run_server(debug=True)
