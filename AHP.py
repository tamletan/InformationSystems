import numpy as np

RI = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.40, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]

def cal_weight(matrix):
    rs = np.sum(matrix, axis=1, dtype=float)
    total = np.sum(rs)
    return rs / total

def fin_weight(inp):
    loop = True
    count = 0
    while loop:
        inp = inp.dot(inp)
        w = cal_weight(inp)
        if count > 0:
            k = abs(w-w1)
            if not any(k > 0.005):
            	loop = False
        count += 1
        w1 = w
    return w1

def determine(inp, fin_weight):
    total_weight = inp.dot(fin_weight)
    consistent = total_weight / fin_weight
    n = consistent.shape[0]
    lamda_max = np.sum(consistent) / n
    CI = (lamda_max - n) / (n - 1)
    try:
        CR = CI / RI[n]
    except Exception as e:
        print(str(e))
    return lamda_max, CI, CR

if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)
    # input = np.array([[1/1, 1/2, 3/1],
    #                   [2/1, 1/1, 4/1],
    #                   [1/3, 1/4, 1/1]])

    input = np.array([[1/1, 5/1, 2/1, 4/1],
                      [1/5, 1/1, 1/2, 1/2],
                      [1/2, 2/1, 1/1, 2/1],
                      [1/4, 2/1, 1/2, 1/1]])

    fw = fin_weight(input)
    print("BỘ TRỌNG SỐ LÀ: ", fw)
    lamda_max, ci, cr = determine(input, fw)
    print("Lambda = {0:.4f}".format(lamda_max))
    print("CI = {0:.4f}".format(ci))
    print("CR = {0:.4f}".format(cr))
    if cr < 0.1:
        print("=> CHẤP NHẬN BỘ TRỌNG SỐ")
    else:
        print("=> KHÔNG CHẤP NHẬN BỘ TRỌNG SỐ")