import pandas as pd
import matplotlib.pyplot as plt
import math

#loading data
path_cat_label = '/Users/ivar/Documents/GitHub/cognitive-modelling/ass.2/data/CategoryLabels.txt'
path_cat_vector = '/Users/ivar/Documents/GitHub/cognitive-modelling/ass.2/data/CategoryVectors.txt'
path_n_response_1 = '/Users/ivar/Documents/GitHub/cognitive-modelling/ass.2/data/NeuralResponses_S1.txt'

cat_label = pd.read_csv(path_cat_label)
cat_vector = pd.read_csv(path_cat_vector)
n_response_1 = pd.read_csv(path_n_response_1)

#creating cat. var dataframe
cat_var = cat_vector.rename(columns={'Var1': "animate", 'Var2': "inanim", 'Var3':"human", 'Var4': "nonhumani", 
                                     'Var5': "body", 'Var6': "face", 'Var7': "natObj", 'Var8': "artiObj",
                                     'Var9': "rand24", 'Var10': "rand48", 'Var11': "other48", 'Var12': "monkeyape"
                                     })                                   

#calculate everage value for every voxel
n_response_1['avg'] = n_response_1.mean(axis=1)
print(n_response_1)

#response_animate= n_response_1.iloc[:44]
#response_inanimate = n_response_1.iloc[44:]

#separate between animate and inanimate responses
avg_response_animate = n_response_1.iloc[:44]['avg']
avg_response_inanimate = n_response_1.iloc[44:]['avg']
print(avg_response_animate)

#get mean of average responses
mean_response_animate = avg_response_animate.mean()
mean_response_inanimate = avg_response_inanimate.mean()

#get std of average responses
std_response_animate = avg_response_animate.std()
std_response_inanimate = avg_response_inanimate.std()

std = pd.DataFrame({'animate std': [std_response_animate], 
                        'inanimate std': [std_response_inanimate]})
print(std)
print(f'Mean ani: {mean_response_animate}, std ani: {std_response_animate}')
print(f"Mean inani: {mean_response_inanimate}, std ani: {std_response_inanimate}")

#create plot
response_plot = pd.DataFrame({'Mean':[mean_response_animate, mean_response_inanimate], 
                        'object':['animate', 'inanimate']})

#ax = response_plot.plot.bar(x='object', y='Mean', yerr=std, rot=0, capsize=5)
#ax.set_title("Average response amplitude")
#ax.set_ylabel("Response amplitude")

#1. Engineering 2.

#reset indexes
reset_response_animate = avg_response_animate.reset_index(drop=True)
reset_response_inanimate = avg_response_inanimate.reset_index(drop=True)

#subtract voxels
sub = reset_response_animate.sub(reset_response_inanimate)
sub_mean = sub.mean()
sub_std = sub.std()
print(f'sub: \n{sub}')
print(f'sub mean: \n{sub_mean}\n sub std: \n{sub_std}\n')

#t-test function
def t_test(m,s,n):
    t_val = m/(s/math.sqrt(n))
    print(f't value: {t_val}')
    return t_val

#N = number of observation per category = 100
t_test(sub_mean,sub_std, 100)

#filling in in online source: degrees of freedom = 100-1 = 99, significance level = 0.98
#T-value (one-tailed) = +/- 0.025132
#T-value (two-tailed) = -2.0812






