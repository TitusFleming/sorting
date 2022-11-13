# bubble sort

unsorted_list = [10, 7, -1, 9, 2, 12, 192, 1, -7]

def bubble_sort(list_to_sort):
	n = len(list_to_sort)
 
 	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if list_to_sort[j] > list_to_sort[j+1]:
				list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
	print(list_to_sort)



if __name__ == "__main__":
	bubble_sort(unsorted_list)