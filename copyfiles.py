import os
import qecopy

if __name__ == '__main__':
    cpfrom = '/home/rehnd/tddft-data/2016-05-33'
    cpto   = '/home/rehnd/tddft-data/2016-05-31'
    
    nat = [4]
    nks = [1]

    dts = [2.**-4, 2.**-3, 2.**-2, 2.**-1, 2.**0, 2.**1, 2.**2]

    methods = ['am2', 'am3', 'am4']

    qecopy.copy(cpfrom, cpto, nat, nks, dts, methods)
