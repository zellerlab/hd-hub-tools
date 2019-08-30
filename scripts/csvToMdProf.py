import os
import re
import csv

csv.register_dialect('myDialect', escapechar='@', delimiter = '`', quoting=csv.QUOTE_NONE)

with open("profiles.csv", "r", encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile, dialect = 'myDialect')
    
    fields = []
    i = 0
    for row in reader:
        if(i == 0):
            fields = row
        
        else:
            name = row[0]
            
            if not os.path.exists("generated_profiles"):
                os.makedirs("generated_profiles")
            with open("generated_profiles/" + name + ".md", "w+", encoding='utf-8') as mdFile:
                if(row[2] != ''):
                    mdFile.write(row[2] + "\n")
            
                mdFile.write("# " + name + "\n\n")
                
                j = 0
                for field in row:
                    if(j >= 1 and j != 2 and field != ''):
                        mdFile.write("#### " + fields[j] + "\n")
                        mdFile.write(field + "\n")
                        
                    j = j + 1
                    
                mdFile.close()
        
        i = i + 1
    
    csvFile.close()
