import matplotlib.pyplot as plt
import seaborn as sns
print("--DATASETS GIVEN IN THE SEABORN--\n",sns.get_dataset_names())
iris=sns.load_dataset("iris")
print("-----IRIS DATASET HEAD-----\n",iris.head())
anagrams=sns.load_dataset("anagrams")
print("-----ANAGRAMS DATASET HEAD----\n",anagrams.head())
print("---IRIS DATASET----\n",iris.count())
print("-----ANAGRAMS DATASET----\n",anagrams.count())
