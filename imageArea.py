__author__ = 'Keziah Blessing'
import xml.dom.minidom
import os

path = 'C:/Users/Keziah Blessing/Desktop/imagesFile'
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue

    images = open('image.txt', 'a+')
    # images.write('%-40s %10s %20s %20s \n' % ("IMAGE NAME", "NECROSIS AREA", "IMAGE AREA", "PERCENTAGE"))
    images.close()
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(filename)
    printout = []
    a = 0
    a2 = 0
    a3 = 0
    percentage = 0
    annotation = DOMTree.documentElement
    imageName = annotation.getElementsByTagName("filename")[0]
    ima = str(imageName.childNodes[0].data)
    # printout.append(ima)
    print "Image Name: %s" % imageName.childNodes[0].data

    obj = annotation.getElementsByTagName("object")
    for objects in obj:

        name = objects.getElementsByTagName('name')[0]
        # print "name: %s" % name.childNodes[0].data

        if (name.childNodes[0].data == 'necrosis') or (name.childNodes[0].data == 'nicosis') or (
                    name.childNodes[0].data == 'necosis'):

            points = objects.getElementsByTagName("pt")

            # Print detail of each point.
            i = 0
            necrosisList = []
            for point in points:
                x = point.getElementsByTagName('x')[0]
                Xcoord = int(x.childNodes[0].data)
                y = point.getElementsByTagName('y')[0]
                Ycoord = int(y.childNodes[0].data)

                necrosisList.append((Xcoord, Ycoord))

            sum1 = 0.0
            sum2 = 0.0
            b = len(points)

            for i in range(len(necrosisList) - 1):
                sum1 = sum1 + necrosisList[i][0] * necrosisList[i + 1][1]
                # print str(matrix[i][0]) +'*'+str(matrix[i+1][1]) +'='+str(matrix[i][0]*matrix[i+1][1]);
            for i in range(len(necrosisList) - 1):
                sum2 = sum2 + necrosisList[i][1] * necrosisList[i + 1][0]
                # print str(matrix[i][1]) +'*'+str(matrix[i+1][0]) +'='+str(matrix[i][1]*matrix[i+1][0]);
            area = (abs(sum1 - sum2) / 2.0)
            a = area
            printout.append(a)
            print "Area of the necrosis = %.1f" % a

        if name.childNodes[0].data == 'Area':
            points = objects.getElementsByTagName("pt")

            # Print detail of each point.
            AreaList = []
            for point in points:
                x = point.getElementsByTagName('x')[0]
                xcoor = int(x.childNodes[0].data)
                y = point.getElementsByTagName('y')[0]
                ycoor = int(y.childNodes[0].data)
                AreaList.append((xcoor, ycoor))

            sum1 = 0.0
            sum2 = 0.0
            count = len(points)

            for i in range(len(AreaList) - 1):
                sum1 = sum1 + AreaList[i][0] * AreaList[i + 1][1]
                # print str(matrix[i][0]) +'*'+str(matrix[i+1][1]) +'='+str(matrix[i][0]*matrix[i+1][1]);
            for i in range(len(AreaList) - 1):
                sum2 = sum2 + AreaList[i][1] * AreaList[i + 1][0]
                # print str(matrix[i][1]) +'*'+str(matrix[i+1][0]) +'='+str(matrix[i][1]*matrix[i+1][0]);
            area = (abs(sum1 - sum2) / 2.0)
            a2 = area
            print "Area the whole image = %.1f" % a2
            # printout.append(a2)

    print printout
    print sum(printout)

    if a2 > 0:
        percentage = (sum(printout) / a2) * 100

    images = open('image.txt', 'a')
    images.write('%-40s %-23.1f %-20.1f %.1f \n' % (imageName.childNodes[0].data, sum(printout), a2, percentage))

    images.close()

