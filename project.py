#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:01:38 2021

@author: samraltahirli
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:57:19 2021

@author: samraltahirli
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pulp

# lp contains the problem data, problem defined as min
lp= pulp.LpProblem("Number_of_students_problem",pulp.LpMaximize)


#variables 
x1=pulp.LpVariable(name="10-345678",   lowBound=1)
x2=pulp.LpVariable(name="102-456",     lowBound=1)
x3=pulp.LpVariable(name="114-45678",   lowBound=1)
x4=pulp.LpVariable(name="116-45678",   lowBound=1)
x5=pulp.LpVariable(name="13-345678",   lowBound=1)
x6=pulp.LpVariable(name="135-45678",   lowBound=1)
x7=pulp.LpVariable(name="138-345678",  lowBound=1)
x8=pulp.LpVariable(name="139-456789",  lowBound=1)
x9=pulp.LpVariable(name="14-45678",    lowBound=1)
x10=pulp.LpVariable(name="144-45678",  lowBound=1)
x11=pulp.LpVariable(name="145-45678",  lowBound=1)
x12=pulp.LpVariable(name="146-345678", lowBound=1)
x13=pulp.LpVariable(name="153-45678",  lowBound=1)
x14=pulp.LpVariable(name="158-678",    lowBound=1)
x15=pulp.LpVariable(name="159-45678",  lowBound=1)
x16=pulp.LpVariable(name="160-456789", lowBound=1)
x17=pulp.LpVariable(name="162-45678",  lowBound=1)
x18=pulp.LpVariable(name="164-5678",   lowBound=1)
x19=pulp.LpVariable(name="251-2345678",lowBound=1)
x20=pulp.LpVariable(name="233-245678", lowBound=1)



# The objective function is min, profits are negative
lp += 330*x1 +164*x2+113*x3+128*x4+160*x5+151*x6+356*x7+326*x8+274*x9+138*x10+280*x11+153*x12+238*x13+191*x14+147*x15+443*x16+274*x17+232*x18+350*x19+361*x20, "Number of students"
# Availability constraints
lp += 0*x1  + 0*x2  + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 0*x7  + 0*x8  + 0*x9  + 0*x10  + 0*x11  + 0*x12  + 0*x13  + 0*x14  + 0*x15  + 0*x16  + 0*x17  + 0*x18  + 20*x19 + 29*x20<= 170, "Availability of workbooks for 2 RUS детей"
lp += 28*x1 + 0*x2  + 0*x3  + 0*x4  + 25*x5 + 0*x6  + 26*x7 + 0*x8  + 0*x9  + 0*x10  + 0*x11  + 27*x12 + 0*x13  + 0*x14  + 0*x15  + 0*x16  + 0*x17  + 0*x18  + 35*x19 + 30*x20<= 180, "Availability of workbooks for 3 AZ детей"
lp += 25*x1 + 0*x2  + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 36*x7 + 0*x8  + 0*x9  + 0*x10  + 0*x11  + 0*x12  + 0*x13  + 0*x14  + 0*x15  + 0*x16  + 0*x17  + 0*x18  + 40*x19 + 30*x20<= 362, "Availability of workbooks for 3 RUS детей"
lp += 29*x1 + 24*x2 + 22*x3 + 25*x4 + 26*x5 + 32*x6 + 23*x7 + 32*x8 + 26*x9 + 31*x10 + 20*x11 + 27*x12 + 19*x13 + 0*x14  + 27*x15 + 43*x16 + 31*x17 + 0*x18  + 27*x19 + 26*x20<= 520, "Availability of workbooks for 4 AZ детей"
lp += 26*x1 + 35*x2 + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 38*x7 + 33*x8 + 35*x9 + 0*x10  + 29*x11 + 0*x12  + 25*x13 + 0*x14  + 0*x15  + 44*x16 + 18*x17 + 0*x18  + 28*x19 + 29*x20<= 454, "Availability of workbooks for 4 RUS детей"
lp += 26*x1 + 24*x2 + 22*x3 + 25*x4 + 25*x5 + 34*x6 + 31*x7 + 31*x8 + 24*x9 + 32*x10 + 29*x11 + 27*x12 + 23*x13 + 0*x14  + 26*x15 + 44*x16 + 31*x17 + 32*x18 + 28*x19 + 27*x20<= 543, "Availability of workbooks for 5 AZ детей"
lp += 37*x1 + 34*x2 + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 40*x7 + 32*x8 + 33*x9 + 0*x10  + 34*x11 + 0*x12  + 23*x13 + 0*x14  + 0*x15  + 41*x16 + 35*x17 + 30*x18 + 21*x19 + 28*x20<= 421, "Availability of workbooks for 5 RUS детей"
lp += 20*x1 + 22*x2 + 21*x3 + 26*x4 + 31*x5 + 27*x6 + 21*x7 + 30*x8 + 25*x9 + 26*x10 + 33*x11 + 25*x12 + 25*x13 + 30*x14 + 33*x15 + 40*x16 + 26*x17 + 28*x18 + 26*x19 + 29*x20<= 630, "Availability of workbooks for 6 AZ детей"
lp += 21*x1 + 25*x2 + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 25*x7 + 31*x8 + 32*x9 + 0*x10  + 29*x11 + 0*x12  + 29*x13 + 33*x14 + 0*x15  + 37*x16 + 39*x17 + 29*x18 + 30*x19 + 26*x20<= 449, "Availability of workbooks for 6 RUS детей"
lp += 25*x1 + 0*x2  + 24*x3 + 27*x4 + 26*x5 + 31*x6 + 31*x7 + 28*x8 + 25*x9 + 23*x10 + 26*x11 + 24*x12 + 20*x13 + 32*x14 + 31*x15 + 45*x16 + 22*x17 + 27*x18 + 27*x19 + 28*x20<= 522, "Availability of workbooks for 7 AZ детей"
lp += 30*x1 + 0*x2  + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 34*x7 + 27*x8 + 24*x9 + 0*x10  + 26*x11 + 0*x12  + 28*x13 + 29*x14 + 0*x15  + 38*x16 + 31*x17 + 33*x18 + 16*x19 + 24*x20<= 475, "Availability of workbooks for 7 RUS детей"
lp += 25*x1 + 0*x2  + 24*x3 + 25*x4 + 27*x5 + 27*x6 + 27*x7 + 29*x8 + 27*x9 + 26*x10 + 26*x11 + 23*x12 + 23*x13 + 29*x14 + 30*x15 + 39*x16 + 22*x17 + 22*x18 + 27*x19 + 29*x20<= 510, "Availability of workbooks for 8 AZ детей"
lp += 38*x1 + 0*x2  + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 24*x7 + 29*x8 + 23*x9 + 0*x10  + 28*x11 + 0*x12  + 23*x13 + 38*x14 + 0*x15  + 38*x16 + 19*x17 + 31*x18 + 25*x19 + 26*x20<= 420, "Availability of workbooks for 8 RUS детей"
lp += 0*x1  + 0*x2  + 0*x3  + 0*x4  + 0*x5  + 0*x6  + 0*x7  + 24*x8 + 0*x9  + 0*x10  + 0*x11  + 0*x12  + 0*x13  + 0*x14  + 0*x15  + 34*x16 + 0*x17  + 0*x18  + 0*x19  + 0*x20<= 110, "Availability of workbooks for 9 RUS детей"


#prob.solve(CPLEX())
lp.solve(pulp.PULP_CBC_CMD(fracGap = 0.00001, maxSeconds = 500, threads = None))
# The status of the solution
print("Status:", pulp.LpStatus[lp.status])
# The optimal objective function value

print("Maximum number of students= ", 1*pulp.value(lp.objective))
# Primal and dual variables optimal value
for var in lp.variables():
    print(var.name, "=", var.value())
for name, c in list(lp.constraints.items()):
    print(name, ":", c, "\t dual", c.pi, "\tslack", c.slack)