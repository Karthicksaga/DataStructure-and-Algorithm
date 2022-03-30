def bubble_sort(array):
    
    #iterate the Main array
    #Iterate the whole pass
    for i in range(len(array)):
        
        for j in range(0,len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                
                array[j],array[j + 1] = array[j + 1],array[j]
                
            print("Inner Loop Executed Succefully {0}".format(j))
            
    return array
array = [441,262,19,519,476,758,359,140]
print(bubble_sort(array))
