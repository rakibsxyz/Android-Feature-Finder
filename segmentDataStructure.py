class segment(object):
    activityNameList = []
    fragmentNameList = []
    methodStack = []
    packageameList = []
    methodNameList = []
    classNameList = []
    msLength = 0
    allPackageName= []
    


    # The class "constructor" - It's actually an initializer 
    def __init__(self, activityNameList, fragmentNameList, methodStack, packageameList, methodNameList, classNameList, allPackageName, msLength):
        self.activityNameList = activityNameList
        self.fragmentNameList = fragmentNameList
        self.methodStack = methodStack
        self.packageameList = packageameList
        self.methodNameList = methodNameList
        self.classNameList = classNameList
        self.msLength = msLength
        self.allPackageName = allPackageName

def createSegment(activityNameList, fragmentNameList, methodStack, packageameList, methodNameList, classNameList,allPackageName,msLength):
    segment = segment(activityNameList, fragmentNameList, methodStack,packageameList,methodNameList, classNameList,allPackageName,msLength)
    return segment