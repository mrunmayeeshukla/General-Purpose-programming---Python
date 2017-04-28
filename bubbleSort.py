# bubble sort
def bubbleSort(data):
    for i in range(len(data)-1):
        for i in range(1,len(data)):
            if data[i] <data[i-1]:
                temp= data[i-1]
                data[i-1]=data[i]
                data[i]=temp
    return data

def main():
    arr=  [45,345,67,345,24,13,78,9,67,4,2]

    print("Sorted data is : ")
    print(bubbleSort(arr))

main()