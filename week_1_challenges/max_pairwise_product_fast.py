def get_largest_num(num1, num2):
    if num1 > num2:
        return num1
    return num2

def sort(num1, num2):
    if num1 > num2:
        return [num1, num2]
    return [num2, num1]

def is_larger(num1, num2):
    if num1 > num2:
        return True
    return False

def get_max_pairwaise_fast(num_list):
    largest_num, second_largest_num = sort(num_list[0], num_list[1])

    if len(num_list) == 2:
        return num_list[0] * num_list[1]

    if len(num_list) < 4:
        largest_num = max(num_list)
        num_list.remove(largest_num)
        second_largest_num = max(num_list)

        return largest_num * second_largest_num
    
    else:
        for i in range(2, len(num_list) - 2, 2):
            value = num_list[i]
            next_value = num_list[i + 1]

            next_pair = sort(value, next_value)

            can_use_first = True

            if is_larger(next_pair[0], largest_num):
                second_largest_num = largest_num
                largest_num = next_pair[0]
                can_use_first = False
                
                if is_larger(next_pair[1], second_largest_num):
                    second_largest_num = next_pair[1]

                    continue
            
            if is_larger(next_pair[1], second_largest_num):
                second_largest_num = next_pair[1]
                can_use_first = False

            if can_use_first and is_larger(next_pair[0],second_largest_num):
                second_largest_num = next_pair[0]

        if len(num_list) % 2 != 0:
            if is_larger(num_list[-1], largest_num):
                second_largest_num = largest_num
                largest_num = num_list[-1]
            
            if is_larger(num_list[-1], second_largest_num):
                second_largest_num = num_list[-1]

        return largest_num * second_largest_num

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(get_max_pairwaise_fast(input_numbers))


    






