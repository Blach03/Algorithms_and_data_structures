from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None


def sol(root, T):
    print(root.key)
    minn=root.left
    while minn.right!=None:
      minn=minn.right
    print(minn.key)
    return 0
    
runtests(sol, all_tests = False)