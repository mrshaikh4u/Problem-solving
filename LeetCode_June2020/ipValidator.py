import re
class Solution:
    def isIPV6(self,IP:str)->bool:
        if not IP or len(IP.strip())==0:
            return False
        splitted = IP.split(':')
        if len(splitted)!=8:
            return False
        ipv6Pattern = r"^[0-9a-fA-F]{1,4}$"
        for string in splitted:
            if re.search(ipv6Pattern,string) is None:
                return False
        return True


    def validIPAddress(self, IP: str) -> str:
        if not IP or len(IP.strip())==0:
            return "Neither"
        ipv4pattern = r"^([1][0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[1-9])\.([1][0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[1-9])\.([11][0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[1-9])\.([11][0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[1-9])$"
        if re.search(ipv4pattern,IP) is not None:
            return "IPv4"
        elif self.isIPV6(IP):
            return "IPv6"
        else:
            return "Neither"


obj = Solution()
ip = "172.16.254.1"
ip2 = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
ip3 = "256.256.256.256"
# print(obj.validIPAddress(ip))
print(obj.validIPAddress(ip2))
# print(obj.validIPAddress(ip3))


