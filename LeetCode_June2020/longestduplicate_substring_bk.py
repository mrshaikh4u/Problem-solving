from collections import defaultdict

class Solution:


    def getHash(self,string:str)->int:
        result = 0
        i=0
        for ch in reversed(string):
            result+= (ord(ch) - 96) * 10**i
            i+=1
        return result

    def findPattern(self,input:str , pattern_length:int)->tuple:
        hashmap = defaultdict(bool)
        length = len(input)
        for i in range(length-pattern_length+1):
            if hashmap[input[i:i+pattern_length]] is True:
                return True,input[i:i+pattern_length]
            hashmap[input[i:i+pattern_length]] = True
        return False,""



    # def findPattern(self,input:str , pattern_length:int)->tuple:
    #     ws = 0
    #     wh=0
    #     tocheck = defaultdict(list)
    #     for we in range(len(input)):
    #         if we < pattern_length-1:
    #             continue
    #         if wh==0:
    #             wh = self.getHash(input[ws:we+1])
    #         else:
    #             old_val = (wh - ((ord(input[ws])-96) * (10**(pattern_length-1))))
    #             wh = (10 * old_val) + (ord(input[we])-96)
    #             ws+=1
    #         tocheck[wh].append(input[ws:we+1])
    #     for k,v in tocheck.items():
    #         for i in range(1,len(v)):
    #             if v[i]==v[i-1]:
    #                 return True,v[i]
    #     return False,""

    def longestDupSubstring(self, S: str) -> str:
        if not S or len(S)==0:
            return 0
        start = 0
        end = len(S)-1
        result=""
        while start <= end:
            mid = start + (end-start)//2
            isFound , temp =self.findPattern(S,mid)
            if isFound:
                start = mid+1
                result = temp
            else:
                end = mid-1
        return result


obj = Solution()
print(obj.longestDupSubstring("moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkzgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"))
# print(obj.longestDupSubstring("banana"))

