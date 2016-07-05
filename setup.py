import os
import sys
import qeinput
import qesetup
import numpy
import math


if __name__ == '__main__':
    prefix = 'graphene'
    pwbindir = '/home/rehnd/qe-tddft/bin'
    tdbindir = '/home/rehnd/qe-tddft/multi-k-tddft/bin'
    pseudodir = '/home/rehnd/qe-tddft/pseudo'
    nat = [4]
    nks = [1]
    #dts = [2.**-10, 2.**-9, 2.**-8, 2.**-7, 2.**-6, 2.**-5, 2.**-4, 2.**-3, 0.25, 0.5, 1.0, 2.0, 4.0]
    dts = [2.**-5, 2.**-4, 2.**-3, 0.25, 0.5, 1.0, 2.0, 4.0]
    methods = ['rk4', 'rk54', 'rk53']
    runtime = 500

    if len(sys.argv) > 1:
        if sys.argv[1] == 'default':
            qesetup.setupall(prefix, pwbindir, tdbindir, pseudodir, nat, nks, dts, methods, runtime)
        elif sys.argv[1] == 'serial':
            qesetup.runserial(nat, nks, dts, methods)
        elif sys.argv[1] == 'parallel':
            qesetup.runparallel(nat, nks, dts, methods)
    else:
        print("Usage:\n\tpython setup.py <option> <number>")
        print("\t\t<option> = default, remove, newdir, serial, or parallel")
        print("\t\t<number> = atom # directories to remove or newdir (ONLY valid for remove, newdir)")
        print("\t\t           use 'all' to delete all atom folders")
