import numpy as np

def get_dot(vec_a,vec_b):
    if len(vec_a) != len(vec_b):
        return ValueError("向量维度数量必须相同")

    sum_dot = 0
    for a,b in zip(vec_a,vec_b):
        sum_dot += a*b

    return sum_dot

def get_norm(vec):
    sum_square = 0  # 平方和
    for v in vec:
        sum_square += v*v
    return np.sqrt(sum_square) #开平方

def cosine_similarity(vec_a,vec_b):
    result  = get_dot(vec_a,vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    return result

if __name__ == '__main__':
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print("ab:",cosine_similarity(vec_a,vec_b))
    print("ac:",cosine_similarity(vec_a,vec_c))
    print("ad:",cosine_similarity(vec_a,vec_d))






