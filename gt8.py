# ======= Import =======
from __future__ import print_function
print("***Importing***")

try:
    print("")
    print("Importing argv :: ", end="")
    from sys import argv
    print("\033[32mDone\033[0m")
    print("Importing Sys :: ", end="")
    import sys 
    print("\033[32mDone\033[0m")
    print("Importing glob :: ", end="")
    import glob
    print("\033[32mDone\033[0m")
    print("Importing os :: ", end="")
    import os
    print("\033[32mDone\033[0m")
    print("Importing os.path :: ", end="")
    import os.path
    print("\033[32mDone\033[0m")
    print("Importing numpy :: ", end="")
    import numpy as np
    print("\033[32mDone\033[0m")
    print("Importing fnmatch :: ", end="")
    from fnmatch import fnmatch
    print("\033[32mDone\033[0m")
    print("Importing math :: ", end="")
    from math import log10
    import math
    print("\033[32mDone\033[0m")
    print("Importing time :: ", end="")
    import time
    print("\033[32mDone\033[0m")
    print("Importing scipy.stats:: ", end="")
    from scipy import stats
    print("\033[32mDone\033[0m")
    print("Importing pynbody :: ", end="")
    import pynbody as pnb
    print("\033[32mDone\033[0m")
    #print("Importing multiprocessing :: ", end="")
    # multiprocessing import Pool, Process, Value, Array
    #print("Done")
    print("")
    
except:
    print("You do not have all the necessary modules ")
    print("Please make sure you have the all of the modules in the ***import*** section are installed and active.")
    exit(0)
print("***Success***")
print("")

# =============== Py Info ===============
__author__ = "Robel Geda"
__credits__ = ["Robel Geda", "Yotam Cohen", "Jay Takle", "Alyson Brooks"]
__version__ = "6.1.0"

# =============== Tools for filebase ===============
# *** Edit filebase ***
def find_filebase():
    global filebase
    
    for file1 in glob.glob("*.grp"):
        file1 = file1.replace(".grp","")
        filebase.append(file1)
        
    filebase = reverse_list(sorted(filebase))
    #print_filebase()
    temp_opt = ""
    if len(filebase) < 5:
        if len(filebase) > 2:
            print("Found less than 5 files")
            print_filebase()
            temp_opt = raw_input("Look of more in sub-dirs? (y/n): ")
            if temp_opt != "n" and temp_opt != "N":
                deep_search()
        else:
            temp_opt = "y"
            deep_search()
        if len(filebase) == 0:
            #print("Error: No {.grp} files found. Exiting...")
            options2()
            exit(0)
                
    try:
        temp_arr = []
        with open("gt8_filebase.txt", "r") as f:
            for line in f:
                if '\n' in line:
                    temp_arr.append(line.replace("\n",""))
                else:
                    temp_arr.append(line)
        for item in temp_arr:
            print("\033[47m\033[30m"+item+"\033[0m : ", end = "")
            if item not in filebase:
                error("file in filebase missing in dir...")
                print("file: "+item)
                print("Please restart gentrack6 (gt8)")
                os.system("rm gt8_filebase.txt")
                exit(0)
            print("\033[32mOk\033[0m")
        filebase = temp_arr
    except:
        print("")
        option = ""
        while option != "c":
            print_filebase()
            print(" ")
            if temp_opt == "y" and temp_opt == "Y":
                print("Gentrack has found folders with stat and grp files, check if steps are correct.")
            else:
                print("Gentrack has found stat and grp files, check if steps are correct.")
            print("enter:(c)continue | (i) remove item | (l) remove list of items ")
            print("      (k) multi-remove using key_word | (r) reverse order")
            print("      (d) remove a range of indices ")
            option = ""
            while(option not in ['c', 'i', 'l', 'k', 'r', 'd']):
                  option = raw_input("Option {c, i, l, k, r, d} => ")
                  
            if (option != 'c'):
                  edit_filebase(option)
                  
        with open("gt8_filebase.txt", "w") as f:
            counter = 0 
            for line in filebase:
                if counter != len(filebase)-1:
                    f.write(line + "\n")
                else:
                     f.write(line)
                    
                    
        print("\n\n\n\n")
        print("Filebase saved @ \033[36mgt8_filebase.txt\033[0m")
        print("Delete that file if you want to re-config filebase.")
        raw_input("*Press enter to continue*")
        
                    
def deep_search():               
    global filebase
    
    filebase = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".grp")]:
            file1 = os.path.join(dirpath, filename)
            file1 = file1.replace(".grp","")
            filebase.append(file1)
    filebase = reverse_list(sorted(filebase))
    
                
def print_filebase():
    global filebase
    counter = 0
    while counter < len(filebase):
        print(counter, filebase[counter])
        counter+=1
        
def edit_filebase(option):
    global filebase, crap_files
    #{c, i, l, k, r, d}
    print_filebase
    if option == 'r':
        print("LOWEST redshift should come first")
        print("(HIGHEST scale should come first)")
        opt_t = raw_input("Reverse? (y/n): ")
        if opt_t == 'y':
            filebase = reverse_list(filebase)
    if option == 'i':
        try:
            target = eval(raw_input("Index of item to remove: "))
        except:
            error("input error.")
            return
        if(target < len(filebase) and target >= 0):
            print("Removing \033[1m\033[35m%s\033[0m from list... " %filebase[target])
            crap = filebase.pop(target)
            crap_files.append(crap)
            print(crap)
            
    if option == 'l':
        try:
            print("Index of items to remove separated by a ';': ")
            target = raw_input("Indices => ")
            targets = target.split(";")
            trash = []
        
            for target in targets:
                target = eval(target)
                if(target < len(filebase) and target >= 0):
                    trash.append(filebase[target])
            print("Removing from list... ")
            for i in trash:
                print("\033[1m\033[35m %s \033[0m" %i)
                crap = filebase.pop(filebase.index(i))
                crap_files.append(crap)
        
        except:
            error("Error.")
            return
        
        
    if option == 'k':
        try:
        
            #print("Key word: ")
            target = raw_input("Key word: ")
            trash = []
        
            for i in filebase:
                if(target in i):
                    trash.append(i)
            print("Removing from list... ")
            for i in trash:
                print("\033[1m\033[31m %s \033[0m" %i)
                crap = filebase.pop(filebase.index(i))
                crap_files.append(crap)
        
        except:
            error("Error.")
            return

    if option == 'd':
        try:
            print("range to include{mini, maxi}")
            mini = eval(raw_input("First index: "))
            maxi = eval(raw_input("Last index: "))
             
            trash = []
            for target in range(mini, maxi+1):
                if(target < len(filebase) and target >= 0):
                        trash.append(filebase[target])
    
            print("Removing from list... ")
            for i in trash:
                print("\033[1m\033[31m %s \033[0m" %i)
                crap = filebase.pop(filebase.index(i))
                crap_files.append(crap)
        
        except:
            error("Error.")
            return
        
    if len(filebase) == 0:
        error("Removed all items!")
        exit(0)
        
    print("\n\n")

# =============== Tool bag ===============
# *** Error ***
def error (message):
    print("\033[31mERROR\033[0m : %s" % message)
# *** Binary Search ***
def  binary_search(array, item, supert = False):
    global filebase
    # Binary search
    item = int(item)
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = int((lo + hi)//2)
        midval = int(arr[mid][0])
        if midval < int(item):
            lo = mid + 1
        elif midval > int(item):
            hi = mid
        else:
            if supert == True:
                return False
            return mid
    if supert == True:
        return True

    print("Error, Stat could not be found for this halo: %s" %item)
    print("Step: %s"  %filebase[count])
    print("")
    exit(0)

# *** Regular Search for stat ***   
def reg_search(array, item, supert = False):
    global filebase
    c = 0
    for i in array:
        if int(i[0]) == int(item):
            return c
        c = c + 1
    if supert == True:
        return True

    error("Stat could not be found for this halo: %s" %item)
    print("Step: %s"  %filebase[count])
    print("")
    exit(0)

# *** Load .stat file***        
def read_stat(filename):
    #filename = filename + ".stat"
    stat = []
    with open(filename) as f:
        f.readline()
        for line in f:
            stat.append(line.split())    
    return stat

def read_stat_header(filename):
    #filename = filename + ".stat"
    global stat_header
    stat_header = []
    with open(filename) as f:
        line = f.readline()
        stat_header = line.split()
    """
    if len(stat_header) != len(temp):
        error("Length of stat file header does not match number of stat items...")
        print("Killing program")
        print(len(stat_header), len(temp))
        print("")
        exit(0)
    """
    return stat_header

# *** Load grp file*** 
def np_read_grp(filename):
    #filename = filename + ".grp"
    file = open(filename)
    data = file.read()
    #grp_array = np.asarray(data.split(), dtype = int)
    grp_array = np.fromstring(data, dtype=int, sep='\n')[1:]
    file.close()
    print(grp_array.size)
    return grp_array
def read_grp (filename):
    #filename = filename + ".grp"
    file = open(filename)
    data = file.read().split()
    file.close()
    return data

# *** Find all indices of np.array(data) items that == value(v)***            
def find_grp(data, v):
    return np.where( data == v )[0]

# *** Find all indices of list(list_in) items that == value(v)***  
def find_in_list(list_in, v):
    list_out = [] 
    index = 0 
    for item in list_in:
        if int(item) == int(v):
            list_out.append(int(index))
        index = index +1
    return list_out

# *** Index multiple values of list, indexL is a list of indices*** 
def values_at(list_in , indexL, string = False):
    list_out = []
    for ind in indexL:
        if string == False:
            list_out.append(int(list_in[ind]))
        else:
            list_out.append(list_in[ind])
    return list_out

# *** Finds unique values of list ***
def squash (arr):
    temp = np.array(arr)
    temp = temp.flatten()
    temp = np.unique(temp)
    return temp

# *** Finds unique values of np.array ***
def unique(temp):
    temp = temp.flatten()
    temp = np.unique(temp)
    return temp
# *** Numpy where ***
def where(arr, value):
    temp = np.where(arr == value)[0]
    return temp
def whereRemove(arr, value):
    temp = np.where(arr < value)[0]
    return temp

# *** Finds mode of list ***
def list_mode (arr):
    arr = sorted(arr)
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        arr = arr[0]
    count = 0
    max1 = 0
    maxcount = 0
    now = arr[0]
    for i in arr:
        if i == now:
            count = count + 1
            if maxcount < count and i != 0:
                if max1 != i:
                    max1 = i
                maxcount = count
        else:
            count = 1
            now = i
    return max1

# *** find mode of numpy ***
"""
def mode (arr):
    global null
    arr.sort()
    if arr.size == 0:
        return null
    if arr.size == 1 and type(arr) == int:
        return arr

    count = 0
    max1  = 0
    maxcount = 0
    now = arr[0]
    
    for i in arr:
        if i == now:
            count = count + 1
            if maxcount < count and i != null:
                if max1 != i:
                    max1 = i
                maxcount = count
        else:
            count = 1
            now = i
    return max1
"""
# Found mode(x) at http://stackoverflow.com/
# I did not come up with the bottom part
def mode(x):
    global null
    x = x[np.where(x!=null)[0]]
    
    if x.size == 0:
        return null
    counts = np.bincount(x)
    return int(np.argmax(counts))

def mode2(x):
    global null, big_halo
    x = x[np.where(x!=null)[0]]
    x = x[np.where(x!=big_halo)[0]]
    
    if x.size == 0:
        return null
    counts = np.bincount(x)
    return int(np.argmax(counts)) 
    
# *** Reverse list ***
def reverse_list(arr):
    array = []
    for i in reversed(arr):
        array.append(i)
    return array    

# *** Arr to str ***
def atos (arr, space):
    temp = []
    for i in arr:
        temp.append(str(i))
    return space.join(temp)

def stoa (arr, space):
    temp = []
    arr = arr.split(space)
    for i in arr:
        try:
            temp.append(eval(i))
        except:
            temp.append(i)
    return temp

# Sign
def sign (num):
    if num < 0:
        return -1
    return 1
# =============== .vtk ===============
# Cedit: Yotam Cohen & Col.
def vtk (filename):
    print("generating .vtk")
    data = []
    with open(filename) as f:
        f.readline()
        for line in f:
            line = line.split("\t")
            data.append(line)
            
    filename = filename.replace(".dat","")
    npoints = len(data)
    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([l[15], l[16], l[17]])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        u = 0
        for l in data: 
            f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('1'+ "\n")
        
        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %3+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            if eval(l[7]) > 0:
                f.write(str(log10(float(l[7])))+ "\n")
            else:
                f.write("0.0")

        f.write('Rvir 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(l[8]+ "\n")
        f.write('Velocities 3 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([l[18], l[19], l[20]])+ "\n")

    """     #*** \/ ***
    with open(filename+".MC.vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([l[15], l[16], l[0].replace("*","")])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        u = 0
        for l in data: 
            f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('1'+ "\n")
        
        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %1+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(log10(float(l[7])))+ "\n")
    """

def grouper(data, x):
    global boss
    temp = [] 
    for l in data:
        if eval(l[0].replace("*","")) == x:
            temp.append([eval(l[15]), eval(l[16]), eval(l[17])])
            if('*' in l[0]):
                boss = [eval(l[15]), eval(l[16]), eval(l[17])]
                
    for i, l in enumerate(temp):
        temp[i][0] = str(l[0] - boss[0])
        temp[i][1] = str(l[1] - boss[1])
        temp[i][2] = str(l[2] - boss[2])
    return temp
                
def tree_vtk(filename):
    global boss
    print("generating .vtk")
    data = []
    with open(filename) as f:
        f.readline()
        for line in f:
            line = line.split("\t")
            data.append(line)

    filename = filename.replace(".dat","")
    npoints = len(data)
    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        maxi = eval(data[-1][0].replace("*",""))
        for x in range(0,maxi):
            x_list = grouper(data, x)
            for l in x_list:
                f.write(" ".join([l[0], l[1], "0"])+ "\n")
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        u = 0
        for l in data:
            f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)                                                                    
            f.write('1'+ "\n")

        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %3+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(log10(float(l[7])))+ "\n")
        f.write('Rvir 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(l[8]+ "\n")
        f.write('Velocities 3 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([l[18], l[19], l[20]])+ "\n")

def Pvtk(data, fn):
    filename = "./gt8_output/Pmovie/PM"+fn
    npoints = len(data)

    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([str(l[0]), str(l[1]), str(l[2])])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        u = 0
        for l in data: 
            f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('1'+ "\n")

            
# =============== Tracking =========================================================================================================================

# *** simple/quick tracking ***
def track(particles = []):
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut
    global maingrp, start_step, end_step
    global length, maincondition, big_halo, big
    
    final = []
    maincondition = True

    # Load base_grp array
    if task == 0 or task == 1 or task == 5:
        print("Setting up initial conditions...")
        grp_arr = np_read_grp(filebase[0]+".grp")
        core_index = where(grp_arr, maingrp)
        base_index = core_index
        main = maingrp
        main_hist.append(main)
    elif task == 2:
        base_index = supertrack()
        grp_arr = np_read_grp(filebase[0]+".grp")
        core_index = where(grp_arr, maingrp)
        base_index = core_index
        main = maingrp
    elif task == 3:
        base_index = mergers()
        grp_arr = np_read_grp(filebase[0]+".grp")
        core_index = where(grp_arr, maingrp)
        base_index = core_index
        main = maingrp
    elif task == 7:
        grp_arr = np_read_grp(filebase[0]+".grp")
        base_index = particles
        core_index = base_index

    # Check if grp has stat 
    try:
        stat_file = filebase[0]+'.stat'
        stat = read_stat(stat_file)
        main_stat = stat[reg_search(stat, maingrp)]
        temp = str(str(0)+"*"+"\t"+filebase[0]+"\t"+"\t".join(main_stat))
        final.append(temp)
    except:
        print("Error in stat file or bad grp number chosen")
        exit(0)

    #old_grp = grp_arr
    #old_stat = stat 
    #print(main, len(core_index))
    if task != 7:
        print("==== Start tracking ====")
    count = 1 
    for step in filebase[1:]:
        #if task != 7:
        print(str(length - count)+" : "+step)
        if task == 5:
            big_halo = big[count]
            print("Big: %s" %big_halo)
            
        grp_arr = np_read_grp(step+".grp")
        stat = read_stat(step+".stat")

        #grp_values = grp_arr[base_index]
        unique = np.unique(grp_arr[base_index])
        if task != 7:
            print("Unique: %s" %unique.size)
        if task == 0 or task == 1 or task == 5  or task == 7:
            main_result = find_main(base_index, grp_arr)
            main = main_result[0]
            core_index = main_result[1]
            if (task == 1 or task == 5) and maincondition == True:
                base_index = core_index
            main_hist.append(main)
        elif task == 2 or task == 3:
            main = main_hist[count]
            print("Main haloID: %s" %main)
        #if (task == 7 or task == 5 or task == 1) and main == null:
            #break
        #maincondition = True
        for j in unique:
            if(j == null):
                pass
            else:
                j_stat = stat[reg_search(stat, j)]
                if j == main:
                    temp = str(str(count)+"*"+"\t"+step+"\t"+"\t".join(j_stat))
                    final.append(temp)
                else:
                    if task != 1 and task != 5 and task != 7:
                        temp = str(str(count)+"\t"+step+"\t"+"\t".join(j_stat))
                        final.append(temp)

        #old_grp = grp_arr
        #old_stat = stat
        count = count + 1
        if task != 7:
            print("")

    if task == 7:
        return final

    head = []
    header = read_stat_header(step+".stat")
    head.append("StepID(*=main)(0)")
    head.append("Step_name(1)")
    c = 2
    for i in header:
        head.append(i+"(%s)" % c)
        c = c + 1
    head = "\t".join(head)
    """
    try:
        os.system("cd ./gt8_output")
    except:
        os.system("mkdir gt8_output")
    """
    os.system("mkdir -p gt8_output")
    if task == 0:
        filename = "./gt8_output/gt8_%s_%s.dat" %(maingrp, filebase[0].split("/")[-1].replace(".","_"))
    if task ==1:
        filename = "./gt8_output/gt8_CORE(%s)_%s.dat" %(maingrp, filebase[0].split("/")[-1].replace(".","_"))
    if task == 2:
        filename = "./gt8_output/gt8_SUPER(%s)_%s.dat" %(maingrp, filebase[0].split("/")[-1].replace(".","_"))
    if task == 3 or task == 7:
        filename = "./gt8_output/gt8_MERGERS(%s).dat" %(maingrp)
    if task == 5:
        os.system("mkdir -p gt8_output/Satellite_Comparison")
        filename = "./gt8_output/Satellite_Comparison/%s.dat" %(maingrp) 

    with open(filename, "w") as f:
        f.writelines(head+"\n")
        for item in final:
            f.writelines(item+"\n")
    if task == 7:
        tree_vtk(filename)
    else:
        vtk(filename)        
    print("\n==== Success! ====")
    print("\nData stored in gt8_output/gt8_%s_%s.dat" %(maingrp, filebase[0]))
    if task == 3:
        print("Main halo major mergers stored in: \n%sMajorMergers.dat"
              %("./gt8_output/gt8_MERGERS(%s).dat" %(maingrp)))
    return

def robust_track(count, grp_num, particles = []):
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut
    global maingrp, start_step, end_step
    global length, maincondition, big_halo, big
    final = []
    maincondition = True
    old_count = count
    print(count)
    grp_arr = np_read_grp(filebase[count]+".grp")
    core_index = where(grp_arr, grp_num)
    base_index = core_index
    main = grp_num
    main_hist.append(main)

    try:
        stat_file = filebase[count]+'.stat'
        stat = read_stat(stat_file)
        main_stat = stat[reg_search(stat, main)]
        temp = str(str(count)+"*"+"\t"+filebase[0]+"\t"+"\t".join(main_stat))
        final.append(temp)
    except:
        print("Error in stat file or bad grp number chosen")
        exit(0)

    print("==== Start tracking ====")
    for step in filebase[old_count+1:]:
        print("Index: "+str(filebase.index(step))+" : "+step)
        count = filebase.index(step)

        grp_arr = np_read_grp(step+".grp")
        stat = read_stat(step+".stat")
        unique = np.unique(grp_arr[base_index])
        #print("Unique: %s" %unique.size)
        main_result = find_main(base_index, grp_arr)
        main = main_result[0]
        core_index = main_result[1]
        if maincondition == True:
            base_index = core_index
        main_hist.append(main)

        for j in unique:
            if(j == null):
                pass
            else:
                if j == main:
                    j_stat = stat[reg_search(stat, j)]
                    temp = str(str(count)+"*"+"\t"+step+"\t"+"\t".join(j_stat))
                    final.append(temp)
        count = count + 1 

    print("--------------------")
    maincondition == True
    #count = old_count #len(filebase)  
    core_index = where(grp_arr, grp_num)
    base_index = core_index
    for step in filebase[old_count-1::-1]: #Too lazy to use enumerate :-)
        count = filebase.index(step)
        print("Index: "+str(count)+" : "+step)

        grp_arr = np_read_grp(step+".grp")
        stat = read_stat(step+".stat")
        unique = np.unique(grp_arr[base_index])
        #print("Unique: %s" %unique.size)
        main_result = find_main(base_index, grp_arr)
        main = main_result[0]
        core_index = main_result[1]
        if maincondition == True:
            base_index = core_index
        main_hist.append(main)
        j = main
        if(j == null):
                pass
        else:
            if j == main:
                j_stat = stat[reg_search(stat, j)]
                temp = str(str(count)+"*"+"\t"+step+"\t"+"\t".join(j_stat))
                final.append(temp)
        count = count - 1
    final.sort()
    return final
# *** supertrack ***
def supertrack():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task
    global maingrp, start_step, end_step
    global length, maincondition

    main = maingrp
    print("\nThis will execute an extensive procedure to track halos before and AFTER mergers")
    kill = raw_input("This method is very time expensive, are you sure you would like to continue? (y or n): ")
    if kill == "n":
        exit()
    print("Lodaing...")
    
    grp_arr = np_read_grp(filebase[0]+".grp")
    core_index = where(grp_arr, maingrp)
    base_index = core_index
    main = maingrp
    main_hist.append(main)

    # Check if grp has stat 
    try:
        stat_file = filebase[0]+'.stat'
        stat = read_stat(stat_file)
        main_stat = stat[reg_search(stat, maingrp)]
 
    except:
        print("Error in stat file or bad grp number chosen")
        exit(0)
        
    #print("Main: ", main)
    print("Length before: ", base_index.size)
    count = 0
    print("")
    for step in filebase[1:]:
        #print(str(length - count)+" : "+step)
        
        grp_arr = np_read_grp(step+".grp")
        temp = grp_arr[core_index]

        if(temp.size != 0 and maincondition != False):        
            main_result = find_main(core_index, grp_arr)
            main = main_result[0]
            core_index = main_result[1]
            main_hist.append(main)

            #print("Main haloID: ", main)
            if main != null:
                ind = where(grp_arr, main)
                base_index = np.append(base_index, ind)
                base_index = squash(base_index)
        else:
            main_hist.append(main)
     
        print("Step: ", step)
        print("Particles in progenitor: ", core_index.size)
        print("Particles in bin: ", base_index.size)
        print(" ")
        count = count + 1
        
    print("Length after: ", base_index.size)
    return base_index

class halo ():
    def __init__ (self):
        self.p = np.array([])
        self.grp = -2
        self.count = -2
        self.isdead = False

    def add(self, p):
        self.p = squash(np.append(self.p, p))

    def update(self, grp_arr):
        global maincondition, null
        #print("Update: " , self.grp)
        if self.isdead == True:
            return
        temp = maincondition
        maincondition = True
        temp_grp = self.grp
        self.grp, core_index = find_main(self.p, grp_arr)
        if self.grp == null:
            self.grp = temp_grp
            self.isdead = True
        maincondition = temp

def in_tree(target,tree_pass):
    for h in tree_pass:
        if target == h.grp:
            return h
    return None

def mergers ():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut
    global maingrp, start_step, end_step
    global length, maincondition
    masspass = np.array([])
    printout = []
    main_pass = []
    tree_pass = []

    main = maingrp
    grp_arr = np_read_grp(filebase[0]+".grp")
    core_index = where(grp_arr, maingrp)
    base_index = core_index
    main_hist.append(main)
    main_pass = base_index
    # Check if grp has stat 
    try:
        stat_file = filebase[0]+'.stat'
        stat = read_stat(stat_file)
        main_stat = stat[reg_search(stat, maingrp)]
    except:
        print("Error in stat file or bad grp number chosen")
        exit(0)

    print("Gathering main halo merger history...")
    print("")
    count = 1
    for step in filebase[1:]:
        print(str(length - count)+" : "+step)
        if main == null or maincondition == False:
            main_hist.append(null)
        else:
            grp_arr = np_read_grp(step+".grp")
            stat = read_stat(step+".stat")

            temp = grp_arr[core_index]
            unique = np.unique(temp)
            
            main_result = find_main(core_index, grp_arr)
            main = main_result[0]
            core_index = main_result[1]
            main_hist.append(main)

            for h in tree_pass:
                h.update(grp_arr)

            if main == null or maincondition == False or step == filebase[-1]:
                #if task == 7:
                #    main_pass = temp
                if masspass.size == 0:
                    masspass = temp
                else:
                    masspass = np.append(masspass, temp)
                print("*Main added to bin*")
                if task == 7:
                    break
            else:
                mainmass = float(stat[reg_search(stat, main)][5])
                for j in unique:
                    if(j == null) or (j == main):
                        pass
                    else:
                        j_stat = stat[reg_search(stat, j)]
                        ratio = mainmass/float(j_stat[5])
                        if ratio < masscut:
                            if ratio < 1:
                                print("Warning: Target Mass Larger Main Halo")
                            if masspass.size == 0:
                                masspass = temp[temp == j]
                                if task == 7:
                                    h = halo()
                                    h.p = where(grp_arr, j)
                                    h.grp = j
                                    h.count = filebase.index(step)
                                    tree_pass.append(h)
                                    #tree_pass = [where(grp_arr, j)]  
                                    #[temp[temp == j]]
                                    #print(j, "Len1st", len(tree_pass), temp[temp == j].size)
                            else:
                                masspass = np.append(masspass, temp[temp == j])
                                if task == 7:
                                    tree_h = in_tree(j, tree_pass)
                                    if tree_h == None:
                                        h = halo()
                                        h.p = where(grp_arr, j)
                                        h.grp = j
                                        h.count = filebase.index(step)
                                        tree_pass.append(h)
                                    else:
                                        tree_h.add(where(grp_arr, j))
                                    #tree_pass.append(where(grp_arr, j)) #temp[temp == j])
                                    #print(j, "Len", len(tree_pass), temp[temp == j].size)

                            #temp = str(str(count)+"*"+"\t"+step+"\t"+"\t".join(j_stat))
                            print("Major merger at: ", filebase[count-1])#, main, j, mainmass, j_stat[5])
                            #print(j_stat)
                            printout.append([step,j_stat])
            count += 1            
            print("Particles in bin: ", masspass.size)
            print("")
    
    if task == 7:
        return [main_pass, tree_pass]
    #print(printout)
    #exit(0)
    time = "n/a"
    filename = "./gt8_output/gt8_MERGER_info(%s).dat" %(maingrp)
    if len(printout) <= 1:
        print("No Major Mergers at given ratio")
        with open(filename, "w") as ff:
            print(os.getcwd().split('/')[-1])
            ff.write("*** No Major Mergers at given ratio ***" + "\n")
    else:
        with open(step+".stat") as fff:
                header = fff.readline()
        with open(filename, "w") as ff:
            print(os.getcwd().split('/')[-1])
            ff.write("*** Main Halo Major Mergers ***" + "\n")
            ff.write(header)
            ff.write("Core Main Halo (Smallest) @%s"%printout[-1][0] + " :\n")
            ff.write("\t".join(printout[-1][1])+ "\n")
            ff.write(""+ "\n")
            if len(printout) == 1:
                ff.write("No Major Mergers at given ratio"+ "\n")
            for item in printout[:-1]:
                if item == printout[-2] or item == printout[-1]:
                    ff.write("============ END ============\n")
                    break
                if time != item[0]:
                    time = item[0]
                    ff.write("============ %s ============\n" %time)
                    ff.write("\t".join(item[1])+ "\n") 
                else:
                    ff.write("\t".join(item[1])+ "\n")
                #print("\t".join(item[1]))
    return masspass

def track_rad(corefile = "./gt8_output/temp_rad.dat", way = 0):
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, radcut
    global maingrp, start_step, end_step
    global length, maincondition
    main = maingrp
    trace = []
    if way == 0:
        with open(corefile) as f:
            for line in f:
                trace.append(eval(line.split(":")[1]))
    else:
        with open(corefile) as f:
            for line in f:
                trace.append(stoa(line, ":"))


    count = 0 
    final = []
    for i, step in enumerate(filebase):
        print(str(length - count)+" : "+step)
        stat = read_stat(step+".stat")
        if way == 0:
            main = trace[i]
        else:
            main = trace[1]
        print("Main: ", main, " Null: ", null)
        if main != null and  main != "null" and main != str(null):
            if way == 0:
                mstat = stat[reg_search(stat, main)]
                mx = eval(mstat[13])
                my = eval(mstat[14])
                mz = eval(mstat[15])
                mm = float(mstat[5])
            else:
                mx = trace[i][3]
                my = trace[i][4]
                mz = trace[i][5]
                mm = trace[i][2]
            for jstat in stat:
                #jstat = stat[reg_search(stat, j)]
                jx = eval(jstat[13])
                jy = eval(jstat[14])
                jz = eval(jstat[15])
                jm = float(jstat[5])
                r = ((jx - mx)**2+(jy - my)**2+(jz - mz)**2)**(.5)
                if r < radcut and float(mm) > 0 and float(jm) > 0:
                    if float(mm)/float(jm) < float(masscut):
                        temp = str(str(count)+"*"+"\t"+step+"\t"+"\t".join(jstat))
                        final.append(temp)
            count = count + 1

    head = []
    header = read_stat_header(step+".stat")
    head.append("StepID(*=main)(0)")
    head.append("Step_name(1)")
    c = 2
    for i in header:
        head.append(i+"(%s)" % c)
        c = c + 1
    head = "\t".join(head)
    filename = "./gt8_output/gt8_RAD(%s)_%s.dat"%(maingrp, filebase[0].split("/")[-1].replace(".","_"))

    with open(filename, "w") as f:
        f.writelines(head+"\n")
        for item in final:
            f.writelines(item+"\n")

    vtk(filename)

def tracemain():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task
    global maingrp, start_step, end_step
    global length, maincondition
    
    main = maingrp
    grp_arr = np_read_grp(filebase[0]+".grp")
    core_index = where(grp_arr, maingrp)
    base_index = core_index
    main = maingrp
    main_hist.append(main)
    out = []
    if task == 9:
        stat = read_stat(filebase[0]+".stat")
        main_stat = stat[reg_search(stat, main)]
        out.append([str(main), str(main_stat[5]), str(main_stat[13]), str(main_stat[14]), str(main_stat[15])] )
    # Check if grp has stat 
    try:
        stat_file = filebase[0]+'.stat'
        stat = read_stat(stat_file)
        main_stat = stat[reg_search(stat, maingrp)] 
    except:
        print("Error in stat file or bad grp number chosen")
        exit(0)
        
    count = 1 
    for step in filebase[1:]:
        print(str(length - count)+" : "+step)
        if maincondition == True:
            grp_arr = np_read_grp(step+".grp")
            stat = read_stat(step+".stat")
            core_index = whereRemove(core_index, grp_arr.size)
            main_result = find_main(core_index, grp_arr)
            main = main_result[0]
            core_index = main_result[1]
            main_hist.append(main)
            if task == 9 and main != null:
                main_stat = stat[reg_search(stat, main)]
                out.append([str(main), str(main_stat[5]), str(main_stat[13]), str(main_stat[14]), str(main_stat[15])])
            else:
                out.append(["null" , "null" , "null" , "null" , "null" , "null"])
        else:
            main_hist.append(null)
            if task == 9:
                out.append(["null" , "null" , "null" , "null" , "null" , "null"])
                #out.append("null : null : null : null : null : null")
        count += 1
        print("")
    os.system("mkdir -p gt8_output")
    if task == 45:
        os.system("mkdir -p gt8_output/Satellite_Comparison")
        filename = "./gt8_output/Satellite_Comparison/main.dat" 
    elif task == 7:
        filename = "gt8_main.dat"
    elif task == 9:
        filename = "./gt8_output/gt8_TRACE(%s)_%s.dat" %(maingrp, filebase[0].split("/")[-1].replace(".","_")) 
        filename2 = "./gt8_output/temp_rad.dat"
    else:
        filename = "./gt8_output/gt8_TRACE(%s)_%s.dat" %(maingrp, filebase[0].split("/")[-1].replace(".","_"))
    with open(filename, "w") as f:
        for count, item in enumerate(filebase):            
            f.write(item+" : "+str(main_hist[count])+"\n")
    if task == 9:
        with open(filename2, "w") as f:
            for count, item in enumerate(filebase):            
                f.write(item+" : "+" : ".join(out[count])+"\n")

    print("Trace Main was used: main halo history stored in: \n%s\n" % filename)    

def find_main(core_index, grp_arr):
    global filebase , crap_files
    global stat_header, main_hist
    global null, task
    global maingrp, start_step, end_step
    global length, maincondition, big_halo
    print(grp_arr.size, core_index[-1])
    temp = grp_arr[core_index]
    #print(maincondition)

    if temp.size == 1 and type(temp) != int:
        print("Type convert.")
        #if temp == null or task == 7:
        return null, temp
        #else:
        #    eturn temp[0], temp 
    if temp.size == 0 or maincondition == False:
        if task != 7:
            print("Main haloID: %s" %null)
        #main_hist.append(null)
        maincondition = False
        return null, core_index
    if task == 5:
        main = mode2(temp)
    else:
        main = mode(temp)
        
    
    #main_hist.append(main)
    if task != 7:
        print("Main haloID: %s" %main)
    if main != null:
        ind = where(temp, main)
        core_index = core_index[ind]
    elif task != 5:
        maincondition = False
    else:
        main = mode(temp)
        if main == null:
            maincondition = False
            #error("this one")
            
            
            
    return main, core_index

def plot_universe():
	global filebase , crap_files
	global stat_header, main_hist
	global null, task, masscut
	global maingrp, start_step, end_step
	global length, maincondition, big_halo
	final = []
	count = 1
	for step in filebase:
		print(str(length - count)+" : "+step)
		stat = read_stat(step+".stat")
		for j in stat:
			if(eval(j[5]) < 10**masscut):
				pass
			else:
				j_stat = j
				temp = str(str(count)+"\t"+step+"\t"+"\t".join(j_stat))
				final.append(temp)
		count += 1
	head = []
	header = read_stat_header(step+".stat")
	head.append("StepID(*=main)(0)")
	head.append("Step_name(1)")
	c = 2
	for i in header:
	    head.append(i+"(%s)" % c)
	    c = c + 1
	head = "\t".join(head)
	filename = "./gt8_output/gt8_Universe(MCut%s)_%s.dat" %(masscut,filebase[0].split("/")[-1].replace(".","_"))
	with open(filename, "w") as f:
	    f.writelines(head+"\n")
	    for item in final:
	        f.writelines(item+"\n")

	vtk(filename)
	print("\n==== Success! ====")

def movie():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut
    global maingrp, start_step, end_step
    global length, maincondition, big_halo
    final = []
    count = 1
    for step in filebase:
        final = []
        print(str(length - count)+" : "+step)
        stat = read_stat(step+".stat")
        for j in stat:
            if(eval(j[5]) < 10**masscut):
                pass
            else:
                j_stat = j
                temp = str(str(count)+"\t"+step+"\t"+"\t".join(j_stat))
                final.append(temp)
        count += 1
        head = []
        header = read_stat_header(step+".stat")
        head.append("StepID(*=main)(0)")
        head.append("Step_name(1)")
        c = 2
        for i in header:
            head.append(i+"(%s)" % c)
            c = c + 1
        head = "\t".join(head)
        os.system("mkdir -p gt8_output")
        os.system("mkdir -p ./gt8_output/movie")
        filename = "./gt8_output/movie/Frame%s.dat" %(length-count)
        with open(filename, "w") as f:
            f.writelines(head+"\n")
            for item in final:
                f.writelines(item+"\n")
        vtk(filename)
    print("\n==== Success! ====")

def LargestHalo():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut, outter
    global maingrp, maingrp2, start_step, end_step
    global length, path, big, h_id, skip
    global roots, rankcut

    stat = read_stat(filebase+".stat")
    stat = sorted(stat, key = lambda x: -1*eval(x[5]))
    for i in stat:
        if 'contam' not in i[19]:
            print("\nLargest Halo:")
            print("GRP: " + i[0])
            print("Mass: " + i[5])
            print("")
            return

def Pmovie():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut, CT_file
    global maingrp,maingrp2, start_step, end_step
    global length, path, rankcut, radcut

    data = []
    os.system("mkdir -p ./gt8_output/Pmovie")
    for i, step in enumerate(filebase[0:1]):
        f = filebase[0].replace(".amiga","")
        print(f)
        s = pnb.load(f)
        s.physical_units()
        h = s.halos()
        h1 = h[1]
        
        print("1")    
        p = h1.dm["pos"]
        Pvtk(p, "h1 dm")
        print("2")
        p = h1.s["pos"]
        Pvtk(p, "h1 stars")
        print("3")
        p = h1.g["pos"]
        Pvtk(p, "h1 gas")
        



# =============== Consistent Trees(CT) ===============
class CT_halo ():
    def __init__ (self):
        self.prog = [] 
        self.data = None
        self.major = False
        self.ragid = -1
        self.ragclip = -1

        self.scale= -1
        self.id= -1
        self.desc_scale= -1
        self.desc_id= -1
        self.num_prog= -1
        self.pid= -1
        self.upid= -1
        self.desc_pid= -1
        self.phantom= -1
        self.sam_mvir= -1
        self.mvir= -1
        self.rvir= -1
        self.rs= -1
        self.vrms= -1
        self.mmp= -1
        self.scale_of_last_MM= -1
        self.vmax= -1
        self.x= -1
        self.y= -1
        self.z= -1
        self.vx= -1
        self.vy= -1
        self.vz= -1
        self.Jx= -1
        self.Jy= -1
        self.Jz= -1
        self.Spin= -1
        self.Breadth_first_ID= -1
        self.Depth_first_ID= -1
        self.Tree_root_ID= -1
        self.Orig_halo_ID= -1
        self.Snap_num= -1
        self.Next_coprogenitor_depthfirst_ID= -1
        self.Last_progenitor_depthfirst_ID= -1
        
    def add ( self ,scale ,hid ,desc_scale ,desc_id ,num_prog ,pid ,upid ,desc_pid ,phantom ,sam_mvir ,mvir ,rvir ,rs ,vrms 
              ,mmp ,scale_of_last_MM ,vmax ,x ,y ,z ,vx ,vy ,vz ,Jx ,Jy ,Jz ,Spin ,Breadth_first_ID ,Depth_first_ID 
              ,Tree_root_ID ,Orig_halo_ID ,Snap_num ,Next_coprogenitor_depthfirst_ID ,Last_progenitor_depthfirst_ID, dataIN):
        self.scale = scale
        self.id = int(hid)
        self.desc_scale = desc_scale
        self.desc_id = int(desc_id)
        self.num_prog = num_prog
        self.pid = pid
        self.upid = upid
        self.desc_pid = desc_pid
        self.phantom = phantom
        self.sam_mvir = sam_mvir
        self.mvir = mvir
        self.rvir = rvir
        self.rs = rs
        self.vrms = vrms
        self.mmp = mmp
        self.scale_of_last_MM = scale_of_last_MM
        self.vmax = vmax
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.Jx = Jx
        self.Jy = Jy
        self.Jz = Jz
        self.Spin = Spin
        self.Breadth_first_ID = int(Breadth_first_ID)
        self.Depth_first_ID = int(Depth_first_ID)
        self.Tree_root_ID = int(Tree_root_ID)
        self.Orig_halo_ID = int(Orig_halo_ID)
        self.Snap_num = int(Snap_num)
        self.Next_coprogenitor_depthfirst_ID = int(Next_coprogenitor_depthfirst_ID)
        self.Last_progenitor_depthfirst_ID = int(Last_progenitor_depthfirst_ID)
        self.data = dataIN

def find_old_halo (target, stepnum, halos):
    for h in halos:
        if h.Orig_halo_ID == target and h.scale == 1.0000: # h.snap_num == stepnum
            return h
    return -1   

def find_halo (target, halos, halo_ids):
    if target == -1:
        return -1
    #ind = halo_ids.index(target)
    ind = np.where(halo_ids == target)[0]
    return halos[ind]

def CT_tree_vtk(plot, dr):
    global added_ids, masscut, maingrp
    global task
    print("generating .vtk")
    os.system("mkdir -p gt8_output")
    data = plot
    if task == 111:        
        filename = "./gt8_ConsTree_grp(%s)" %maingrp
    else: 
        filename = "./gt8_ConsTree(%s)" %maingrp
    npoints = len(data)
    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            #print(l)
            f.write(" ".join([str(float(l[1])),str(float(l[2])),str(float(l[0])*dr)+ "\n"]))
            #f.write(" ".join([str(l[2]), str(l[3]), str(l[4])])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        #u = 0
        for l in data: 
            if int(l[10]) in added_ids:
                f.write('2'+" "+str(int(l[9]))+" "+str(int(l[10]))+ "\n")
            else:
                f.write('2'+" "+str(int(l[9]))+" "+str(int(l[9]))+ "\n")
            #f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            #u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('3'+ "\n")
        
        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %4+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(log10(float(l[7])))+ "\n")
        f.write('Rvir 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(float(l[8]))+ "\n")
        f.write('Velocities 3 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([ str(float(l[4])), str(float(l[5])), "0\n"]))
        f.write('Phantom 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(int(l[11]))+"\n")
def CT_vtk(plot, dr):
    global added_ids, masscut, maingrp
    global task
    print("generating .vtk")
    os.system("mkdir -p gt8_output")
    data = plot
    if task == 111:        
        filename = "./gt8_ConsTree_Track_grp(%s)" %maingrp
    else: 
        filename = "./gt8_ConsTree_Track(%s)" %maingrp
    npoints = len(data)
    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            #print(l)
            f.write(" ".join([str(float(l[1])),str(float(l[2])),str(float(l[3]))+ "\n"]))
            #f.write(" ".join([str(l[2]), str(l[3]), str(l[4])])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        #u = 0
        for l in data: 
            if int(l[10]) in added_ids:
                f.write('2'+" "+str(int(l[9]))+" "+str(int(l[10]))+ "\n")
            else:
                f.write('2'+" "+str(int(l[9]))+" "+str(int(l[9]))+ "\n")
            #f.write('2'+" "+str(u)+" "+str(0)+ "\n")
            #u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('3'+ "\n")
        
        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %4+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(log10(float(l[7])))+ "\n")
        f.write('Rvir 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(float(l[8]))+ "\n")
        f.write('Velocities 3 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([ str(float(l[4])), str(float(l[5])), str(float(l[6]))])+"\n")
        f.write('Phantom 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(int(l[11]))+"\n")

def CT_tree():
    global added_ids, maingrp, masscut, CT_file, task
    filename = CT_file
    data = []
    junck = []
    print("Loading file...")
    with open(filename) as f:
        for line in f:
            if '#' not in line:
                line = line.split()
                if len(line) > 1:
                    line = np.array(line, dtype = float).tolist()
                    data.append(line)
            else: 
                junck.append(line)
    print("\033[32mok\033[0m") 
    halos = []
    halo_ids = []
    print("Loading Halos...")
    for p_args  in data:
        h = CT_halo()
        #p_args = data[0]
        h.add(p_args[0] ,p_args[1] ,p_args[2] ,p_args[3] ,p_args[4] ,p_args[5] ,p_args[6] ,p_args[7] ,p_args[8] ,p_args[9] 
              ,p_args[10] ,p_args[11] ,p_args[12] ,p_args[13] ,p_args[14] ,p_args[15] ,p_args[16] ,p_args[17] ,p_args[18] 
              ,p_args[19],p_args[20] ,p_args[21] ,p_args[22] ,p_args[23] ,p_args[24] ,p_args[25] ,p_args[26] 
              ,p_args[27] ,p_args[28],p_args[29] 
              ,p_args[30] ,p_args[31] ,p_args[32] ,p_args[33],p_args)
        halos.append(h)
        halo_ids.append(h.id)
    
    halo_ids = np.array(halo_ids, dtype = int)
    length2 =  len(halos)
    print("Traversing the halo graph...")
    for i, h in enumerate(halos):
        if(i%10000) == 0:
             print(i,"/", length2)
        h2 = find_halo(h.desc_id, halos, halo_ids)
        if h2 != -1:
            h2.prog.append(h)
    print("\033[32mok\033[0m")
    if task == 11 or task == 0:
        h = find_halo(maingrp, halos, halo_ids)
    else:
        h = find_old_halo(maingrp, 1, halos)#2438
    h.major = True
    h.ragid = 0
    h.ragclip = 0
    center = [h.x, h.y,h.z,h.vx,h.vy,h.vz]
    zero = h.Snap_num
    final = [] 
    final2 = []
    hive = [h]
    added_ids = []
    rag = 1
    print(h.Orig_halo_ID, h.id, h.scale, h.Snap_num, int(h.ragid))
    while len(hive) != 0:
        temp = []
        for h in hive:
            #print(h.Orig_halo_ID, h.id, h.scale,int(h.ragid))
            print(h.id,h.scale,"(",h.ragid, h.ragclip,")")
            

            final.append([zero - h.Snap_num,h.x - center[0],h.y - center[1],h.z - center[2], h.vx - center[3],h.vy - center[4],h.vz - center[5], h.mvir, h.rvir, h.ragid, h.ragclip, h.phantom])
            final2.append([zero - h.Snap_num, h.x, h.y, h.z, h.vx, h.vy, h.vz, h.mvir, h.rvir, h.ragid, h.ragclip, h.phantom])
            added_ids.append(int(h.ragid))
            #print(int(h.ragid))
            progs = [] 
            progmass = []
            for j in h.prog:
                #print(j.Orig_halo_ID, j.id, j.scale)
                progmass.append(j.mvir)
            if len(progmass) == 0:
                pass
            else:
                hmain = h.prog[progmass.index(max(progmass))]
                if h.major == True:
                    main = hmain
                    main.major = True
                    center2 = [main.x, main.y,main.z, main.vx, main.vy, main.vz]
                    for xhalo in h.prog:
                        if main.mvir/xhalo.mvir <= masscut:
                            xhalo.ragid = rag
                            xhalo.ragclip = h.ragid
                            #print(rag)
                            rag += 1
                            temp.append(xhalo)
                else:
                    hmain.ragid = rag
                    hmain.ragclip = h.ragid
                    #print(rag)
                    rag += 1
                    temp.append(hmain)
        center = center2
        hive = temp
        print("="*10)

    CT_tree_vtk(final, 0.0582) #Change 2nd arg for scale. 
    CT_vtk(final2, 0.0582)

# =============== Satellite Comparison ===============
def comparison():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut
    global maingrp, maingrp2, start_step, end_step
    global length, path, big
    
    main1 = maingrp
    main2 = maingrp2
    here = os.getcwd()
    filebase_here = filebase
    data = []
    step = filebase[0]
    stat = step+".stat"
    with open(step+".stat") as f:
        f.readline()
        for line in f:
            line = line.split()
            temp = []
            for i in line:
                try:
                    temp.append(eval(i))
                except:
                    temp.append(i)
            data.append(temp)

    #fil = open("satellite.dat","w")
    os.chdir(path)
    filebase = []
    find_filebase()
    filebase_path = filebase
    
    data2 = []
    step2 = filebase[0]
    stat2 = step2+".stat"
    print("\n\n\n\033[47m\033[30mComparing files\033[0m\033[0m : ",step,step2)
    
    with open(step2+".stat") as f:
        f.readline()
        for line in f:
            line = line.split()
            temp = []
            for i in line:
                try:
                    temp.append(eval(i))
                except:
                    temp.append(i)
            data2.append(temp)

    for main in data:
        if main[0] == main1:
            maingrp_mass = main[5]
            break
        
    low = []
    high = []
    for main in data:
        if main[19] != 'contam' and (main[20] == main1 or main[0] == main1) and main[5]!=0:
            low.append(main)

    for main in data2:
        #if main[19] != 'contam': #and (main[20] == main2  or main[0] == main2) and main[5]!=0:
        high.append(main)
            
    low = sorted(low, key = lambda x: x[5])
    high = sorted(high, key = lambda x: x[5])

    low = reverse_list(low)
    high = reverse_list(high)
    #"""
    if len(low) > 25:
        low = low[:25+1]
    if len(high) > 600:
        high = high[:850+1]#850+1]
    for i, item in enumerate(low):
        print([item[0],item[5]])
    """
    if len(low) > 5:
        low = low[:5]
    if len(high) > 10:
        high = high[:10]
    for i, item in enumerate(low):
        print([item[0],item[5]])
    """
    print("")
    for item in high:
        print([item[0],item[5]])

    task = 45

    os.chdir(here)
    filebase = filebase_here
    maingrp = main1
    main_hist = []
    tracemain()
    big1 = []
    with open("./gt8_output/Satellite_Comparison/main.dat") as f:
        for line in f:
            line = line.replace("\n","").split(":")
            #print(line)
            big1.append(int(line[1]))
    f.close()        

    os.chdir(path)
    maingrp = main2
    filebase = filebase_path
    main_hist = []
    tracemain()
    big2 = []
    with open("./gt8_output/Satellite_Comparison/main.dat") as ff:
        for line in ff:
            line = line.replace("\n","").split(":")
            print(line[1])
            big2.append(int(line[1]))
    print(big1)
    print("")
    print(big2)
    
    task = 5
    
    os.chdir(here)
    filebase = filebase_here
    big = big1
    #"""
    for main in low:
        if int(main[0]) != main1:
            task = 5
            maingrp = int(main[0])
            print("Multi-CoreTrack, grp: ", maingrp)
            main_hist = []
            track()


    #"""
    os.chdir("./gt8_output/Satellite_Comparison")
    sim1_files = []
    for item in glob.glob("*.dat"):
        sim1_files.append(item)
    print(sim1_files)
    sim1_files.remove("main.dat")
    sim1_data = {}
    for fl in sim1_files:
        tempfl = []
        sim1_data[fl]= []
        with open(fl) as f:
            f.readline()
            for line in f:
                line = line.split()
                #print(line)
                d = np.array([eval(line[15]),eval(line[16]),eval(line[17])])
                tempfl.append(d)
        sim1_data[fl]= tempfl
       

    os.chdir(path)
    filebase = filebase_path
    big = big2
    #"""
    for main in high:
        if int(main[0]) != main2:
            task = 5
            maingrp = int(main[0])
            print("Multi-CoreTrack, grp: ", maingrp)
            main_hist = []
            track()
    #"""
    os.chdir("./gt8_output/Satellite_Comparison")
    sim2_files = []
    for item in glob.glob("*.dat"):
        sim2_files.append(item)
    sim2_files.remove("main.dat")    
    sim2_data = {}
    for fl in sim2_files:
        tempfl = []
        sim2_data[fl]= []
        with open(fl) as f:
            f.readline()
            for line in f:
                line = line.split()
                #print(line)
                d = np.array([eval(line[15]),eval(line[16]),eval(line[17])])
                tempfl.append(d)
        sim2_data[fl]= tempfl

    os.chdir(here)
    filebase = filebase_here
    winners  = []
    other = []
    os.system("mkdir -p temp_plots")
    
    for key in sim1_data:
        #halo1_name = key
        arr1 = sim1_data[key]
        print("===",key,"===")
        res = []
        id2 = []
        zones = []
        #fxf = open("./temp_plots/"+str(key),"w")
        for joi, key2 in enumerate(sim2_data):
            #halo2_name = key2
            arr2 = sim2_data[key2] 
            id2.append(key2)
            tot = 0
            zone = []
            late = 0 
            if abs(len(arr1)-len(arr2)) <= 6:
                late = 0
                for di, dj in zip(arr1, arr2):
                    if late > -1:
                        dz = di-dj
                        r = np.dot(dz,dz)**.5
                        zone.append(str(r))
                        tot += r
                    late += 1
            else:
                tot = 10**10
            res.append(tot)
            zones.append(zone)
            #fxf.write(key2.replace(".dat","")+"\t"+"\t".join(zone)+"\n")
        #fxf.close()
        ind = res.index(min(res))
        winner = id2[ind]
        winval = min(res)
        print("Match: " ,key,winner,winval)
        winners.append("\t".join([str(key.replace(".dat","")),str(winner.replace(".dat","")),str(winval)]))
        other.append("\n".join([str(key.replace(".dat","")), str(sorted(res)),str(res),str(id2)]))
        
        dodo = sorted(res)
        plot_data = []
        fxf = open("./temp_plots/"+str(key),"w")
        for counti in range(15):
            ind = res.index(dodo[counti])
            plot_data.append(zones[ind])
            fxf.write(id2[ind].replace(".dat","")+"\t"+"\t".join(zones[ind])+"\n")
        fxf.close()
        print("")
        """    
        print("")
        print(res)
        print(id2)
        print("")
        print("")
        """
    with open("./gt8_output/satellite_matches.dat","w") as f:
        for winner in winners:
            f.write(winner+"\n")
    with open("./gt8_output/satellite_matches2.dat","w") as f:
        for winner in other:
            f.write(winner+"\n")

    print("")
    #print("Great Success!!!")
    usa()
    print("")
    print("Great Success!!!\n")
    print("Output: satellite_matches.dat")
    exit(0)
    
# =============== Tree and track ====================
def setup_tree(finalx):
    temp = []
    for i in finalx:
        temp.append(i.split("\t"))
    return temp

def find_dr(main_branch):
    #x = []
    #y = []
    #z = []
    r = []
    l = len(main_branch)
    if l < 2:
        x = abs(float(line[15])-float(main_branch[i-1][15]))
        y = abs(float(line[16])-float(main_branch[i-1][16]))
        z = abs(float(line[17])-float(main_branch[i-1][17]))
        dr = math.sqrt(x**2+y**2+z**2)
        return dr

    for i, line in enumerate(main_branch[1:]):
        x = abs(float(line[15])-float(main_branch[i-1][15]))
        y = abs(float(line[16])-float(main_branch[i-1][16]))
        z = abs(float(line[17])-float(main_branch[i-1][17]))
        dr = math.sqrt(x**2+y**2+z**2)
        r.append(dr)
    """
    dx = sum(x)/len(x)
    dy = sum(y)/len(y)
    dz = sum(z)/len(z)
    """
    dr = sum(r)/len(r)
    return dr/8 #[dx,dy,dz]

def tree_vtk(plot, dr):
    global maingrp, masscut
    print("generating .vtk")
    data = plot        
    filename = "./gt8_output/gt8_Tree("+str(maingrp)+")"+"ratio("+str(masscut)+")"
    npoints = len(data)
    with open(filename+".vtk","w") as f:
        f.write('# vtk DataFile Version 3.0'+ "\n")
        f.write('vtk output'+ "\n")
        f.write('ASCII'+ "\n")
        f.write('DATASET UNSTRUCTURED_GRID'+ "\n")
        f.write('POINTS %d float' %(npoints)+ "\n")
        for l in data:
            #print(l)
            f.write(" ".join([str(l[1]),str(l[2]),str(l[0]*dr)+ "\n"]))
            #f.write(" ".join([str(l[2]), str(l[3]), str(l[4])])+ "\n")
                    
        f.write(''+ "\n")
        f.write('CELLS %d %d' %(npoints, npoints*3 )+ "\n")
        #u = 0
        for l in data: 
            f.write('2'+" "+str(l[9])+" "+str(l[10])+ "\n")
            #u = u + 1
        f.write(''+ "\n")
        f.write('CELL_TYPES %d' %(npoints)+ "\n" )
        for l in data: # ignore first line (final single halo)
            f.write('3'+ "\n")
        
        f.write(''+ "\n")
        f.write('POINT_DATA %d' %(npoints)+ "\n")
        f.write('FIELD FieldData %d' %3+ "\n")
        f.write('LogHaloMass 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(log10(float(l[7])))+ "\n")
        f.write('Rvir 1 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(str(l[8])+ "\n")
        f.write('Velocities 3 %d double' %(npoints)+ "\n")
        for l in data:
            f.write(" ".join([ str(l[4]), str(l[5]), "0\n"]))
        
def tree ():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut, outter
    global maingrp, maingrp2, start_step, end_step
    global length, path, big, h_id, skip
    global roots, rankcut
    
    maincondition = True
    """
    if len(ps) != 0:
        for i in ps:
            print(i.size)
    """
    #elif task == 3 or task == 7:
    os.system("mkdir -p gt8_output")
    main_p, halos = mergers()
    main_branch = setup_tree(track(main_p))
    dr = find_dr(main_branch)
    """
    for  i in o:
        print(i.split("\t"))
    """
    final = [main_branch]
    for i, h in enumerate(halos):
        print("=====",i+1, "out of", len(halos),"=====")
        finalx = track(h.p)#robust_track(h.count, h.grp, h.p) #track(h.p)
        print(finalx)
        final.append(setup_tree(finalx))
        #print(final)
    #"""

    plot = []
    now_id = 0 
    #print(main_branch[0], len(main_branch[0]))
    #print(main_branch[0][15])
    for j, finalx in enumerate(final):
        print(j)
        last_id = now_id
        file_length = len(finalx)
        for i, line in enumerate(finalx):
            temp = []
            try:
                mx = float(main_branch[i][15])
                my = float(main_branch[i][16])
                mz = float(main_branch[i][17])
                mvx = float(main_branch[i][18])
                mvy = float(main_branch[i][19])
                mvz = float(main_branch[i][20])
            except:
                pass
                #print("pass")
            
            temp= [int(line[0].replace("*","")),
            float(line[15])-mx,
            float(line[16])-my,
            float(line[17])-mz,
            float(line[18])-mvx,
            float(line[19])-mvy,
            float(line[20])-mvz,
            float(line[7]),float(line[8]),
            now_id, last_id]
                
            last_id = now_id
            now_id += 1 
            plot.append(temp)
    tree_vtk(plot, dr)

def rescale():
    print("")
    print("This method will multiply the time component of the each data point by a scalar const.")
    filenm = raw_input("Tree file name (include path and .vtk): ")#"gt8_Tree(1).vtk"
    data = []
    scale = input("Scale: ")
    with open(filenm) as f:
        cond = 0
        for line in f:
            if cond == 1:
                if line == "\n" or "CELLS" in line:
                    cond = 2
                else:
                    #print("\n"+line)
                    line = line.split()
                    #line = [str(float(i)*scale) for i in line]
                    line[2] = str(float(line[2])*scale)
                    line = " ".join(line)
                    #print(line+"\n")
            elif "POINTS " in line:
                cond = 1
            data.append(line)

    with open("Scaled.vtk", "w") as f:
        for line in data:
            f.write(line)




# =============== options ===============
def options ():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut, CT_file
    global maingrp,maingrp2, start_step, end_step
    global length, path, rankcut, radcut
    print("")
    print("Enter: (0) Qucik Track | (1) CoreTrack | (2) SuperTrack")
    print("       (3) Mergers(with mass cutoff) | (4) Only Trace Main Halo {No tracking}")
    print("       (5) Satellite Comparison | (6) Multi-CoreTrack | (7) MakeTree")  
    print("       (8) Rescale Tree(only for trees) | (9) Within radius | (10) Plot_Universe") 
    print("       (11) Consistent_Trees to VTK | (12) Reverse Track | (13) Movie") 
    print("       (14) Find Largest Halo | (15)Pmovie")
    task = input("Option => ")
    print("")
    os.system("mkdir -p gt8_output")
    if task == 15:
        Pmovie()
        return
    if task == 11:
        CT_file = raw_input("Consistent Tree file: ")
        main_type = raw_input("Main halo Consistent_Trees ID (type 'grp' to use grp#): ")
        if "grp" in main_type:
            task = 111
            maingrp = input("Main halo grp number @ start step: ")
        else:
            maingrp = eval(main_type)
        masscut = input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        CT_tree()
        return
    if task == 8:
        rescale()
        return
    if task == 5:
        #print("\033[33mDisabled.\033[0m")
        """
        maingrp = 1331#input("Main halo grp number of low resolution main halo: ")
        maingrp2 = 2794#input("Main halo grp number of high resolution main halo: ")
        path = "/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072/h277.cosmo50cmb.3072.rockstar" #raw_input("Path to higher resolution files/gt8_filebase: ").strip()
        comparison()
        """
        return
    if task == 6:
        mainList = raw_input("List of main halo grps separated by ';': ")
        mainList = mainList.split(';')
        task = 1
        for main in mainList:
            maingrp = eval(main)
            print("Multi-CoreTrack, grp: ", maingrp)
            
            main_hist = []
            track()
        return

    if task == 14:
        print_filebase()
        start_step = input("Step index (0 for lowest redshift): ")
        filebase = filebase[start_step]
        LargestHalo()
        return

    if task != 10 and task != 13:
    	maingrp = input("Main halo grp number @ start step: ")
    else:
    	masscut = input('Log mass cutoff(10^x) where x > ')
    	if task == 10:
            plot_universe()
        else:
            movie()
    	return
    print_filebase()

    start_step = input("Start step index (0 for lowest redshift): ")
    if task != 12:
        end_step = input("Last step index to include(or -1 for end of list): ")
        if end_step == -1:
            end_step = length - 1 

    if task == 12:
        filebase = filebase[start_step::-1]
        tracemain()
        return
    else:
        filebase = filebase[start_step : end_step + 1]

    if task == 0:
        track()
    if task == 1:
        track()
    if task == 2:
        track()
    if task == 3:
        masscut = input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        track()
    if task == 4:
        tracemain()
    if task == 7:
        #maingrp2 = 1331#input("Dominant halo: ")
        masscut = input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        #rankcut = input("Rank cutoff: ")
        tree()
        #track()
    if task == 9:
        masscut = input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        radcut= input("Max R from halo's core (Mpc): ")
        print("Would you like to use the grp (g) entered or file(f)?")
        opt_fg = raw_input("(g/f)? ")
        if opt_fg == "f":
            print("The file must be temp_rad.dat or in similar format!")
            print("You can use option (9 + 'g') to generate file")
            corefile = raw_input("File name with path? ")
            track_rad(corefile, 1)
        else:
            tracemain()
            track_rad()

def options2():
    global filebase , crap_files
    global stat_header, main_hist
    global null, task, masscut, CT_file
    global maingrp,maingrp2, start_step, end_step
    global length, path, rankcut, radcut
    print("")
    error("No grp files found... showing limited options:")
    print("Copy this file to dir with grp and stat files for more options.")
    print("")
    print("Enter: (0) Consistent_Trees to VTK | (1) Rescale Tree(only for trees)")
    task = input("Option => ")
    print("")
    os.system("mkdir -p gt8_output")
    if task == 0:
        CT_file = raw_input("Consistent Tree file: ")
        main_type = raw_input("Main halo Consistent_Trees ID (type 'grp' to use grp#): ")
        if "grp" in main_type:
            task = 111
            maingrp = input("Main halo grp number @ start step: ")
        else:
            maingrp = eval(main_type)
        masscut = input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        CT_tree()

    if task == 1:
        rescale()
    exit(0)
    
# What's code without a little fun...    
def usa():
    """
    print("*\033[34m*\033[0m"*4+ "\033[31m"+"="*14+"\033[0m\n" +"\033[34m*\033[0m*"*4 +
          "\033[0m"+"="*14+"\033[0m\n"+"*\033[34m*\033[0m"*4+ "\033[31m"+"="*14+"\033[0m\n"+
          "\033[0m"+"="*22+"\n"+ "\033[31m"+"="*22+"\033[0m")
    """
    print("\033[44m *"*5+ "\033[0m\033[41m"+" "*14+"\033[0m\n"
          +"\033[44m* "*5 + "\033[0m\033[47m"+" "*14+"\033[0m\033[0m\n"
          +"\033[44m *"*5+ "\033[0m\033[41m"+" "*14+"\033[0m\033[0m\n"
          +"\033[44m* "*5 + "\033[0m\033[47m"+" "*14+"\033[0m\033[0m\n"
          +"\033[0m\033[41m"+" "*24+"\033[0m\n"+"\033[0m\033[47m"
          +" "*24+"\033[0m\033[0m\033[0m\n"+"\033[0m\033[41m"+" "*24
          +"\033[0m\n")
        
#=========== Gentrack 6.1.0 ==============
if __name__ == '__main__':
    print("Gentrack 6")
    global filebase , crap_files
    global stat_header
    global null, task, masscut
    global maingrp, start_step, end_step
    global length, path
    global maincondition
    maincondition = True
    null = -1
    filebase = []
    crap_files = []
    main_hist = []

    # *** Load files ***
    find_filebase()
    length = len(filebase)

    # ***find null value***
    if('amiga' in filebase[0] or 'AHF' in filebase[0]):
        null = 0
    else:
        arr = read_grp(filebase[0]+'.grp')
        if "-1" in arr:
            null = -1
        else:
            null = 0
    if len(argv) == 2:
        maingrp = eval(argv[1])
        task = 0
        track()
    elif(len(argv) == 4) and ( "t" in argv or "tree" in argv or "Tree" in argv or "TREE" in argv):
        task = 7
        maingrp = eval(argv[2])
        masscut = eval(argv[3]) #input('Mass ratio cutoff (mass of main halo/ mass of x halo): ')
        tree()

    else:
        options()   

