x = 1



def local_scope(a):
    if a == 1:
        print("YES")
        return 2
    else:
        return a


x = local_scope(x)

