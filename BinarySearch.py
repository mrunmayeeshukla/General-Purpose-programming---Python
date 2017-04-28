# linear search

def bnarySearch(data,n):
    start = 0
    end = len(data)
    found = False
    print("here")
    while end-start >1:
        mid = (start + end) // 2
        print(start,end)
        print(mid)
        if n== data[mid]:
            return mid
            break
        elif n < data[mid]:
            start=0
            end = mid
        elif data[mid] < n:
            start = mid
            end= len(data)

    if end-start<=1:
        data.append(n)
        return False

def main():
    arr=  [1,2,4,5,6,7,9,10,13,34,56]
    n= 56
    find = bnarySearch(arr,n)
    if find!=False:
        print("element is found at location : ",bnarySearch(arr,n) )
    else:
        print("Element was not present in array and has been inserted at the end")

main()