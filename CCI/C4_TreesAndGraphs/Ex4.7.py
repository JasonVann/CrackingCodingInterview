from tree import Tree_Node


def build_order(projects, dependencies):
    order = []
    table_xy = {}
    table_yx = {}
    for x, y in dependencies:
        # y dependent on x
        if y in table_yx:
            table_yx[y] += [x]
        else:
            table_yx[y] = [x]
        if x in table_xy:

            table_xy[x] += [y]
        else:
            table_xy[x] = [y]
        # Check for cyclic dependency
        if y in table_xy and x in table_xy[y]:
            return None

    for p in projects:
        if p not in table_xy and p not in table_yx:
            order.append(p)

    l = len(dependencies)
    stack = []
    while True:
        if stack == []:
            keys = list(table_xy.keys())
            if len(keys) == 0:
                break
            x = keys[0]
        else:
            x = stack.pop(0)
        while x in table_yx:
            if len(table_yx[x]) == 0:
                table_yx.pop(x)
            else:
                x = table_yx[x][0]
        if x not in table_yx:
            #if x not in order:
            order.append(x)
            if x in table_xy:
                for y in table_xy[x]:
                    table_yx[y].remove(x)
                    if len(table_yx[y]) == 0:
                        stack.append(y)

                table_xy.pop(x)

    return order

def test():
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    #dependencies = [('d', 'a'),('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    order = build_order(projects, dependencies)
    print(order)

test()
