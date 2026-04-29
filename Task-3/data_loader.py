import os
import xml.etree.ElementTree as et

def load_xml(path):

   
    
    if not os.path.exists(path):
        print("DEBUG: Folder does not exist!")
        return []
    
    texts=[]
    base_dir=os.path.dirname(os.path.abspath(__file__))
    full_path=os.path.join(base_dir, path)
    print(f"Debug: Looking in absolute path: {full_path}")
    for filename in os.listdir(full_path):
        if filename.endswith(".xml"):
            p=os.path.join(full_path, filename)
            try:
                tree=et.parse(p)
                root=tree.getroot()
                file_pairs=0
                for qa in root.findall('.//QAPair'):
                    question=qa.find('Question').text if qa.find('Question') is not None else ""
                    answer=qa.find('Answer').text if qa.find('Answer') is not None else ""
                    if question or answer:
                        texts.append(f"Question: {question} \nAnswer: {answer}")
                        file_pairs+=1
                print(f"Found {file_pairs} pairs!")
            except Exception as e:
                print(f"Skipping {filename}: {e}")
    return texts

