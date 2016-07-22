def getsbatch(np, pw_path, tddft_path):
    string = """#!/bin/bash

#SBATCH --job-name=scaling-np"""
    string+= str(np)
    string+="""
#SBATCH --output=tddft.out
#SBATCH --error=tddft.err
#SBATCH --time=00:10:00
#SBATCH --qos=normal
#SBATCH --nodes="""
    string+=str(np)
    string+="""
#SBATCH --mem=4000
#SBATCH --ntasks-per-node=16
"""

    string+="""
rm -rf *out
mpirun -np """
    string+=str(np)
    string+=""" """
    string+=pw_path + '/pw.x'
    string+=""" < graphene.pw-in > graphene.pw-out
mpirun -np """
    string+=str(np)
    string+=""" """
    string+=tddft_path + '/tddft.x'
    string+=""" < graphene.tddft-in > graphene.tddft-out
"""
    return string


def gettdfile(prefix, dt, nstep, conv_threshold):
    string = """&inputtddft
    job = 'optical'
    prefix = '"""
    string += prefix + "'"
    string += """
    tmp_dir = './out/'
    dt = """
    string += str(dt) 
    string += """
    nstep = """
    string += str(nstep) 
    string +="""
    e_direction = 3
    e_strength = 0.01          
    conv_threshold = """
    string += str(conv_threshold)
    string += "\n/\n"

    return string


def getpw16at(pseudodir):
    string = """&control
    calculation = 'scf'
    restart_mode='from_scratch'
    prefix='graphene'
    pseudo_dir = '""" + pseudodir
    string +="""',
    outdir = './out'

/
&system
    ibrav=8
    celldm(1)=9.297452
    celldm(2)=1.7317073170
    celldm(3)=1.96
    nat=16
    ntyp=1
    ecutwfc=25.0
    occupations='smearing'
    smearing='gaussian'
    degauss=0.01

/
&electrons
    diagonalization='david'
    electron_maxstep = 100
    mixing_mode='plain'
    mixing_beta=0.1
    conv_thr = 1.0e-27

/
ATOMIC_SPECIES
C 12.011 C.pbe-hgh.UPF

ATOMIC_POSITIONS (angstrom)
C 0.000000000 0.000000000 0.000000000
C 1.230000000 0.710000000 0.000000000
C 1.230000000 2.130000000 0.000000000
C 0.000000000 2.840000000 0.000000000
C 0.000000000 4.260000000 0.000000000
C 1.230000000 4.970000000 0.000000000
C 1.230000000 6.390000000 0.000000000
C 0.000000000 7.100000000 0.000000000
C 2.460000000 0.000000000 0.000000000
C 3.690000000 0.710000000 0.000000000
C 3.690000000 2.130000000 0.000000000
C 2.460000000 2.840000000 0.000000000
C 2.460000000 4.260000000 0.000000000
C 3.690000000 4.970000000 0.000000000
C 3.690000000 6.390000000 0.000000000
C 2.460000000 7.100000000 0.000000000

K_POINTS {tpiba}
4
0.0 0.0000000000000000 0.0 1.0
1.0 0.0000000000000000 0.0 1.0
0.0 0.5774647887323944 0.0 1.0
1.0 0.5774647887323944 0.0 1.0
"""
    
    return string
