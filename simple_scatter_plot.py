#CELL_1
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
sns.catplot(x="species",y="petal_length",kind="swarm",data=iris)
plt.show()

#CELL_2
fig,ax=plt.subplots()
sns.scatterplot(x="petal_length",y="petal_width",data=iris)
plt.show()
