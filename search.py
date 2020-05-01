import pandas as pd

# load the dataset
anime_data = pd.read_csv("Anime Recommendation.csv")

# input your favorite anime
print("Give me one anime title: ", end='')
base_anime = input()

# input your anime
if base_anime in list(anime_data['Anime']) :
    idx = list(anime_data['Anime']).index(base_anime)

# search for your anime
arr_result = []
anime_recommendation = anime_data['Recommendation'][idx].replace("[",'').replace("]",'').replace("'","").split(",")
# anime_reasoning = anime_data['Reasoning'][idx].replace("[",'').replace("]",'').replace("'","").split(",")
anime_power = anime_data['Recommendation Power'][idx].replace("[",'').replace("]",'').replace("'","").replace(" ", "").split(",")
for i in range(len(anime_recommendation)) :
    arr_result.append(anime_power[i] + " | " + anime_recommendation[i])
arr_result = sorted(arr_result, reverse=True)

# print
print("If you like " + base_anime + ", try this :")
for recommendation in arr_result :
    print(recommendation)
