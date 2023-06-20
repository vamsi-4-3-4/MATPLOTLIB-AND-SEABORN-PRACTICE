import matplotlib.pyplot as plt
revenue=[4555,6565,3232]
labels=["AUDI","BMW","BENZ"]
colors=["red","blue","silver"]
plt.style.use("seaborn-darkgrid")
fig,ax=plt.subplots()
ax.set_title("REVENUE SHARE")
ax.pie(revenue,labels=labels,wedgeprops={"edgecolor":"white"},colors=colors,shadow=False,startangle=90)
plt.tight_layout()
plt.show()

explode=[0,0,0.2]
plt.style.use("seaborn-bright")
fig,ax=plt.subplots()
ax.set_title("REVENUE SHARE")
ax.pie(revenue,labels=labels,wedgeprops={"edgecolor":"white"},colors=colors,explode=explode,shadow=False,startangle=90,autopct="%1.1f%%")
fig.legend(loc="lower right")
plt.tight_layout()
plt.show()
