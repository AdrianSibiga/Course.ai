# Important Parameters: 
# Days of the week, [0,1,0,1,0]
# Start time, [8, 35]
# End time, [14, 25]
# Days go from 8h to 21h, 05m to 55m

# Say we have 2 classes, 2 lecture sections, 2 lab sections, total of (2*2)^2 = 16 different combinations
# SYSC 2004 and ELEC 2602

# SYSC 2004 A is held from [8, 35] to [9, 55] on Mondays and Wednesdays [1,0,1,0,0]
# SYSC 2004 B is held from [10, 05] to [11, 25] on Mondays and Wednesdays [1,0,1,0,0]
# SYSC 2004 L1 is held from [11, 35] to [14, 25] on Mondays [1,0,0,0,0]
# SYSC 2004 L2 is held from [8, 35] to [11, 25] on Tuesdays [0,1,0,0,0]

# ELEC 2602 A is held from [10, 05] to [11, 25] on Mondays and Wednesdays [1,0,1,0,0], time conflict
# ELEC 2602 B is held from [10, 05] to [11, 25] on Tuesdays and Thursdays [0,1,0,1,0], time conflict
# ELEC 2602 L1 is held from [8, 35] to [11, 25] on Fridays
# ELEC 2602 L2 is held from [11, 35] to [14, 25] on Thursdays

# A L1, A L1    Conflict between SL1 and EA
# A L1, A L2    Conflict between SL1 and EA
# A L1, B L1
# A L1, B L2
# A L2, A L1
# A L2, A L2
# A L2, B L1    Conflict between SL2 and EB
# A L2, B L2    Conflict between SL2 and EB
# B L1, A L1
# B L1, A L2
# B L1, B L1
# B L1, B L2
# B L2, A L1
# B L2, A L2
# B L2, B L1
# B L2, B L2

# This leaves 12 non-conflict cases

