def mergeSort(arr, start, end):
  center = 0
  if(start < end):
    center = (start + end) // 2
    mergeSort(arr, start, center)
    mergeSort(arr, center+1, end)
  else: return
  
  temp = []
  i, j = start, center+1

  # add small item to temp arr 
  while(i<=center and j<=end):
    if(arr[i] <= arr[j]):
      temp.append(arr[i])
      i+=1
    else:
      temp.append(arr[j])
      j+=1
  
  # add remain item
  while(i<=center):
    temp.append(arr[i])
    i+=1
  while(j<=end):
    temp.append(arr[j])
    j+=1
  
  # apply to original
  i=start
  for item in temp:
    arr[i] = item
    i+=1
    # logwrite(len(arr), start, end, f"(apply_to_original)now position: {i}\ntemp_length: {len(temp)}")
  return arr
def logwrite(length, start, end, content_str):
  print(f"length: {length}, start: {start}, end {end}, \ncontent:\n{content_str}")
  
a = [3,1,8,6,10,2,4,9,7,5]
b= [3,6,2,4,1,8,7,5]
sortList = mergeSort(b,0,7)

print(sortList)
