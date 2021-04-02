from os import device_encoding
from segmentDataStructure import segment


def methodStackParser(line):
    newLine = line.replace('at ', '')

    newLine = newLine.split("(")
    return newLine[0]
    # just return method part


def splitLineAndFindActivityTokens(line):
    # print(line)

    line = line.split(".")
    packagename = line[1] + "." + line[2]
    type = line[3]
    activityName = line[4]
    methodName = line[len(line)-2].split("(")
    # print(methodName)
    # print(line, "\n")
    if(len(methodName) > 1):
        className = methodName[1]
    else:
        className = activityName
    # print(packagename+" --" + activityName + " "+ methodName[0]+ " "  + className + "\n")

    return packagename, activityName, methodName[0], className


def packageNameAndMethodNamePerser(line):
    line = line.split(".")
    packagename = line[1] + "." + line[2]
    # pkgname = line[3]
    activityName = line[3]
    # print(line)
    
    methodName = line[len(line)-2].split("(")
    if(len(line) > 6):
        methodName = line[5].split("(")
    # print(line)
    # print(line, "\n")
    if(len(methodName) > 1):
        className = methodName[1]
    else:
        className = activityName 
    if len(methodName) > 0: 
        totalString = packagename + " "+ activityName + " " +  methodName[0]
    else:
        totalString = packagename + " " + activityName

    return totalString, className, methodName[0], activityName

def createCsvHeader():
    f = open('testCsv.csv', 'w')
    f.write("activity,"+"fragment,"+"methodStact," +
            "packagename,"+"methodName,"+"className," +"allPackagMethodName," +"MSLength"+ "\n")
    f.close()

def writeCsv(segments):

    f = open('testCsv.csv', 'a')
    x = ""
    x = ' '.join(segments.activityNameList)
    x += "," + ' '.join(segments.fragmentNameList)
    x += "," + ' '.join(segments.methodStack)
    x += "," + ' '.join(segments.packageameList)
    # print(segments.methodNameList)
    x += "," + ' '.join(segments.methodNameList)
    # x +=","+ ''.join(str(v) for v in segments.methodNameList)
    x += "," + ' '.join(segments.classNameList)
    x += "," + ' '.join(segments.allPackageName)
    x += "," + str(segments.msLength)
    x += "\n"

    f.write(x)


# **********TouchEvent**********
# $$$$$$$$$$Id: preview
# $$$$$$$$$$Text:
# with open("traceTooSmall") as f:
# with open("traceSmall") as f:
def openTraceFileAndExecute(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        print(len(lines))

        segmentList = []
        activityNameList = []
        fragmentNameList = []
        methodStack = []
        packageameList = []
        methodNameList = []
        classNameList = []
        methodStackLength = 0
        allPackageName = []
        totalLines = len(lines)

        for i in range(0, totalLines):
            # check if starts of a method stack
            if "**********TouchEvent**********" in lines[i]:
                continue
            if "$$$$$$$$$$Id:" in lines[i]:
                continue
            if "$$$$$$$$$$Text" in lines[i]:
                continue
            if "java.lang.Throwable" in lines[i]:
                # print("Yooo Starts of a track")
                if i > 0:
                    if(len(activityNameList) == 0):
                        activityNameList.append("a x")
                    if(len(fragmentNameList) == 0):
                        fragmentNameList.append("f x")
                    if(len(classNameList) == 0):
                        classNameList.append("c x")

                    if(len(methodNameList) == 0):
                        methodNameList.append("m x")
                    if(len(methodStack) == 0):
                        methodStack.append("ms x")
                    if(len(allPackageName) == 0):
                        allPackageName.append("ap x")
            
                    # print(len(methodStack))
                    methodStackLength = len(methodStack)
                    # print(methodStackLength)
                    tempSegment = segment(activityNameList, fragmentNameList,
                                        methodStack, packageameList, methodNameList, classNameList,allPackageName,methodStackLength)
                    # segmentList.append(tempSegment)

                    writeCsv(tempSegment)
                    activityNameList.clear()
                    fragmentNameList.clear()
                    methodStack.clear()
                    packageameList.clear()
                    methodNameList.clear()
                    classNameList.clear()
                    allPackageName.clear()
                    methodStackLength = 0

            elif ".activity." in lines[i] or ".activities." in lines[i]:
                # print("Activity Found---", j)
                splitted = splitLineAndFindActivityTokens(lines[i])
                packageameList.append(splitted[0])
                activityNameList.append(splitted[1])
                methodNameList.append(splitted[2])
                classNameList.append(splitted[3])

            elif ".fragment." in lines[i]  or ".fragments." in lines[i]:
                # print("fragment Found in --", j)
                splitted = splitLineAndFindActivityTokens(lines[i])
                packageameList.append(splitted[0])
                fragmentNameList.append(splitted[1])
                methodNameList.append(splitted[2])
                classNameList.append(splitted[3])
            elif "at " in lines[i]:
                # print("got lines stack man")
                if "com." in lines[i] and "com.android.internal.os" not in lines[i] :
                    totalStringPkg, classNamePkg, methodNamePkg,activityNamePkg  = packageNameAndMethodNamePerser(lines[i])
                    # print(methodNamePkg)
                    allPackageName.append(totalStringPkg)
                    methodNameList.append(methodNamePkg)
                    classNameList.append(classNamePkg)
                    activityNameList.append(activityNamePkg)
                methodParsed = methodStackParser(lines[i])
                methodStack.append(methodParsed)
        if(len(activityNameList) == 0):
            activityNameList.append("a x")
        if(len(fragmentNameList) == 0):
            fragmentNameList.append("f x")
        if(len(classNameList) == 0):
            classNameList.append("c x")

        if(len(methodNameList) == 0):
            methodNameList.append("m x")
        if(len(methodStack) == 0):
            methodStack.append("ms x")
        if(len(allPackageName) == 0):
            allPackageName.append("ap x")

        print(len(methodStack))
        methodStackLength = len(methodStack)
        tempSegment = segment(activityNameList, fragmentNameList,
                                methodStack, packageameList, methodNameList, classNameList,allPackageName, methodStackLength)
        # segmentList.append(tempSegment)

        writeCsv(tempSegment)
        activityNameList.clear()
        fragmentNameList.clear()
        methodStack.clear()
        packageameList.clear()
        methodNameList.clear()
        classNameList.clear()
        allPackageName.clear()
        methodStackLength = 0

    f.close()
    # print(len(segmentList))
def readTraceAndParse(traceFileName):
    createCsvHeader()
    openTraceFileAndExecute(traceFileName)
    return True
    



# Fixed method fragments name
# added methodname and classNAme with package extraction for tutor app data