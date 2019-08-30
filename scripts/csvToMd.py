import os
import re
import csv

csv.register_dialect('myDialect', escapechar='@', delimiter = '`', quoting=csv.QUOTE_NONE)

with open("tools.csv", "r", encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile, dialect = 'myDialect')
    
    fields = []
    i = 0
    for row in reader:
        if(i == 0):
            fields = row
        
        else:
            title = row[0]
            description = row[1]
            category = row[14]
            
            if not os.path.exists("generated_" + category):
                os.makedirs("generated_" + category)
            with open("generated_" + category + "/" + title + ".md", "w+", encoding='utf-8') as mdFile:
                mdFile.write("# " + title + "\n")
                mdFile.write(description + "\n")
                
                j = 0
                for field in row:
                    if(j >= 2 and field != '' and field != category):
                        mdFile.write("#### " + fields[j] + "\n")
                        mdFile.write(field + "\n")
                        
                    j = j + 1
                    
                mdFile.close()
        
        i = i + 1
    
    csvFile.close()
