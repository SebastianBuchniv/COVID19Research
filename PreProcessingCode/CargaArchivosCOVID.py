import io
import os
import csv
#Root directory to work with. The files are TEXT files, with data ate the TOP, and some trash data in the bottom.
#I will process each file, and generate a new one with the summarized data i need for my investigation.
RootDir = 'C:/Sebas/DataSets/PoblacionEEUU/'

#Open in write mode the final CSV 
with open('EEUUPopulation.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	#Fetch the data in the directory
	with os.scandir(RootDir) as entries:
		#Iterate throu files
		for entry in entries:
			#Read the file
			with open(RootDir+entry.name) as inp:
				Estado = entry.name.replace(".txt","")
				Cantidad = 0
				#Iterate throw lines in the files.
				for line in inp:
					arr = line.split("\t")
					arr.insert(0,entry.name.replace(".txt",""))
					#Break if i reach the end of the data in the RAW files.
					if "---" in arr[1]:
						break
					arr[3] = arr[3].replace("\"","").replace("+","")
					arr[4] = arr[4].replace("\n","")
					#Ignore titles, and only count population over 65 , and don't count the 85+ because it's a wrong estimation.
					#Instead duplicate de 84 age group.
					if arr[3] != "Age Code":
						if int(arr[3]) > 65 and int(arr[3]) < 85:
							if int(arr[3]) == 84:
								Cantidad = Cantidad + int(arr[4])*2
							else:
								Cantidad = Cantidad + int(arr[4])
				#Write the row with the acumulated data.
				writer.writerow([Estado,Cantidad])

