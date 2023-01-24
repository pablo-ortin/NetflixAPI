from fastapi import FastAPI

app = FastAPI()

import pandas as pd

df = pd.read_csv("csv/netflix.csv",delimiter = ',',encoding = "utf-8")

df["date_added"] = pd.to_datetime(df["date_added"])

df = df.sort_values(by=["date_added"])

df["director"] = df["director"].replace({"Not Given":None})

df2019 = df.release_year == 2019
df2019 = df[df2019]

df2020 = df.release_year == 2020
df2020 = df[df2020]

df2021 = df.release_year == 2021
df2021 = df[df2021]

df2019dicc = df2019.reset_index().to_dict(orient="index")
df2020dicc = df2020.reset_index().to_dict(orient="index")
df2021dicc = df2021.reset_index().to_dict(orient="index")

@app.get("/")
async def index():
    return {"Hola, para ver los diccionarios por favor utilice los siguientes decoradores: /2019 /2020 /2021 según el año que desee consultar."}

@app.get("/2019")
async def index():
    return {"2019":df2019dicc}

@app.get("/2020")
async def index():
    return {"2020":df2020dicc}

@app.get("/2021")
async def index():
    return {"2021":df2021dicc}