import numpy as np

def calculate(list_of_nums):
    if len(list_of_nums) != 9:
        raise ValueError('List must contain nine numbers.')
    stats_dict = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    numpy_array = np.array([[int(x) for x in list_of_nums[i:i+3]] for i in range(0, len(list_of_nums), 3)])
    
    for axis in ([0, 1, None]):
        values = [
            numpy_array.mean(axis=axis), 
            numpy_array.var(axis=axis), 
            numpy_array.std(axis=axis),
            numpy_array.max(axis=axis),
            numpy_array.min(axis=axis),
            numpy_array.sum(axis=axis)
        ]

        for i, key in enumerate(stats_dict):
            if type(values[i]) == np.ndarray:
                values[i] = list(values[i])
            stats_dict[key].append(values[i])
    
    return stats_dict
