class Codec:
    def __init__(self):
        self.ht = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        count = self.count
        self.ht[count] = longUrl
        self.count += 1
        
        return "http://tinyurl.com/" + str(count)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = int(shortUrl.replace("http://tinyurl.com/", ""))
        
        return self.ht.get(key)