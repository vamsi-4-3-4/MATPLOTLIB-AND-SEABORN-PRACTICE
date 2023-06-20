import matplotlib.pyplot as plt
import seaborn as sns
titanic=sns.load_dataset("titanic")
titanic.head()

titanic.isnull().sum()

survived_df=titanic[titanic['survived']==True]
names=survived_df["sex"].unique()
print(names)


values=survived_df["sex"].value_counts()
print(values)

fig,ax=plt.subplots()
ax.bar(names,values,color=["black","green"])
ax.set_xlabel("SEX")
ax.set_ylabel("NUMBER OF SURVIVALS")
ax.set_title("TITANIC SURVIVALS")
plt.show()

survived=titanic.groupby("sex")["survived"].sum()
survived.head()
fig,ax=plt.subplots()
ax.bar(survived.index,survived.values,color=["red","black"])
ax.set_xlabel("GENDER")
ax.set_ylabel("NUMBER OF SURVIVALS")
ax.set_title("TITANIC SURVIVALS")
plt.show()

survived=titanic.groupby("sex")["survived"].sum()
survived.head()
fig,ax=plt.subplots()
ax.barh(survived.index,survived.values,color=["red","black"])
ax.set_xlabel("GENDER")
ax.set_ylabel("NUMBER OF SURVIVALS")
ax.set_title("TITANIC SURVIVALS")
plt.show()

tips=sns.load_dataset("tips")
tips.head()

fig,ax=plt.subplots()
sns.set_style("darkgrid")
ax=sns.barplot(x="day",y="total_bill",data=tips,ax=ax)
plt.show()

fig,ax=plt.subplots()
sns.barplot(x="tip",y="time",data=tips,ax=ax)
plt.show()

fig,ax=plt.subplots()
sns.set_style("darkgrid")
ax=sns.barplot(x="day",y="total_bill",palette="BuGn_r",data=tips,ax=ax)
plt.show()
