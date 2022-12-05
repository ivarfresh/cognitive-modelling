import matplotlib.pyplot as plt
import numpy as np

#defines start time
def start() -> int: 
    return 0

#defines perception time
def perceptualstep(p_type = 'middle') -> int:
    if p_type == 'slow':
        return 200
    elif p_type == 'middle':
        return 100
    elif p_type == 'fast':
        return 50

#defines cognitive time
def cognitivestep(c_type = 'middle') -> int:
    if c_type == 'slow':
        return 170
    elif c_type == 'middle':
        return 70
    elif c_type == 'fast':
        return 25
    
#defines motor time
def motorstep(m_type = 'middle') -> int:
    if m_type == 'slow':
        return 100
    elif m_type == 'middle':
        return 70
    elif m_type == 'fast':
        return 30

def example1() -> int:
    ts = start()
    tp = perceptualstep()
    tc = cognitivestep()
    tm = motorstep()
    
    total_time = ts + tp + tc + tm
    
    print("Example1 time:")
    print(f"{total_time}")
    print()
    return total_time

#defining the possible times for all processes
t_s = start()
t_p = [perceptualstep(p_type = 'fast'), perceptualstep(p_type = 'middle'), perceptualstep(p_type = 'slow')]
t_c = [cognitivestep(c_type = 'fast'), cognitivestep(c_type = 'middle'), cognitivestep(c_type = 'slow')]
t_m = [motorstep(m_type = 'fast'), motorstep(m_type = 'middle'), motorstep(m_type = 'slow')]
labels = ["fast", "middle", "slow"]
multiplier = [3,2,0.5]

def example2(completeness = 'extremes'):
    if completeness == 'extremes':
        tp_f = t_p[0]
        tc_f = t_c[0]
        tm_f = t_m[0]
        time_f = t_s + tp_f + tc_f + tm_f

        tp_m = t_p[1]
        tc_m = t_c[1]
        tm_m = t_m[1]
        time_m = t_s + tp_m + tc_m + tm_m
        
        tp_s = t_p[2]
        tc_s = t_c[2]
        tm_s = t_m[2]
        time_s = t_s + tp_s + tc_s + tm_s
        print(f'Fastman time: {time_f}, Middleman time: {time_m}, Slowman time: {time_s}')
        return time_f, time_m, time_s
    
    elif completeness == 'all':
        output = []
        for p_index, p in enumerate(t_p):
            for c_index, c in enumerate(t_c):
                for m_index, m in enumerate(t_m):
                  value = p+c+m
                  print(f"{p} ({labels[p_index]}) + {c} ({labels[c_index]}) + {m} ({labels[m_index]}) = {value}")
                  output.append(value)
                  output.sort()
        
        print("All combinations:")
        print(f"{output}")
        print()
        
        #plot
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.boxplot(output)
        ax.set_ylabel('time (ms)')
        ax.set_ylim([0, 500])
        # show plot
        plt.show()

# =============================================================================
# example1()
# 
example2(completeness = 'all')
# 
# =============================================================================


#self test question:
#Do you know why the prediction for middle-man for question E 
#is not aligned with the thick line of the boxplot? 
#(hint: think about what the different lines of a boxplot mean).

#-------------------Answer:
    
#Middle-man prediction time = 240
# Thick line box plot = 270
#These do not align because the thick line of the box plot is the median (the middle element)
#In this case the middle element of 'All combinations'. This element has value 270 and not 240
# 240 is just a different element of 'All comninations' (namely; result of middle+middle+middle)

#1.C
#Self-check: What would be the task analysis, calculation, and approximation for this task?
#Analysis:
#the implementation of model/theory. 
#The model describes where a cognitive process takes place and what this process entails



#Implement a model that can make fastman, middleman, and slowman
#predictions similar to example 2.

def example3(completeness = 'extremes', s2_delay=0):
    
    if completeness == 'extremes':
        
        # 1. everything fast
        #define two stimuli: tp1_f = fast perceptual processing time of stimuli 1, 
        #tp2_f = fast perceptual processing time of stimuli 2
        tp_f=  t_p[0]
        
        #defining two time for two coginitive processes: tcc_f = fast cognitive processing time of 
        #comparing stimuli, tcm_f = fast cognitive processing time of preparing motor command
        tc_f = t_c[0]
        tm_f = t_m[0]
        time_f = max(tp_f, s2_delay) + tp_f + tc_f + tc_f + tm_f

        # 2. everything middle
        tp_m =  t_p[1]
        tc_m = t_c[1] 
        tm_m = t_m[1]
        time_m = max(tp_m, s2_delay) + tp_m + tc_m + tc_m + tm_m
        
        # 3. everything slow
        tp_s =  t_p[2]
        tc_s = t_c[2] 
        tm_s = t_m[2]
        time_s = max(tp_s, s2_delay) + tp_s + tc_s + tc_s + tm_s
        
        #fast perception, middle cognitive, slow motor time
        B_time = max(tp_f, s2_delay) + tp_f + tc_m + tc_m + tm_s
        
        
        
           
        
        print(f'Fastman time: {time_f} ms, Middleman time: {time_m} ms, Slowman time: {time_s} ms')
        print()
        print(f'1B time: {B_time} ms')
        print()
        
        return time_f, time_m, time_s  
        
    if completeness == "all":
        for p_index, p in enumerate(t_p):
            for c_index, c in enumerate(t_c):
                for m_index, m in enumerate(t_m):
                  print(f"t_p = {p} ({labels[p_index]}) + t_c = {c} ({labels[c_index]}) + t_m = {m}")
                  
                  time = max(p, s2_delay) + p + c + c + m
                  print(f"Time = {time}\n")
        
                
        

#example3(completeness = 'extremes', s2_delay = 0) # EXAMPLE 3

# EXAMPLE 4 is just a modified example 3:
    
def example4():
    for s2_delay in [40, 80, 110, 150, 210]:
        print(f">> For stimulus 2 delay of {s2_delay}:")
        example3(completeness = 'extremes', s2_delay = s2_delay) 

example4()

def example5(completeness = "all", s2_delay=0):
    e_orig = 0.01
    e_list = []
    time_list = []
    if completeness == "all":
        for p_index, p in enumerate(t_p):
            for c_index, c in enumerate(t_c):
                for m_index, m in enumerate(t_m):
                    print(f"t_p = {p} ({labels[p_index]}), t_c = {c} ({labels[c_index]}), t_m = {m} ({labels[m_index]})")
                  
                    time = max(p, s2_delay) + p + c + c + m
                    print(f"Time = {time}")
                    
                    e_update = e_orig * multiplier[p_index]**2 * multiplier[c_index]**2 * multiplier[m_index]
                    print(f"error {e_update}\n")
                    
                    e_list.append(e_update)
                    time_list.append(time)
                    

        #day one, the age and speed of 13 cars:
        x = np.array(time_list)
        y = np.array(e_list)
        plt.scatter(x, y)
        plt.xlabel("total time (ms)")
        plt.ylabel("error")
        #day two, the age and speed of 15 cars:
        #x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
        #y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
        #plt.scatter(x, y)
        
        plt.show()

#example5()




