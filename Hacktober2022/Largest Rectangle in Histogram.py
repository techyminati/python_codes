class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        r=next_smallest_element_from_right(heights)
        l=next_smallest_element_from_left(heights)
        
        #now we'll find maximum area
        m=0
        for i in range(len(heights)): 
            m=max((r[i]-l[i]-1)*heights[i],m) #(r[i]-l[i]-1)*heights[i] = (distance covered * width of those bars)
        return m
        
        
#we are doing here as function named next_smallest_element_from_right
def next_smallest_element_from_right(heights):
    st=[]
    ans=[0]*len(heights)
    for i in range(len(heights)-1,-1,-1):
        while len(st)!=0 and st[-1][0]>=heights[i]:
            st.pop()
        if len(st)==0:
            ans[i]=len(heights)
        else:
            ans[i]=st[-1][-1]
        st.append([heights[i],i])
    return ans


#we are doing here as function named next_smallest_element_from_left
def next_smallest_element_from_left(heights):
    st=[]
    ans=[0]*len(heights)
    for i in range(len(heights)):
        while len(st)!=0 and st[-1][0]>=heights[i]:
            st.pop()
        if len(st)==0:
            ans[i]=-1
        else:
            ans[i]=st[-1][-1]
        st.append([heights[i],i])
    return ans
