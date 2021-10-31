import pandas as pd 

df = pd.read_csv("filtered_data.csv")

star_name = df["Star_name"].to_list()
distance = df["Distance"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()

final_star_list=[]
for i in range(0,len(star_name)):
    temp_dict = {
        "name": star_name[i],
        "mass": mass[i],
        "distance": distance[i],
        "radius": radius[i],
        "gravity": gravity[i]
    }
    final_star_list.append(temp_dict)

print(final_star_list)