from collections import Counter
from random import randrange

# coding conventions (from https://google-styleguide.googlecode.com/svn/trunk/pyguide.html):
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
def main():
    enumerate_example()
    counter_example()
    dict_function_example()

def enumerate_example():
    l = ["this", "is", "a", "list"]
    for index, value in enumerate(l):
        print(index, value)

def counter_example():
    #hahia. no really, an example of a counter.
    my_counter = Counter()
    for i in xrange(100):
        random_number = randrange(10)
        my_counter[random_number] += 1
    for i in xrange(10):
        print(i, my_counter[i])

def dict_function_example():
    my_favorites = {"number" : 42, "colour" : "green", "sport": "rock climbing!"}
    for key, value in my_favorites.iteritems():
        print(key, value)
    # default values:
    print(my_favorites.get("animal", "turtle"))

if __name__ == "__main__":
    main()
