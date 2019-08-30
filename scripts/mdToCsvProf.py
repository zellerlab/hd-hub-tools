import os
import re
import csv

csv.register_dialect('myDialect', escapechar='@', delimiter = '`', quoting=csv.QUOTE_NONE)

with open("profiles.csv", "w+", newline='', encoding='utf-8') as csvFile:
    row = ['name', 'Description', 'image', 'Position', 'Address', 'Education', 'Scientific Experience', 'E-mail', 'Webpage']
    writer = csv.writer(csvFile, dialect = 'myDialect')
    writer.writerow(row)
    
    for filename in os.listdir("profiles"):
        with open("profiles/" + filename, newline='', encoding='utf-8') as file:
            row = [''] * 9
            
            line = file.readline()
            if("<figure" in line):
                row[2] = line
            
            while True:
                    if(not line):
                        break
                    if(line == '\n'):
                        line = file.readline()
                        continue
                        
                    if(re.match('^# .*', line) is not None):
                        row[0] = re.sub('# ', '', line)
                        row[0] = re.sub('\n', '', row[0])
                        line = file.readline()
                        
                    if('#### ' in line):
                        line = re.sub('#### ', '', line)
                        
                        if('Description' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                row[1] += line
                        if('Position' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[3] += line
                        if('Address' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[4] += line
                        if('Education' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[5] += line
                        if('Scientific Experience' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[6] += line
                        if('E-mail' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[7] += line
                        if('Webpage' in line):
                            while True:
                                line = file.readline()
                                if(not line or line[0] == '#' or line == '\n'):
                                    break
                                        
                                row[8] += line
                    
                    line = file.readline()
            
            writer.writerow(row)
            file.close()
            
    csvFile.close()
