from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        '''Getting hash code for a word using a summation of
        the ASCII values and prime numbers taking ideas from
        Polynomial rolling hash functions'''
        prime = 31
        # Stort mod primtal för att hålla hash value inom en viss range
        mod = 10e9 + 7
        hash_val = 0
        for i, char in enumerate(word):
            hash_val += ord(char) * prime**i
            hash_val % mod
        return round(hash_val)

    # Doubles size of bucket list
    def rehash(self):
        copy_bucket = self.buckets
        self.buckets = [[] for i in range(self.bucket_list_size() * 2)]
        # Reset size
        self.size = 0
        for i in range(len(copy_bucket)):
            for element in copy_bucket[i]:
                self.add(element)

    # Adds a word to set if not already added
    def add(self, word):
        if self.size >= self.bucket_list_size():
            self.rehash()
        if not self.contains(word):
            word_index = self.get_hash(word) % self.bucket_list_size()
            self.buckets[word_index].append(word)
            self.size += 1

    # Returns a string representation of the set content
    def to_string(self):
        ret_str = "{ "
        for i in range(self.bucket_list_size()):
            if len(self.buckets[i]) > 0:
                for element in self.buckets[i]:
                    ret_str += element + " "
        ret_str += "}"
        return ret_str

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        index = self.get_hash(word) % len(self.buckets)
        for element in self.buckets[index]:
            if element == word:
                return True
        return False
        # Placeholder code ==> to be replaced

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        if self.contains(word):
            word_index = self.get_hash(word) % self.bucket_list_size()
            self.buckets[word_index].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max_size = 0
        for i in range(self.bucket_list_size()):
            bucket_len = len(self.buckets[i])
            if bucket_len > max_size:
                max_size = bucket_len
        return max_size

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        zero_buckets = 0
        for bucket in self.buckets:
            if len(bucket) == 0:
                zero_buckets += 1
        return zero_buckets / self.bucket_list_size()
