from bitarray import bitarray

import mmh3

class BloomFilter(set):
    def __init__(self,size,hash_count):
        #size:the num of the bitarray
        #hash_count:the num of hash function
        super(BloomFilter,self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0) #初始化为0
        self.size = size
        self.hash_count = hash_count

        def __len__(self):
            return self.size

        def __iter__(self):
            return iter(self.bit_array)

        def add(self,item):
            for i in range(self.hash_count):
                index = mmh3.hash(item,i) % self.size
                self.bit_array[index] = 1
            return self

        def __contains__(self,item):
            out = True
            for i in range(self.hash_count):
                index = mmh3.hash(item,i)%self.size
                if bit_array[index] == 0:
                    out = False
                    
            return out

def main():
    # bloom = BloomFilter(100,5)
    # animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
    #                'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
    #                'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
    # for animal in animals:
    #     bloom.add(animal)

    # for animal in animals:
    #     if animal in bloom:
    #         print("{} is in bloom filter".format(animal))
    #     else:
    #         print('Something is terribly went wrong for {}'.format(animal))
    #         print('FALSE NEGATIVE!')

    # other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
    #                      'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
    #                      'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
    #                      'hawk' ]
    # for other_animal in other_animals:
    #     if other_animal in bloom:
    #         print('{} is not in the bloom, but a false positive'.format(other_animal))
    #     else:
    #         print('{} is not in the bloom filter as expected'.format(other_animal))
    fd = open("urls.txt")  #有重复的网址 http://www.kalsey.com/tools/buttonmaker/  
    bloomfilter = BloomFilter(100,10)    
    while True:    
        url = fd.readline().strip()   
        if (url == 'exit') :  
            print ('complete and exit now')
            break    
        elif url not in bloomfilter:   
            bloomfilter.add(url)
            # print(url)    
        else:    
            print ('url :%s has exist' % url )

if __name__ == '__main__':
    main()
        
