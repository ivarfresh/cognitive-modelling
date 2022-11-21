import matplotlib.pyplot as plt

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
# example2(completeness = 'all')
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

def example3_and_4(completeness = 'extremes', s2_delay=0):
    
    if completeness == 'extremes':
        
        # 1. everything fast
        #define two stimuli: tp1_f = fast perceptual processing time of stimuli 1, 
        #tp2_f = fast perceptual processing time of stimuli 2
        tp1_f, tp2_f =  t_p[0], t_p[0]
        
        #defining two time for two coginitive processes: tcc_f = fast cognitive processing time of 
        #comparing stimuli, tcm_f = fast cognitive processing time of preparing motor command
        tcc_f, tcm_f = t_c[0], t_c[0]
        tm_f = t_m[0]
        time_f = max(tp1_f, s2_delay) + tp2_f + tcc_f + tcm_f + tm_f

        # 2. everything middle
        tp1_m, tp2_m =  t_p[1], t_p[1]
        tcc_m, tcm_m = t_c[1], t_c[1] 
        tm_m = t_m[1]
        time_m = max(tp1_m, s2_delay) + tp2_m + tcc_m + tcm_m + tm_m
        
        # 3. everything slow
        tp1_s, tp2_s =  t_p[2], t_p[2]
        tcc_s, tcm_s = t_c[2], t_c[2]
        tm_s = t_m[2]
        time_s = max(tp1_s, s2_delay) + tp2_s + tcc_s + tcm_s + tm_s
        
        #fast perception, middle cognitive, slow motor time
        B_time = max(tp1_f, s2_delay) + tp2_f + tcc_m + tcm_m + tm_s
        
           
        
        print(f'Fastman time: {time_f} ms, Middleman time: {time_m} ms, Slowman time: {time_s} ms')
        print()
        print(f'1B time: {B_time} ms')
        print()
        
        return time_f, time_m, time_s  

example3_and_4(completeness = 'extremes', s2_delay = 0) # EXAMPLE 3

# EXAMPLE 4 is just a modified example 3:
    
for s2_delay in [40, 80, 110, 150, 210]:
    print(f">> For stimulus 2 delay of {s2_delay}:")
    example3_and_4(completeness = 'extremes', s2_delay = s2_delay) 








