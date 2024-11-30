class Hashset:
    def __init__(self,size=100):
        self.size=size
        self.buckets=[[] for _ in range(size)]
    def hashfunc(self,value):
        return sum(ord(cher) for cher in value) % self.size
    def add(self,value):
        index=self.hashfunc(value)
        bucket=self.buckets[index]
        if value not in bucket:
            bucket.append(value)
    def contain(self,value):
        index=self.hashfunc(value)
        bucket=self.buckets[index]
        return value in bucket
    def remove(self,value):
        index=self.hashfunc(value)
        bucket=self.buckets[index]
        if value in bucket:
            bucket.remove(value)
    def printset(self):
        for index,bucket in enumerate(self.buckets):
            print(f"bucket:{index}:{bucket}")
hash_set=Hashset(size=10)
hash_set.add('sai')
hash_set.add('raju')
hash_set.add('arvind')
hash_set.add('venu')
hash_set.add('uday') 

print(hash_set.printset())
hash_set.remove('raju')
print(hash_set.hashfunc('venu'))
print(hash_set.contain('raju'))