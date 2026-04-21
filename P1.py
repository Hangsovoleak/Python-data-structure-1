# =============================================================================
#  PYTHON DATA STRUCTURES — COMPLETE STUDY REFERENCE
#  Topics: Types, Booleans, Strings, Range, Lists, Tuples,
#          Dictionaries, Sets, Operators, Collections Module
# =============================================================================


# -----------------------------------------------------------------------------
# 1. DATA TYPES
#    Every value in Python has a type. Use type() to inspect it.
#    Variables are dynamic — reassigning changes the type automatically.
# -----------------------------------------------------------------------------

p = "Hello Me"          # str     — text / characters
q = 10                  # int     — whole number
r = 3.14                # float   — decimal number
c = 12 + 31j            # complex — real + imaginary part

print(type(p))          # <class 'str'>
print(type(q))          # <class 'int'>
print(type(r))          # <class 'float'>
print(type(c))          # <class 'complex'>

# Variables are dynamic — type follows the assigned value
var = 31.2                        # float
print(type(var))                  # <class 'float'>

var = "Now the type is string"    # reassigned → now str
print(type(var))                  # <class 'str'>

var = 13.2
print(var)                        # 13.2


# -----------------------------------------------------------------------------
# 2. BOOLEANS
#    Holds only True or False.
#    Falsy values  → 0, 0.0, "", None, False, empty containers
#    Truthy values → everything else (non-zero, non-empty)
# -----------------------------------------------------------------------------

print(type(bool(22)))   # <class 'bool'>
print(type(True))       # <class 'bool'>
print(type(False))      # <class 'bool'>

print(bool(False))      # False
print(bool(0))          # False  ← zero is falsy
print(bool(11))         # True   ← non-zero is truthy
print(bool(-2.3))       # True   ← negative numbers are truthy


# -----------------------------------------------------------------------------
# 3. STRINGS
#    Ordered, immutable sequence of characters.
#    Supports concatenation (+) and repetition (*).
# -----------------------------------------------------------------------------

str1 = 'Hello how are you'    # single quotes
str2 = "Hello how are you"    # double quotes — identical result
str3 = 'multi' + 'line'       # concatenation with +

print(str1)
print(str2)
print(str3)

# Concatenation
f = 'data'
s = 'structure'
print(f + s)              # 'datastructure'
print('Data' + 'structure')

# Repetition
st = 'data.'
print(st * 3)             # 'data.data.data.'
print(3 * st)             # same result


# -----------------------------------------------------------------------------
# 4. RANGE
#    Generates a lazy sequence of integers.
#    Syntax: range(start, stop, step)  — stop is EXCLUSIVE
#    Wrap in list() to see all values at once.
# -----------------------------------------------------------------------------

print(list(range(10)))           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))           # same as above
print(list(range(1, 10, 2)))     # [1, 3, 5, 7, 9]  — odd numbers
print(list(range(20, 10, -2)))   # [20, 18, 16, 14, 12]  — countdown


# -----------------------------------------------------------------------------
# 5. LISTS
#    Ordered, mutable sequence. Can hold mixed types.
#    Supports indexing, slicing, and in-place modification.
# -----------------------------------------------------------------------------

a = ['food', 'bus', 'apple', 'queen']
print(a)

mylist = [10, "Me", "World", 8]
print(mylist[1])          # "Me"  — zero-based index

# Order matters — these are NOT equal
print([10, 12, 31, 14] == [14, 10, 31, 12])   # False

# --- Mutation ---
b = ['data', 'and', 'book', 'structure', 'hello', 'st']
b += [32]           # append element
print(b)

b[2:3] = []         # delete a slice
print(b)

del b[0]            # delete by index
print(b)

# --- Mixed types allowed ---
a = [2.2, 'python', 31, 41, 'data', False, 33.59]
print(a)

# --- Indexing & Slicing ---
a = ['data', 'structure', 'using', 'python', 'happy', 'learning']
print(a[0])         # 'data'        ← first element
print(a[2])         # 'using'
print(a[-1])        # 'learning'    ← last element
print(a[-5])        # 'structure'

print(a[1:5])       # ['structure', 'using', 'python', 'happy']
print(a[-3:-1])     # ['python', 'happy']

# --- In-place modification ---
a = ['data', 'and', 'book', 'structure', 'hello', 'st']
a[1]  = 1           # replace single element
a[-1] = 120         # replace last element
print(a)

a = ['data', 'and', 'book', 'structure', 'hello', 'st']
print(a[2:5])
a[2:5] = [1, 2, 3, 4, 5]   # replace a slice with more elements
print(a)


# -----------------------------------------------------------------------------
# 6. OPERATORS — MEMBERSHIP, IDENTITY, LOGICAL
# -----------------------------------------------------------------------------

# --- Membership operators: in / not in ---
a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print('data' in a)          # True

mylist1 = [100, 20, 30]
mylist2 = [10, 50, 60]
if mylist1[1] in mylist2:
    print("elements are overlapping")
else:
    print("elements are not overlapping")   # prints this

val = 104
mylist = [100, 210, 430, 840]
if val not in mylist:
    print("val is NOT present in mylist")   # prints this
else:
    print("val is present in mylist")

# --- Identity operators: is / is not ---
# 'is' checks if two variables point to the SAME object in memory
# '==' checks if two variables have the SAME contents
FirstList  = []
SecondList = []

if FirstList == SecondList:
    print("Both are equal")                             # prints this
if FirstList is SecondList:
    print("Both variables point to the same object")
else:
    print("Both variables are NOT the same object")     # prints this

thirdList = FirstList                                   # same reference
if thirdList is FirstList:
    print("Both point to the same object")              # prints this

# 'is not'
if FirstList is not SecondList:
    print("Different objects in memory")                # prints this

# --- Logical operators: and / or / not ---
a = 67
b = 76

if a > 0 and b > 0:
    print("Both a and b are greater than zero")

if a > 0 or b > 0:
    print("At least one is greater than zero")

if not a:
    print("Boolean value of a is False")
else:
    print("Boolean value of a is True")                 # prints this


# -----------------------------------------------------------------------------
# 7. TUPLES
#    Ordered, IMMUTABLE sequence — like a list you cannot change.
#    Useful for fixed data, return values, and dictionary keys.
# -----------------------------------------------------------------------------

tupleName = ("entry1", "entry2", "entry3")
myTuple   = ("shyam", 23, True, "female")

print((4, 5) + (10, 20))           # (4, 5, 10, 20)  — concatenation
print((2, 1) * 3)                  # (2, 1, 2, 1, 2, 1)  — repetition
print(3 in ('hi', 'xyz', 3))       # True  — membership test

for p in (6, 7, 8):
    print(p)

x = ('hello', 'world', 'india')
print(x[1])     # 'world'
print(x[-2])    # 'world'
print(x[1:])    # ('world', 'india')


# -----------------------------------------------------------------------------
# 8. DICTIONARIES
#    Collection of key → value pairs.
#    Keys must be unique and immutable. Values can be anything.
#    Very fast O(1) lookups by key.
# -----------------------------------------------------------------------------

my_dict = {
    '1': 'Data',
    '2': 'Structure',
    '3': 'Python',
    '4': 'Programming'
}

# --- Building a dict dynamically ---
person = {}
print(type(person))         # <class 'dict'>

person['name']     = 'ABC'
person['lastname'] = 'XYZ'
person['age']      = 31
person['address']  = ['Jaipur']

print(person)
print(person['name'])       # 'ABC'

print('name'  in person)    # True   — key exists
print('fname' not in person)# True   — key absent
print(len(person))          # 4

# --- Common dictionary methods ---
mydict = {'a': 1, 'b': 2, 'c': 3}

mydict.get('b')     # 2    — safe get, no KeyError if missing
mydict.get('z')     # None — missing key returns None

print(list(mydict.items()))     # [('a',1), ('b',2), ('c',3)]
print(list(mydict.keys()))      # ['a', 'b', 'c']
print(list(mydict.values()))    # [1, 2, 3]

print(mydict.pop('b'))          # 2  — removes 'b' and returns its value
print(mydict)                   # {'a': 1, 'c': 3}

mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict.popitem())         # ('c', 3)  — removes last inserted pair
print(mydict)                   # {'a': 1, 'b': 2}

# merge d2 into d1 (d2 values overwrite on collision)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)   # {'a': 10, 'b': 200, 'c': 30, 'd': 400}

mydict.clear()
print(mydict)   # {}


# -----------------------------------------------------------------------------
# 9. SETS
#    Unordered collection of UNIQUE values — duplicates auto-removed.
#    Ideal for membership testing and set math operations.
# -----------------------------------------------------------------------------

x1 = set(['and', 'python', 'data', 'structure'])
print(x1)           # {'and', 'python', 'data', 'structure'}
print(type(x1))     # <class 'set'>

x2 = {'and', 'python', 'data', 'structure'}    # literal syntax
print(x2)

x = {'data', 'structure', 'and', 'python'}
print(len(x))               # 4
print('structure' in x)     # True

x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

# Union — all elements from both sets
print(x1 | x2)                      # {'java','structure','c','python','data'}
print(x1.union(x2))                 # same result

# Intersection — elements present in BOTH sets
print(x1.intersection(x2))          # {'data'}
print(x1 & x2)                      # {'data'}

# Difference — elements in x1 but NOT in x2
print(x1.difference(x2))            # {'structure'}
print(x1 - x2)                      # {'structure'}

# Symmetric difference — elements in one but NOT both
print(x1.symmetric_difference(x2))  # {'structure','python','c','java'}
print(x1 ^ x2)                      # same result

# Subset check — is every element of x1 inside x2?
print(x1.issubset(x2))  # False
print(x1 <= x2)         # False

# --- frozenset — immutable version of a set ---
x = frozenset(['data', 'structure', 'and', 'python'])
print(x)

# frozensets can be used inside another set (regular sets cannot)
a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x  = {a1, a2, a3}
print(x)


# =============================================================================
# 10. COLLECTIONS MODULE — ADVANCED CONTAINER TYPES
#     Specialised containers that extend Python's built-ins.
# =============================================================================

# -----------------------------------------------------------------------------
# 10a. namedtuple — a tuple with named fields
#      Access elements by index OR by name (more readable).
# -----------------------------------------------------------------------------

from collections import namedtuple

Book  = namedtuple('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book('Hands on Data Structures', '9781788995573', '50')

print('Using index ISBN: ' + Book1[1])   # '9781788995573'
print('Using key ISBN: '   + Book1.ISBN) # '9781788995573'


# -----------------------------------------------------------------------------
# 10b. deque — double-ended queue
#      O(1) appends and pops from BOTH ends (lists are O(n) on the left).
# -----------------------------------------------------------------------------

from collections import deque

s        = deque()                 # empty deque
my_queue = deque([1, 2, 'Name'])
print(my_queue)                    # deque([1, 2, 'Name'])

my_queue.append('age')             # add to right end
print(my_queue)

my_queue.appendleft('age')         # add to left end
print(my_queue)

my_queue.pop()                     # remove from right
print(my_queue)

my_queue.popleft()                 # remove from left
print(my_queue)


# -----------------------------------------------------------------------------
# 10c. OrderedDict — dict that remembers insertion order
#      (In Python 3.7+ regular dicts also preserve order, but
#       OrderedDict provides extra order-related methods.)
# -----------------------------------------------------------------------------

from collections import OrderedDict

od = OrderedDict({'my': 2, 'name': 4, 'is': 2, 'Mohan': 5})
od['hello'] = 4
print(od)


# -----------------------------------------------------------------------------
# 10d. defaultdict — dict with automatic default values
#      Missing keys are created automatically using the factory function.
# -----------------------------------------------------------------------------

from collections import defaultdict

dd    = defaultdict(int)   # missing keys default to 0 (int())
words = str.split('data python data data structure data python')

for word in words:
    dd[word] += 1

print(dd)   # defaultdict(<class 'int'>, {'data':4, 'python':2, 'structure':1})


# -----------------------------------------------------------------------------
# 10e. ChainMap — logical merge of multiple dicts (no copying)
#      Searches dicts left-to-right; the first match wins.
# -----------------------------------------------------------------------------

from collections import ChainMap

dict1 = {"data": 1, "structure": 2}
dict2 = {"python": 3, "language": 4}
chain = ChainMap(dict1, dict2)

print(chain)                    # ChainMap({'data':1,'structure':2}, {'python':3,'language':4})
print(list(chain.keys()))       # ['python', 'language', 'data', 'structure']
print(list(chain.values()))     # [3, 4, 1, 2]
print(chain["data"])            # 1  — found in dict1
print(chain["language"])        # 4  — found in dict2


# -----------------------------------------------------------------------------
# 10f. Counter — count occurrences of elements
#      Returns a dict-like object with elements as keys, counts as values.
# -----------------------------------------------------------------------------

from collections import Counter

inventory = Counter('hello')
print(inventory)   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})


# -----------------------------------------------------------------------------
# 10g. UserString — create custom string subclasses
#      Inherit from UserString to add or override string methods safely.
# -----------------------------------------------------------------------------

from collections import UserString

class MyString(UserString):
    def append(self, value):
        self.data += value       # adds a custom .append() method

s1 = MyString("data")
print("Original:     ", s1)     # 'data'

s1.append('h')
print("After append: ", s1)     # 'datah'


# =============================================================================
# END OF FILE
# =============================================================================