def selection_sort(num_list):
    num_list_len = len(num_list)
    for i in range(num_list_len):
        minIndex = i
        for j in range(i+1, num_list_len):
            if num_list[j] < num_list[minIndex]:
                minIndex = j
        
        minValue = num_list[minIndex]
        num_list[minIndex] = num_list[i]
        num_list[i] = minValue
    return num_list


if  __name__ == '__main__':
    num_list = [9, 4, 11, 2, 7]
    print('選擇排序前:{}'.format(num_list))
    print('選擇排序後:{}'.format(selection_sort(num_list)))
