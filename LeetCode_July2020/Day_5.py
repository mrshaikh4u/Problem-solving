class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        smaller , larger = (x,y) if x < y else (y,x)
        bin_smaller = bin(smaller)
        bin_larger = bin(larger)
        lst_smaller = bin_smaller.split('b')[1]
        lst_larger = bin_larger.split('b')[1]
        print(f"{smaller} : {lst_smaller} -> {larger} : {lst_larger}")
        small_len = len(lst_smaller)
        large_len = len(lst_larger)
        cnt=0
        for i in range(len(lst_smaller)):
            if lst_smaller[small_len-1-i] != lst_larger[large_len-1-i]:
                cnt+=1
        for i in range(len(lst_smaller),len(lst_larger)):
            if lst_larger[large_len-1-i]=='1':
                cnt+=1
        return cnt

obj = Solution()
print(obj.hammingDistance(12,12))

