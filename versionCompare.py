def compareVersion(version1, version2):
    
    v1 = version1.split('.')
    v2 = version2.split('.')

    l = min(len(v1), len(v2))
    i = 0

    while i < l:
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
        else:
            i += 1

    if len(v1) > len(v2):
        while i < len(v1):
            if int(v1[i]) > 0:
                return 1
            i += 1

    elif len(v1) < len(v2):
        print "Get in here"
        while i < len(v2):
            if int(v2[i]) > 0:
                return -1
            i += 1

    return 0