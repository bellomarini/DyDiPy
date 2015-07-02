from pyDatalogExt import pyDatalog
def test():

    #@pyDatalog.program()
    #def basic_test():
    #	+a(1,2)
    #	assert ask(a(X, Y)) == set([(1,2)])

    pyDatalog.clear()    
    @pyDatalog.program()
    def tgd_1():
    	+a(1,2)
    	b(X,Y)&c(X,Y)<=a(X,Y)
    	ask(b(X,Y))
    	#ask(b(X,Y))
    	#ask(c(X,Y))
    	    		
if __name__ == "__main__":
    test()