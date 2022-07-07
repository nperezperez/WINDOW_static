'''
This script is used to create the batch of simulations to be run using WINDOW for different values of
rated power and rotor radius. For each combination,
'''
import os
import numpy as np
from IEA_borssele_irregular_new_UC import run_main_script

def batch():
    ###### Run a batch ######
    val_power = 20
    #vals_rad = [110, 115, 120, 125, 130, 135, 140] #rotor radius values
    vals_rad = np.linspace(90,150,13)



    for val in vals_rad:
            value_rad = val
            value_power = val_power
            run_main_script(value_rad, value_power)
            old_filename = 'parameters.csv'
            new_filename = 'parameters_' + str(value_power) + '_' + str(value_rad) + '.csv'
            os.rename(old_filename, new_filename)


def singlecase():
    ##### Run a single case #####
    value_power = 15
    value_rad = 240/2 #reference rotor radius

    # dict = {'target_IRR':target_IRR}
    # f = open('Input/finance.txt', 'w')
    # f.write(repr(dict) + '\n')
    # f.close()

    run_main_script(value_rad, value_power)
    old_filename = 'parameters.csv'
    new_filename = 'parameters_' + str(value_power) + '_' + str(value_rad*2) + '.csv'
    os.rename(old_filename, new_filename)

## RUN ##

#batch()
singlecase()
