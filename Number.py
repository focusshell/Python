class A:
    pass

class B(A):
    pass

isinstance(A( ), A)    # returns True
type(A( )) == A        # returns True
isinstance(B( ), A)    # returns True
type(B( )) == A        # returns False