from component import *

if __name__ == '__main__':
	
	vcc = Component(0, 'source', True)
	r1 = Component(1, 'r1')
	r2 = Component(2, 'r2')

	vcc.connect(r1)
	vcc.connect(r2)
	r1.connect(vcc)
	r2.connect(vcc)

	c1 = Circuit(5)
	c1.set_source(vcc)

	c1.print()

