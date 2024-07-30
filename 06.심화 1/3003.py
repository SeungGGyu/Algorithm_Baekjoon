def calculate_diff(_list, input_list):
    
    final=[]

    for i in range(len(_list)):
        final.append(_list[i]-input_list[i])
    
    return final



def main():

    _list = [1,1,2,2,2,8]

    input_list = list(map(int, input().split()))

    result = calculate_diff(_list,input_list)

    for i in result:
        print(i, end=' ')



if __name__ =="__main__":
    main()

