def insertion_sort(num_list):
    num_list_len = len(num_list)
    for i in range(1, num_list_len):
        value = num_list[i]
        j = i - 1
        while j >= 0:
            if value < num_list[j]:
                num_list[j+1] = num_list[j]
                num_list[j] = value;

            j-=1

    return num_list


if __name__ == '__main__':
    num_list = [9, 4, 11, 2, 7]
    print('插入排序前:{}'.format(num_list))
    print('插入排序後:{}'.format(insertion_sort(num_list)))              
                
    
