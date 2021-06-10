from flask import Flask, request
import psycopg2 as pg

app = Flask("covid cases")


@app.route("/")
def hello():
    conc = pg.connect(database="covidcases")
    cursor = conc.cursor()
    cursor.execute("select state,active_cases,deaths from covid_data")
    cases = []
    for state, active_cases, deaths in cursor.fetchall():
        item = f"<a href=/find?state={state}>{state}<a/>: <br/>  Active Cases:{active_cases} <br/> Deaths : {deaths}"
        cases.append(item)
    l = "<hr/>".join(cases)
    return l


items = []


@app.route("/add")
def add_item():
    item = request.args.get("item")
    items.append(item)
    return f"No.of items : {len(items)}"


@app.route("/find")
def active_cases():
    state = request.args.get("state")
    conc = pg.connect(database="covidcases")
    cursor = conc.cursor()
    cursor.execute(
        "select state,active_cases,deaths from covid_data where state like %s",
        (state.title() + "%",),
    )
    for name, active_cases, deaths in cursor.fetchall():
        a = active_cases
        b = deaths
        l = f"<h2>{name}:<h2/><h3>Active Cases : {a} <br/> Deaths : {b}<h3/>"
        return l
