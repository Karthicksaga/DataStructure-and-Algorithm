def insertion_sort(array):
    
    #iterate the full array
    for i in range(1,len(array)):
        
        #take an ith element is an max element
        max_element = array[i]
        l = i
        print(max_element)
        #iterate the array until the previous element
        for k in range(i - 1,-1,-1):
            
            print(array[k])
            #compare the current element is an maximum element
            if array[k] > max_element:
                # if the current element is an maximum element swap it
                array[k],array[l] = max_element,array[k]
                #store the maximum element swapped position element in an array element
                max_element = array[k]
                print(max_element)
            l -= 1
            
    return array
    
array = [441,262,19,519,476,758,359,140]
insertion_sort(array)
                
            
