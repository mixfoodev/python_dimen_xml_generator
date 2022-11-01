import lxml.etree as ET
import os
from config import *

def make_dir(dirname):
    if(not os.path.exists(output_path + dirname)):
        os.mkdir(output_path + dirname)

def save_new_file(filename, tree):
    with open(filename,'wb') as t:
        tree.write(t)

def trim_float_string(value):
    # 20.00 -> 20
    if(value[-2:] == '00'):
        return value[:-3]
    # 20.50 -> 20.5
    if(value[-1:] == '0'):
        return value[:-1]
    return value

def edit_tree(tree, width):
    multiplier = width / source_width
    for dimen in tree.findall("dimen") :
        value = dimen.text[:-2]
        unit = dimen.text[-2:] # dp,sp etc.
        new_value = "{:.2f}".format(float(value) * multiplier)
        dimen.text = trim_float_string(new_value) + unit

def validate():
    if(not os.path.exists(output_path)):
        print("\nInvalid config! 'output_path':%s does not exist." % output_path)
        if input("Do you want to create it ? (y) or any key to cancel. ").lower() =='y':
            os.mkdir(output_path)
        else:
            exit()

    dict_msg = "\nInvalid config! 'folders_to_create' must be a list of dicts eg {'name':'sw360dp','width':360}.\nPlease check config.py"
    try:
        if (len(folders_to_create) == 0):
            print("\n'folders_to_create' list is empty.")
            exit()
        if(type(source_width) is not int):
            print("\nInvalid config!'source_width' must be an int.")
            exit()
    except SystemExit:
        exit()
    except:
        print(dict_msg)
        exit()
    
    for folder in folders_to_create:
        invalid_type = type(folder) is not dict
        invalid_keys = "name" not in folder or "width" not in folder
        if invalid_type or invalid_keys:
            print(dict_msg)
            exit()
    try:
        tree = ET.parse(source_xml)
    except :
        print("\nError! Could not parse source xml file!")
        exit()  
        
    if(len(tree.findall("dimen")) == 0):
        print("\nNo dimens found in source xml file!")
        exit() 

def run():
    for folder in folders_to_create:     
        tree = ET.parse(source_xml)
        cur_width = folder['width']
        current_folder = 'values-' + folder['name']
        make_dir(current_folder)
        filename = output_path + current_folder + os.path.sep + 'dimens.xml'
        if os.path.exists(filename) and not OVERRIDE_EXISTING_FILES:
            print("\n%s already exists and will be skipped. If you want to override existing files change 'OVERRIDE_EXISTING_FILES' to True in config.py" %
            filename)
            continue
        edit_tree(tree, cur_width)
        save_new_file(filename, tree)

if (__name__ == "__main__"):
    validate()
    run()
    print('Completed . .')

