#my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]
# def hashfunc(value):
#     sum_of_char=0
#     for char in value:
#         sum_of_char+=ord(char)
#     return sum_of_char % 10
# def contain(name):
#     index=hashfunc(name)
#     return my_hash_set[index]==name
# print(contain('Bob'))

my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]
def hash_function(value):
    return sum(ord(cher) for cher in value)%10
def add(value):
    index=hash_function(value)
    bucket=my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
def contain(value):
    index=hash_function(value)
    bucket=my_hash_set[index]
    return value in bucket
add('sai')
print(my_hash_set)
print(contain('sai'))