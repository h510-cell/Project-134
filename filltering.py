import csv
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("gravity.csv")
df.head()

#filtering the stars based on distance
filtering =[]
for d in df.Distance:
    if d<=100:
        filtering.append(True)
    else:
        filtering.append(False)

is_dist = pd.Series(filtering)

is_dist.head()

star_dist=df[is_dist]

star_dist.reset_index(inplace=True,drop=True)

star_dist.head()

star_dist.shape

#keep the stars having gravity similar to sun
gravity_filtering = []
for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_filtering.append(True)
    else :
        gravity_filtering.append(False)

is_gravity = pd.Series(gravity_filtering)

final_stars = star_dist[is_gravity]
final_stars.head()

final_stars.shape

final_stars.reset_index(inplace=True,drop=True)

final_stars.head()

final_stars.to_csv("filteringStars.csv")