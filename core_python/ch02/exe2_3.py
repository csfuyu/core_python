def switch(m_array, index1, index2):
    tmp = m_array[index1]
    m_array[index1] = m_array[index2]
    m_array[index2] = tmp

def sort(m_array):
    if m_array[1] < m_array[0]:
        switch(m_array,1,0)
    if m_array[2] < m_array[1]:
        switch(m_array, 2,1)
    if m_array[1] < m_array[0]:
        switch(m_array,1,0)
    return m_array

def reverse(m_array):
    size = len(m_array)-1
    index = 0
    while index < size / 2:
        switch(m_array,index,size-index)
        index += 1
    return m_array

m_array = [1,2,3]       
m_array[0] = int(raw_input('Enter the 1st number: '))
m_array[1] = int(raw_input('Enter the 2nd number: '))
m_array[2] = int(raw_input('Enter the 3rd number: '))

print m_array
print sort(m_array)
print reverse(m_array)