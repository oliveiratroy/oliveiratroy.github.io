import pandas as pd

df = pd.read_csv("pct\\src\\data\\net_migration_data.csv")
g = df.loc[df["Country Name"] == "Guatemala"]
h = df.loc[df["Country Name"] == "Honduras"]
c = df.loc[df["Country Name"] == "Colombia"]

for n,d in [("Guatemala", g), ("Honduras",h), ("Colombia",c)]:
    f = open(n + ".js", "a")
    f.write("export let "+n+" = [\n")
    
    for n in range(1960, 2022):
        f.write("  {\n    Year: "+str(n)+",\n    Change: "+str(d[str(n)].values[0])+",\n  },\n")

    f.write("];")
    f.close()


df2 = pd.read_csv("pct\\src\\data\\percent_gdp.csv")
g = df2.loc[df2["Country Name"] == "Guatemala"]
h = df2.loc[df2["Country Name"] == "Honduras"]
c = df2.loc[df2["Country Name"] == "Colombia"]

for n,d in [("Guatemala", g), ("Honduras",h), ("Colombia",c)]:
    f = open(n + "2.js", "a")
    f.write("export let "+n+"2 = [\n")
    
    for n in range(1960, 2022):
        f.write("  {\n    Year: "+str(n)+",\n    Change: "+str(d[str(n)].values[0])+",\n  },\n")

    f.write("];")
    f.close()






