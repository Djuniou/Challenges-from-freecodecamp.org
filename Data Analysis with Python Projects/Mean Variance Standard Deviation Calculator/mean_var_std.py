import numpy as np

def calculate(numbers):
    calculations = {'mean':[],
        'variance':[],
        'standard deviation':[],
        'max':[],
        'min':[],
        'sum':[]            
        }
    if (len(numbers)<9):
        raise ValueError ("List must contain nine numbers.")
    else:
        array = np.array(numbers).reshape(3,3)
        calculations.update({
            'mean':[ list(np.mean(array,axis=0)), list(np.mean(array,axis=1)), np.mean(np.array(numbers)) ],
            'variance': [ list(np.var(array,axis=0)), list(np.var(array,axis=1)), np.var(np.array(numbers)) ],
            'standard deviation': [ list(np.std(array,axis=0)), list(np.std(array,axis=1)), np.std(np.array(numbers)) ], 
            'max': [ list(np.max(array,axis=0)), list(np.max(array,axis=1)), np.max(np.array(numbers)) ],
            'min': [ list(np.min(array,axis=0)), list(np.min(array,axis=1)), np.min(np.array(numbers)) ],
            'sum': [ list(np.sum(array,axis=0)), list(np.sum(array,axis=1)), np.sum(np.array(numbers)) ],   
            })
    
    return calculations
