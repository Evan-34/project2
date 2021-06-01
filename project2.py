def predict(input_string, index, predict_history, result):
    if index == 0:
        history = 0
        if predict_history[history] == 0 or predict_history[history] == 1:
            pred = 0
        else:
            pred = 1
        if input_string[index] == pred:
            print('correct')
            result[index] = 1
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1
        else:
            print('incorrect')
            result[index] = 0
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1
    elif index == 1:
        history = input_string[0]
        if predict_history[history] == 0 or predict_history[history] == 1:
            pred = 0
        else:
            pred = 1
        if input_string[index] == pred:
            print('correct')
            result[index] = 1
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1
        else:
            print('incorrect')
            result[index] = 0
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1
    else:
        history = input_string[index-2]*2 + input_string[index-1]*1
        if predict_history[history] == 0 or predict_history[history] == 1:
            pred = 0
        else:
            pred = 1
        if input_string[index] == pred:
            print('correct')
            result[index] = 1
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1

        else:
            result[index] = 0
            print('incorrect')
            if input_string[index] == 1:
                if predict_history[history] < 3:
                    predict_history[history] = predict_history[history] + 1
            else:
                if predict_history[history] > 0:
                    predict_history[history] = predict_history[history] - 1

    return history
def decimalToBinary(n, size):
    dec2binary = bin(int(n)).replace("0b", "")
    while (len(dec2binary) < size): dec2binary = '0' + dec2binary
    return dec2binary
def main():
    with open("project2.txt", "r") as myfile:
        input_result = myfile.readlines()
        input_result = ''.join(input_result)
        print(input_result)
    length = len(input_result)
    input_string = [0 for x in range(length)]
    result = [0 for x in range(length)]
    history_result = [0 for x in range(5)]
    for i in range(length):
        if input_result[i] == 'T':
            input_string[i] = 1
        else:
            input_string[i] = 0
    predict_history = [0, 0, 0, 0]
    for index in range(length):
        history = predict(input_string, index, predict_history, result)
        for h in range(4):
            if predict_history[h] == 0:
                history_result[h+1] = 'SN'
            elif predict_history[h] == 1:
                history_result[h+1] = 'WN'
            elif predict_history[h] == 2:
                history_result[h+1] = 'WT'
            else:
                history_result[h+1] = 'ST'
        history_result[0] = decimalToBinary(history, 2)
        print(history_result)
    for i in range(length):
        if result[i] == 1:
            result[i] = 'T'
        else:
            result[i] = 'N'
    print(result)
main()
