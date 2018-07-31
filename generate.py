import pandas as pd
import random
from datetime import datetime
from sklearn.utils import shuffle




#####generate random age#########
def gen_random_age(num, young):

	ages = []

	if young == True:

		for x in range(num):
			ages.append(random.randint(18, 23))


	else:
		for x in range(num):
			ages.append(random.randint(18, 55))

	return ages



###generate random time###########
def gen_random_time(num, sus):
	
	times =[]

	for x in range(num):

		year = random.randint(2007, 2018)

		month = random.randint(1, 12)

		day = random.randint(1, 28)

		if sus == True:

			hour = random.randint(16, 23)

			minute = random.randint(1, 59)


		else:

			hour = random.randint(1, 23)

			minute = random.randint(1, 59)


		times.append(datetime(year, month, day, hour, minute))
		

	return times	

def assign_random_location(num, sus):

	final = []

	for x in range(num):

		if sus == True:

			locations = ['40.712775, -74.005973', '39.952584, -75.165222', '42.360082, -71.05888', '39.290385, -76.612189']

			location = locations[random.randint(0,3)]

		else:

			locations = ['40.712775, -74.005973', '39.952584, -75.165222', '42.360082, -71.05888',
						 '39.290385, -76.612189', '30.267153, -97.743061', '32.776664, -96.796988',
						  '37.774929, -122.419416', '34.052234, -118.243685', '36.169941, -115.13983']

			location = locations[random.randint(0, 8)]

		final.append(location)

	return final




def gen_random_length(num, sus):

	final = []


	for x in range(num):

		if sus == True:

			final.append(random.randint(40, 150))

		else:

			final.append(random.randint(40, 350))

	return final







df_sus = pd.DataFrame()

df_sus['age'] = gen_random_age(60, True)
df_sus['time'] = gen_random_time(60, True)
df_sus['location'] = assign_random_location(60, True)
df_sus['length'] = gen_random_length(60, True)


df = pd.DataFrame()

df['age'] = gen_random_age(100, False)
df['time'] = gen_random_time(100, False)
df['location'] = assign_random_location(100, False)
df['length'] = gen_random_length(100, False)



df = pd.concat([df, df_sus], axis=0)

df = shuffle(df)

df.to_csv('trafficking.csv')




