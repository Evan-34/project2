def predict(result, index, predict_history):
    if index == 0:


def main():
    with open("project2.txt", "r") as myfile:
        input_result = myfile.readlines()
        input_result = ''.join(input_result)
        print(input_result)
    length = len(input_result)
    result = [0 for x in range(length)]
    for i in range(length):
        if input_result[i] == 'T':
            result[i] = 1
        else:
            result[i] = 0
    print(result)
    predict_history=['SN','SN','SN','SN']
    for index in range(length):
        predict(result, index)
main()