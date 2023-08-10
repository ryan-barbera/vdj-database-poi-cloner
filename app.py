import shutil
import xml.etree.ElementTree as ET



    

def main():
    base_path = 'C:\\Users\\Masque\\Code\\VDJ-database-poi-cloner\\base\\database.xml'
    source_path = 'C:\\Users\\Masque\\Code\\VDJ-database-poi-cloner\\source\\database.xml'
    output_path = 'C:\\Users\\Masque\\Code\\VDJ-database-poi-cloner\\output\\database.xml'

    
    shutil.copy(base_path,output_path )

    source_tree = ET.parse(source_path)
    source_root = source_tree.getroot()
    #output_tree = ET.parse(output_path)
    
    for x in source_root[0]:
        #tagname= x.getElementsByTagName('T')[0]

        #print(x.tag, x.attrib)
        #print(x.find('Tags'))
        break
    
    
    print('Read Source_Tree...')
    for x in source_root.iter('Tags'):
        print(x.attrib.get('Author'))
        print(x.attrib.get('Title'))
        #author = x.attributes['Author'].text
        #title = x.attributes['Title'].text
        
        #print(author + ' ' + title)
    print('Done!')

if __name__ == "__main__":
    main()