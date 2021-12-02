import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='index',
        options=[
            {'label': 'AtomicNumber', 'value': 'AtomicNumber'},
            {'label': 'Element', 'value': 'Element'},
            {'label': 'Symbol', 'value': 'Symbol'},
            {'label': 'AtomicMass', 'value': 'AtomicMass'},
            {'label': 'NumberOfNeutrons', 'value': 'NumberOfNeutrons'},
            {'label': 'NumberOfProtons', 'value': 'NumberOfProtons'},
            {'label': 'NumberOfElectrons', 'value': 'NumberOfElectrons'},
            {'label': 'Period', 'value': 'Period'},
            {'label': 'Group', 'value': 'Group'},
            {'label': 'Phase', 'value': 'Phase'},
            {'label': 'Radioactive', 'value': 'Radioactive'},
            {'label': 'Natural', 'value': 'Natural'},
            {'label': 'Metal', 'value': 'Metal'},
            {'label': 'Nonmetal', 'value': 'Nonmetal'},
            {'label': 'Metalloid', 'value': 'Metalloid'},
            {'label': 'Type', 'value': 'Type'},
            {'label': 'AtomicRadius', 'value': 'AtomicRadius'},
            {'label': 'Electronegativity', 'value': 'Electronegativity'},
            {'label': 'FirstIonization', 'value': 'FirstIonization'},
            {'label': 'Density', 'value': 'Density'},
            {'label': 'MeltingPoint', 'value': 'MeltingPoint'},
            {'label': 'BoilingPoint', 'value': 'BoilingPoint'},
            {'label': 'NumberOfIsotopes', 'value': 'NumberOfIsotopes'},
            {'label': 'Discoverer', 'value': 'Discoverer'},
            {'label': 'Year', 'value': 'Year'},
            {'label': 'SpecificHeat', 'value': 'SpecificHeat'},
            {'label': 'NumberOfShells', 'value': 'NumberOfShells'},
            {'label': 'NumberOfValence', 'value': 'NumberOfValence'}
        ],
        value='Period'
    ),
        dcc.Dropdown(
        id='columns',
        options=[
            {'label': 'AtomicNumber', 'value': 'AtomicNumber'},
            {'label': 'Element', 'value': 'Element'},
            {'label': 'Symbol', 'value': 'Symbol'},
            {'label': 'AtomicMass', 'value': 'AtomicMass'},
            {'label': 'NumberOfNeutrons', 'value': 'NumberOfNeutrons'},
            {'label': 'NumberOfProtons', 'value': 'NumberOfProtons'},
            {'label': 'NumberOfElectrons', 'value': 'NumberOfElectrons'},
            {'label': 'Period', 'value': 'Period'},
            {'label': 'Group', 'value': 'Group'},
            {'label': 'Phase', 'value': 'Phase'},
            {'label': 'Radioactive', 'value': 'Radioactive'},
            {'label': 'Natural', 'value': 'Natural'},
            {'label': 'Metal', 'value': 'Metal'},
            {'label': 'Nonmetal', 'value': 'Nonmetal'},
            {'label': 'Metalloid', 'value': 'Metalloid'},
            {'label': 'Type', 'value': 'Type'},
            {'label': 'AtomicRadius', 'value': 'AtomicRadius'},
            {'label': 'Electronegativity', 'value': 'Electronegativity'},
            {'label': 'FirstIonization', 'value': 'FirstIonization'},
            {'label': 'Density', 'value': 'Density'},
            {'label': 'MeltingPoint', 'value': 'MeltingPoint'},
            {'label': 'BoilingPoint', 'value': 'BoilingPoint'},
            {'label': 'NumberOfIsotopes', 'value': 'NumberOfIsotopes'},
            {'label': 'Discoverer', 'value': 'Discoverer'},
            {'label': 'Year', 'value': 'Year'},
            {'label': 'SpecificHeat', 'value': 'SpecificHeat'},
            {'label': 'NumberOfShells', 'value': 'NumberOfShells'},
            {'label': 'NumberOfValence', 'value': 'NumberOfValence'}
        ],
        value='Group'
    ),
        dcc.Dropdown(
        id='values',
        options=[
            {'label': 'AtomicNumber', 'value': 'AtomicNumber'},
            {'label': 'Element', 'value': 'Element'},
            {'label': 'Symbol', 'value': 'Symbol'},
            {'label': 'AtomicMass', 'value': 'AtomicMass'},
            {'label': 'NumberOfNeutrons', 'value': 'NumberOfNeutrons'},
            {'label': 'NumberOfProtons', 'value': 'NumberOfProtons'},
            {'label': 'NumberOfElectrons', 'value': 'NumberOfElectrons'},
            {'label': 'Period', 'value': 'Period'},
            {'label': 'Group', 'value': 'Group'},
            {'label': 'Phase', 'value': 'Phase'},
            {'label': 'Radioactive', 'value': 'Radioactive'},
            {'label': 'Natural', 'value': 'Natural'},
            {'label': 'Metal', 'value': 'Metal'},
            {'label': 'Nonmetal', 'value': 'Nonmetal'},
            {'label': 'Metalloid', 'value': 'Metalloid'},
            {'label': 'Type', 'value': 'Type'},
            {'label': 'AtomicRadius', 'value': 'AtomicRadius'},
            {'label': 'Electronegativity', 'value': 'Electronegativity'},
            {'label': 'FirstIonization', 'value': 'FirstIonization'},
            {'label': 'Density', 'value': 'Density'},
            {'label': 'MeltingPoint', 'value': 'MeltingPoint'},
            {'label': 'BoilingPoint', 'value': 'BoilingPoint'},
            {'label': 'NumberOfIsotopes', 'value': 'NumberOfIsotopes'},
            {'label': 'Discoverer', 'value': 'Discoverer'},
            {'label': 'Year', 'value': 'Year'},
            {'label': 'SpecificHeat', 'value': 'SpecificHeat'},
            {'label': 'NumberOfShells', 'value': 'NumberOfShells'},
            {'label': 'NumberOfValence', 'value': 'NumberOfValence'}
        ],
        value='Element'
    ),
    html.Div(id='my-output'),
])

@app.callback(
    Output('my-output', 'children'),
    Input('index', 'value'),
    Input('columns', 'value'),
    Input('values', 'value')
)
def update_output(index, columns, values):
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )

app.run_server(debug=True, host="0.0.0.0")