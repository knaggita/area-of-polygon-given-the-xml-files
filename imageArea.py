__author__ = 'KEZIAH'
import xml.dom.minidom
import os

class ImageAreas(object):

   # loop through the folder and get only files ending with .xml 
    def loopThroughFolder(self):
        folderelements = []
        path = 'C:/Users/KEZIAH/Desktop/imagesFile'
        for filename in os.listdir(path):
            if not filename.endswith('.xml'):
                continue            
            folderelements.append(filename)   
        
        # print folderelements
        return folderelements

    def areas(self):
        imagedetails = []
        fileElements = []
        necrosisList = []
        image = []
        # instatiate ImageAreas class and use the loopthroughfolder method
        folder1 = ImageAreas()
        for xmlfiles in folder1.loopThroughFolder():

            DOMTree = xml.dom.minidom.parse(xmlfiles)
            printout = []
            wholeimagearea = 0           
            percentage = 0
            annotation = DOMTree.documentElement
            imageName = annotation.getElementsByTagName("filename")[0]
            ima = str(imageName.childNodes[0].data)
            
            print "Image Name: %s" % imageName.childNodes[0].data

            obj = annotation.getElementsByTagName("object")
            for objects in obj:

                name = objects.getElementsByTagName('name')[0]
               
                points = objects.getElementsByTagName("pt")

                # Print detail of each point.
                i = 0
                # contains x,y cordinates of anecrosis part of the image
                necrosisList = []
                # contains x,y cordinates of the whole image
                areaList = []
                part = []

                # get the x,y cordinates of the object from the xml file
                for point in points:
                    x = point.getElementsByTagName('x')[0]
                    Xcoord = int(x.childNodes[0].data)
                    y = point.getElementsByTagName('y')[0]
                    Ycoord = int(y.childNodes[0].data)
                    if (name.childNodes[0].data == 'necrosis') or (name.childNodes[0].data == 'nicosis') or (
                            name.childNodes[0].data == 'necosis'):                
                        necrosisList.append((Xcoord, Ycoord))
                        part = necrosisList

                    if name.childNodes[0].data == 'Area':
                        areaList.append((Xcoord, Ycoord))
                        part = areaList

                # calculate area of the polygon given the x,y cordinates
                sum1 = 0.0
                sum2 = 0.0
                count = len(points)

                for i in range(len(part) - 1):
                    sum1 = sum1 + part[i][0] * part[i + 1][1]                 
                for i in range(len(part) - 1):
                    sum2 = sum2 + part[i][1] * part[i + 1][0]                    
                area = (abs(sum1 - sum2) / 2.0)
                if part == necrosisList:
                    printout.append(area)
                    necrosisarea = sum(printout)
                if part == areaList:
                    wholeimagearea = area

            print "Area of the necrosis = %.1f" %  necrosisarea 
            print "Area the the image = %.1f" % wholeimagearea

            imagedetails.append(((ima),(necrosisarea), (wholeimagearea)))
       
        return imagedetails

    # write the image details to afile  

    def writetofile(self):

        folder1 = ImageAreas()
        images = open('imagesdetails.txt', 'a')  
        images.write('%-40s %10s %20s %20s \n' % ("IMAGE NAME", "NECROSIS AREA", "IMAGE AREA", "PERCENTAGE"))        
        for image in folder1. areas():            
            if image[2] > 0:
                percentage  = (image[1] / image[2]) * 100                
            if image[2] == 0:
                percentage  = 0.0                      
            images.write('%-40s %-23.1f %-20.1f %.1f \n' % (image[0], image[1], image[2], percentage))
            
            # print image
        images.close()

folder1 = ImageAreas()
folder1.writetofile()





    images.close()

