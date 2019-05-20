#these functions print all the subsets that can be from the list items
def subSets(items):
    blocks = [items]
    stack = []
    while len(blocks) > 0:
        block = blocks[0]
        del blocks[0]
        if len(block) == 0:
            break
        stack.append(block)
        for i in range(len(block)):
            new_block = []
            for j in range(len(block)):
                if i != j:
                    new_block.append(block[j])
            if new_block not in blocks:
                blocks.append(new_block)
    while len(stack) > 0:
        print(stack.pop())

#subSets([1,2,3,4,5,6,7,8,9,10])


def subSetsR(items):
    if len(items) == 1:
        return [items]
    
    set_1 = subSetsR(items[0:len(items)//2])
    set_2 = subSetsR(items[len(items)//2:])
    
    new_sets = []
    for s1 in set_1:
        for s2 in set_2:
            new_sets.append(s1+s2)    
    return set_1 + set_2 + new_sets

def getKey1(item):
    return len(item)

def getKey2(item):
    return item[0]

#sol = sorted(sorted(subSetsR([1,2,3,4,5,6]),key = getKey2),key = getKey1)
