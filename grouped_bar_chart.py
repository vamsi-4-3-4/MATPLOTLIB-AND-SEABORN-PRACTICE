import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data_a={"product":["audi","audi","bmw","bmw","bugatti","bugatti","volvo","volvo","ferrari","ferrari"],
        "year":[2022,2023,2022,2023,2022,2023,2022,2023,2022,2023],
        "sales":[456,500,670,770,456,556,567,667,333,444]
        }
df=pd.DataFrame(data_a)
df.head(20)

fig,ax=plt.subplots()
sns.barplot(x="year",y="sales",hue="product",data=df,palette="bright",estimator=sum,ax=ax)
plt.show()
