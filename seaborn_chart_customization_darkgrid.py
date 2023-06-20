#CELL 1
import matplotlib.pyplot as plt
import seaborn as sns
print("--DATASETS GIVEN IN THE SEABORN--\n",sns.get_dataset_names())
iris=sns.load_dataset("iris")
print("-----IRIS DATASET HEAD-----\n",iris.head())
anagrams=sns.load_dataset("anagrams")
carcrashes=sns.load_dataset("car_crashes")
print("-----CAR CRASHES DATASET-----------\n",carcrashes.head())
print("-----ANAGRAMS DATASET HEAD----\n",anagrams.head())
print("---IRIS DATASET----\n",iris.count())
print("-----ANAGRAMS DATASET----\n",anagrams.count())
print("A FIGURE LEVEL FUNCTION CONTROLS THE FIGURE CATPLOT,RELPLOT")
#CELL 2

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
sns.swarmplot(x="species",y="petal_length",data=iris,ax=ax1).set_title("PLOT_1")
ax2.scatter("petal_width","petal_length",data=iris)
ax2.set_ylabel("PETAL_LENGTH")
ax2.set_xlabel("PETAL_WIDTH")
plt.show()

#CELL 3
sns.set()
sns.set_style("darkgrid")
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
sns.swarmplot(x="species",y="petal_length",data=iris,ax=ax1)
ax2.scatter("petal_width","petal_length",data=iris)
ax2.set_ylabel("PETAL_LENGTH")
ax2.set_xlabel("PETAL_WIDTH")
plt.show()
