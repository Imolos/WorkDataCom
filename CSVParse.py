import dask.dataframe as dd

Open = ('All.csv')

data = dd.read_csv(Open, usecols=["ID","Název","Kontaktní osoba"])

print(data)

