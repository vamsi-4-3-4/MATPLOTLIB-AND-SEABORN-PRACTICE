import pandas as pd
data_a={"product":["audi","audi","bmw","bmw","bugatti","bugatti","volvo","volvo","ferrari","ferrari"],
        "year":[2022,2023,2022,2023,2022,2023,2022,2023,2022,2023],
        "sales":[456,500,670,770,456,556,567,667,333,444]
        }
df=pd.DataFrame(data_a)
df.head(20)

fig,ax=plt.subplots()
(markerline,stemlines,baseline)=ax.stem(df["product"],df["sales"],use_line_collection=True)

fid,ax=plt.subplots()
(markerline,stemlines,baseline)=ax.stem(df["product"],df["sales"],use_line_collection=True)
markerline.set(marker="*",markersize=15,markeredgewidth=2,color="red")
stemlines.set(color="black")
baseline.set(visible=False)
ax.set_xlabel("product",size=12)
ax.set_ylabel("units",size=12)
ax.set_ylim(bottom=0)
plt.show()

df2=df.sort_values("sales",ascending=False)
fid,ax=plt.subplots()
(markerline,stemlines,baseline)=ax.stem(df2["product"],df2["sales"],use_line_collection=True)
markerline.set(marker="*",markersize=15,markeredgewidth=2,color="red")
stemlines.set(color="black")
baseline.set(visible=False)
ax.set_xlabel("product",size=12)
ax.set_ylabel("units",size=12)
ax.set_ylim(bottom=0)
plt.show()
