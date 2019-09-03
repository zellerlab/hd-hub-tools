import os
import re
import csv

csv.register_dialect('myDialect', escapechar='$', delimiter = '`', quoting=csv.QUOTE_NONE)

with open(os.pardir + "/csv/tools.csv", "w+", newline='', encoding='utf-8') as csvFile:
    row = ['title', 'description', 'Homepage', 'Relevant Publications', 'Contact', 'Relevant Papers', 'Funding', 'Development', 'BioTools', 'Bioconda', 'Type of Material', 'Bioconductor', 'Open Slides', 'Open Course Material', 'category', 'Version']
    writer = csv.writer(csvFile, dialect = 'myDialect')
    writer.writerow(row)
    
    folders = ['de.nbi-epigenetics', 'HumanGeneticsAndGenomics', 'OnlineMaterial', 'SystematicPhenotyping']
    for foldername in folders:
        for filename in os.listdir(os.pardir + '/' + foldername):
            with open(os.pardir + '/' + foldername + '/' + filename, encoding='utf-8') as file:
                title = ''
                description = ''
                homepage = ''
                relevant_publications = ''
                contact = ''
                relevant_papers = ''
                funding = ''
                development = ''
                biotools = ''
                bioconda = ''
                type_of_material = ''
                bioconductor = ''
                open_slides = ''
                open_course_material = ''
                version = ''
            
                line = file.readline()
                line = re.sub('\n', '', line)
                title = re.sub('# ', '', line)
                
                while True:
                    line = file.readline()
                    if(not line or line[0] == '#'):
                        break
                            
                    description += line
                    
                while True:
                    if(not line):
                        break
                        
                    line = re.sub('#### ', '', line)
                    
                    if('Homepage' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                            homepage += line
                    if('Relevant Publications' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            relevant_publications += line
                    if('Contact' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            contact += line
                    if('Relevant Papers' in line or 'Relevant papers' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            relevant_papers += line
                    if('Funding' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            funding += line
                    if('Development' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            development += line
                    if('BioTools' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            biotools += line
                    if('Bioconda' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            bioconda += line
                    if('Type of Material' in line or 'Type of material' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            type_of_material += line
                    if('Bioconductor' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            bioconductor += line
                    if('Open Slides' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            open_slides += line
                    if('Open Course Material' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            open_course_material += line
                    if('Version' in line):
                        while True:
                            line = file.readline()
                            if(not line or line[0] == '#'):
                                break
                                    
                            version += line
                            
                row = [title, description, homepage, relevant_publications, contact, relevant_papers, funding, development, biotools, bioconda, type_of_material, bioconductor, open_slides, open_course_material, foldername, version]
                writer.writerow(row)
                
                file.close()
                
    csvFile.close()
            
                    
            