import os
import shutil

# Script that moves annotated images with the labelImg tool from the all images folder to the annotated images folder
def moveAnnotations():
    imagesFolder = os.path.join('workspace','images','all')
    newImagesFolder = os.path.join('workspace','images','all','annotated')
    counter = 0
    for filename in os.listdir(imagesFolder):
        if filename.endswith(".jpg"):
            filename_no_ext = filename.split(".jpg")[0]
            xml_filename = filename_no_ext+".xml"
            # if a xml file with the same name exists, the image has been annotated
            if os.path.exists(os.path.join(imagesFolder,xml_filename)):
                counter += 1
                shutil.copy(os.path.join(imagesFolder,filename), newImagesFolder)
                shutil.copy(os.path.join(imagesFolder,xml_filename), newImagesFolder)
    print("You have annotated " + str(counter) + " images...")

# allowing the possibility to call the script via terminal
if __name__ == "__main__":
    moveAnnotations()