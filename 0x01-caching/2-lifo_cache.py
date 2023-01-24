#!/usr/bin/env python3
""" 0. Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ BasicCache defines """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.nbObjet = 1
        self.teteval = None
        self.queudval = None
        self.liste = None

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)['data']))

    def put(self, key, item):
        """
            - Must assign to the dictionary self.cache_data
                the item value for the key key.
            - If key or item is None, this method should not
                do anything.
            - If the number of items in self.cache_data is higher
                that BaseCaching.MAX_ITEMS:
                * you must discard the first item put in cache
                    (FIFO algorithm)
                * you must print DISCARD: with the key discarded and
                    following by a new line
        """

        if key not in self.cache_data and item is not None:
            if self.nbObjet > LIFOCache.MAX_ITEMS:
                sauve = self.teteval
                self.teteval = self.cache_data[self.teteval]['next']
                print('DISCARD:', sauve)
                self.cache_data.pop(sauve)

            noeud = {'data': item, 'next': None}

            if self.teteval is None:
                self.queudval = key
            else:
                noeud['next'] = self.teteval
                
            self.teteval = key
            self.cache_data[key] = noeud

        self.nbObjet += 1

    def get(self, key):
        """
            - Must return the value in self.cache_data linked to key.
            - If key is None or if the key doesn’t exist in self.cache_data,
                return None.
        """

        if key not in self.cache_data:
            return None
        if self.cache_data[key] is None:
            return None
        return self.cache_data[key]
