from itertools import product

def combine_lists(list1, list2):
    return list(product(list1, list2))

# Example usage
if __name__ == "__main__":
    list1 = ["hola", "caracola"]
    list2 = ["adios", "caracol"]
    result = combine_lists(list1, list2)
    print("Combined pairs:", result)
