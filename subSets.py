#this function prints all the subsets that can be from the list items
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
