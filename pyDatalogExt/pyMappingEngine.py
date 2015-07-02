"""
This file is part of pyDatalog, a datalog engine for python.

Copyright (C) 2015 Luigi Bellomarini

This library is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc.  51 Franklin St, Fifth Floor, Boston, MA 02110-1301
USA
"""

"""
This file contains the port of the datalog engine of J. D. Ramsdell, 
from lua to python, with many enhancements.
"""

from . import pyEngine
from collections import OrderedDict

Slow_motion = True # True => detail print of the stack of tasks at each step

def chase():
    # for all the clauses
    # unify the body with its atoms
    # calculate the atoms of the generated head
    # unify the head with its atoms
    # if does unify, discard
    # else
    # insert the atoms of the generated head
    
    Slow_motion = True
    
    # for all the clauses
    for cla in pyEngine.Logic.tl.logic.Clauses.values():
        # do not chase queries
        if str(cla).startswith("_pyD_"):
            continue
            
        if Slow_motion:
            print("Chasing " + str(cla))
        # if it has a body (is not a fact)
        if cla.parsed_body:
            # unify the body with its atoms
            # variables : {[('X', [1,2,3]),('Y',[2,3,4])]}
            variables = cla.parsed_body._variables()
            
            # number of possible homomorphism for the body
            homo_num = len(variables.values()[0]) if len(variables.values())>0 else 0
            if Slow_motion:
                print("Variables: " + str(variables))
                print("Found " + str(homo_num) + " homomorphism to facts")
            
            # calculates all the homomorphism from the body to the facts
            homos = []
            homo = OrderedDict()
            for i in range(homo_num):
                for var, val_list in variables.items():
                    print(str(val_list[i]))
                    homo[var]=val_list[i]
                homos.append(homo)
                    
            if Slow_motion:
                print(homos)
            
                    
            
            
            head = cla.head
            head2 = head.subst(variables)
            
            print(head2)
            
            
            