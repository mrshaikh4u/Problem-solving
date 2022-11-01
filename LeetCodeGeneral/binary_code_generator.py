def prepareDistinctCodes(self,string:str,k):
        my_list = list(string)
        we = 0
        code = set()
        while we < len(my_list)-k:
            code.add(''.join(my_list[we:we+k]))
            we+=1
        for i in code:
            print(i)
        return len(code)
