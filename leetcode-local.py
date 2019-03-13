# class Solution:
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
def findMedianSortedArrays( nums1, nums2):
    nums1 = nums1[::-1]
    nums2 = nums2[::-1]
    Len1 = len(nums1)
    Len2 = len(nums2)
    if Len1>Len2:
        nums1,nums2 = nums2,nums1
        Len1,Len2 = Len2,Len1
    Len = Len1 + Len2
    odd = Len%2 #odd
    i1 = 0
    j1 = Len1-1
    # pre process over
    if Len1==0:
        if odd==1:
            return nums2[Len//2]
        else:
            return (nums2[Len//2-1]+nums2[Len//2])/2
    # there is no posibility that double empty
    while i1 <= j1: 
        L1 = (i1 + j1)//2 # exact or before index
        L2 = Len//2 - L1
        if L2 >= Len2:
            if i1 != L1:
                i1 = L1
            else:
                i1 = L1+1
            continue
        L1end = nums1[L1-1]
        R1start = nums1[L1]
        L2end = nums2[L2-1]  # ?
        R2start = nums2[L2]
        if L1end >= R2start and L2end >= R1start:
                if odd == 1:
                    return max(R1start, R2start)
                else:
                    return (min(L1end, L2end)+max(R1start, R2start))/2
        elif L1end >= R2start and L2end < R1start:
                i1 = L1
        elif L1end < R2start and L2end >= R1start:
                j1 = L1
        else:
            print('impossible')

    if Len1 <= Len/2:
            L2 = Len//2 - Len1
            if nums1[-1]>=nums2[L2]:#考虑不全
                if odd == 1:
                    return nums2[L2]
                else:
                    return (max(nums1[-1],nums2[L2-1])+nums2[L2])/2
            if nums1[0]<=nums2[Len2-L2-1]:
                if odd == 1:
                    return nums2[Len2-L2-1]
                else:   
                    if L2==0:
                        tmp = nums2[-1]
                    else:   
                        tmp = nums2[Len2-L2]
                    # try:
                    #     tmp = nums2[Len2-L2]
                    # except:
                    #     pass
                    # finally:
                    #     tmp = nums2[-1]
                return (min(nums1[0],tmp)+nums2[Len2-L2-1])/2    
 
        # if max(R1start,R2start)<=min(L1end,L2end):
        #     if flag:
        #         return max(R1start,R2start)
        #     else:
        #         return (max(R1start,R2start)+min(L1end,L2end))/2
        # print("i1:")
        # print(i1)
        # print("j1")
        # print(j1)
                
nums1 = [3]
nums2 = [1,2,4]
med = findMedianSortedArrays(nums1,nums2)
print(med)
