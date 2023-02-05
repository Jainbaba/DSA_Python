class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        def Merge(nums,l,mid,h):
            cnt = 0
            j = mid+1
            for i in range(l,mid+1):
                while(j <= h and nums[i] > (2 * nums[j])):
                    j += 1
                cnt += (j - (mid+1))
            
            new = []
            le = l
            ri = mid+1
            while(le <= mid and ri <= h):
                if nums[le] <= nums[ri]:
                    new.append(nums[le])
                    le += 1
                else:
                    new.append(nums[ri])
                    ri += 1
            
            while(le <= mid):
                new.append(nums[le])
                le+=1
            while(ri <= h):
                new.append(nums[ri])
                ri+=1
            for i in range(l,h+1):
                nums[i] = new[i-l]
            return cnt
        
        def MergeSort(nums,l,h):
            if l >= h: return 0
            mid = (l+h) // 2
            cnt = MergeSort(nums,l,mid)
            cnt += MergeSort(nums,mid+1,h)
            cnt += Merge(nums,l,mid,h)
            return cnt
        
        return MergeSort(nums,l,h)
        