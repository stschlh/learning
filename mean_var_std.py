import numpy as np

def calculate(list):
    # 检查输入列表长度是否为9
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # 将列表转换为3x3的numpy数组
    arr = np.array(list).reshape(3, 3)
    
    # 计算各统计量
    mean_axis1 = arr.mean(axis=1).tolist()
    mean_axis0 = arr.mean(axis=0).tolist()
    mean_flattened = arr.mean().tolist()
    
    variance_axis1 = arr.var(axis=1).tolist()
    variance_axis0 = arr.var(axis=0).tolist()
    variance_flattened = arr.var().tolist()
    
    std_dev_axis1 = arr.std(axis=1).tolist()
    std_dev_axis0 = arr.std(axis=0).tolist()
    std_dev_flattened = arr.std().tolist()
    
    max_axis1 = arr.max(axis=1).tolist()
    max_axis0 = arr.max(axis=0).tolist()
    max_flattened = arr.max().tolist()
    
    min_axis1 = arr.min(axis=1).tolist()
    min_axis0 = arr.min(axis=0).tolist()
    min_flattened = arr.min().tolist()
    
    sum_axis1 = arr.sum(axis=1).tolist()
    sum_axis0 = arr.sum(axis=0).tolist()
    sum_flattened = arr.sum().tolist()
    
    # 构建返回的字典
    result = {
        'mean': [mean_axis1, mean_axis0, mean_flattened],
        'variance': [variance_axis1, variance_axis0, variance_flattened],
        'standard deviation': [std_dev_axis1, std_dev_axis0, std_dev_flattened],
        'max': [max_axis1, max_axis0, max_flattened],
        'min': [min_axis1, min_axis0, min_flattened],
        'sum': [sum_axis1, sum_axis0, sum_flattened]
    }
    
    return result

# 示例测试
if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))
