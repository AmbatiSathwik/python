from flask import Flask, request
import psycopg2 as pg

app = Flask("covid cases")


@app.route("/")
def hello():
    conc = pg.connect(database="covidcases")
    cursor = conc.cursor()
    items = cursor.execute("select state,active_cases,deaths from covid_data")
    cases = []
    for state, active_cases, deaths in cursor.fetchall():
        item = f"{state}: <br/>  Active Cases:{active_cases} <br/> Deaths : {deaths}"
        cases.append(item)
    l = "<hr/>".join(cases)
    return l


@app.route("/add")
def add_item():
    item = request.args.get("item")
    items.append(item)
    return f"No.of items : {len(items)}"
