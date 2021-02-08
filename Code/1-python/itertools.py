import itertools
import operator

data = [1, 3, 5, 7, 12, 2]
data2 = [(2, 6), (8, 4), (7, 3)]  # iterable of iterables
shapes = ["circle", "sqare", "rectangle"]
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
]
selections = [True, False, True]
robots = [
    {
        "name": "blaster",
        "faction": "autobot"
    },
    {
        "name": "galvatron",
        "faction": "decepticon"
    },
    {
        "name": "jazz",
        "faction": "autobot"
    },
    {
        "name": "metroplex",
        "faction": "autobot"
    },
    {
        "name": "megatron",
        "faction": "decepticon"
    },
    {
        "name": "starcream",
        "faction": "decepticon"
    },
]

print("Accumulate: Makes an iterator that returns the results of a function.")
for i in itertools.accumulate(data, operator.mul):
    print(i)

print(
    "\nCombinations: Takes an iterable and a integer. This will create all the unique combination that have r members."
)
for s in itertools.combinations(shapes, 2):
    print(s)

print(
    "\nCombinations with replacements: allows individual elements to be repeated more than once."
)
shapes = ["circle", "sqare", "rectangle"]
for s in itertools.combinations_with_replacement(shapes, 3):
    print(s)

print("\nCounts.")
for i in itertools.count(start=10, step=3):
    print(i)
    if i > 20:
        break

print("\ncycle(): This function cycles through an iterator endlessly.")
for s in itertools.cycle(shapes):
    print(s)
    break

print(
    "\nchain(): Take a series of iterables and return them as one long iterable."
)
for each in itertools.chain(shapes, data):
    print(each)

print("\ncompress(): Filters one iterable with another.")
for i in itertools.compress(shapes, selections):
    print(i)

print(
    "\ndropwhile(): Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element."
)
for i in itertools.dropwhile(lambda x: x < 5, data):
    print(i)

print(
    "\nfilterfalse(): Makes an iterator that filters elements from iterable returning only those for which the predicate is False."
)
for i in itertools.filterfalse(lambda x: x < 5, data):
    print(i)

print("\ngroupby(): Simply put, this function groups things together.")
for key, group in itertools.groupby(robots, key=lambda x: x["faction"]):
    print(key)
    print(list(group))

print(
    "\nislice(): This function is very much like slices. This allows you to cut out a piece of an iterable."
)
for e in itertools.islice(colors, 3):
    print(e)

print("\npermutations()")
for i in itertools.permutations(shapes):
    print(i)

print(
    "\nproduct(): Creates the cartesian products from a series of iterables.")
for i in itertools.product(shapes, colors):
    print(i)

print(
    "\nrepeat(): This function will repeat an object over and over again. Unless, there is a times argument."
)
for i in itertools.repeat("Hi ", 3):
    print(i)

print(
    "\nstarmap(): Makes an iterator that computes the function using arguments obtained from the iterable."
)
for i in itertools.starmap(operator.mul, data2):
    print(i)

print(
    "\ntakewhile(): The opposite of dropwhile(). Makes an iterator and returns elements from the iterable as long as the predicate is true."
)
for i in itertools.takewhile(lambda x: x < 5, data):
    print(i)

print("\ntee(): Return n independent iterators from a single iterable.")
a, b = itertools.tee(colors, 2)
print(a)
for i in a:
    print(i)

print(
    "\nzip_longest(): Makes an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted."
)
for e in itertools.zip_longest(colors, data, fillvalue=None):
    print(e)
