import os

## SETTINGS ##

# The folders that will be generated. Replace with yours.
folders_to_create = [
    {'name':'sw360dp','width':360},
    {'name':'sw480dp','width':480},
    {'name':'sw600dp','width':600},
    {'name':'sw800dp','width':800},
]

# Source xml with current values. Replace it with yours.
# eg ..\yourProject\app\src\main\res\values\dimens.xml
source_xml ='sample.xml' 

# Source xml sw-width. The rest of dimens will be calculated based on this value. Replace it with yours.
source_width = 320

# The output folder where you want to save the generated files. Replace it with yours.
#eg ..\yourProject\app\src\main\res\values\
output_path = os.path.abspath(os.getcwd()) + os.path.sep + "sample_output_folder" + os.path.sep

# Set to True if you want existing files to be overriden.
OVERRIDE_EXISTING_FILES = False
