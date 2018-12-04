class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            # Set first occurance index as mapping
            # aabbccd -> 1122334
            # ffgghhi -> 1122334
            if not s[i] in mapS:
                mapS[s[i]] = i

            if not t[i] in mapT:
                mapT[t[i]] = i

            # Saw different index, not isomorphic
            if mapS[s[i]] != mapT[t[i]]:
                return False

        return True


def groupIsomorphic(strs):
    import collections
    res = collections.defaultdict(list)

    for s in strs:
        ht = {}
        idx = ''

        for i in range(len(s)):
            if not s[i] in ht:
                ht[s[i]] = i
            idx += str(ht[s[i]])
        res[idx].append(s)

    return res.values()
