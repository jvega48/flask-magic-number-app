class EfficientMagicMath:
    def __init__(self):
        return

    def magicNumber(self, n, dictionary):
        result = 0
        
        if dictionary is None:
            dictionary = {}

        if n in dictionary:
            return dictionary[n]
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        result = n + self.magicNumber(n-1, dictionary) + self.magicNumber(n-2, dictionary)
        dictionary[n] = result
        
        return result
