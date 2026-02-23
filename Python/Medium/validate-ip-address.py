# Name: validate-ip-address
# URL: https://leetcode.com/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        queryIP_v4 = queryIP.split('.')
        queryIP_v6 = queryIP.split(':')

        if len(queryIP_v4) == 4:
            for octet in queryIP_v4:
                if len(octet) > 1 and octet[0] == "0":
                    return "Neither"
                try:
                    octet = int(octet)
                    if not 0 <= int(octet) <= 255:
                        return "Neither"
                except ValueError:
                    return "Neither"
            return "IPv4"

        if len(queryIP_v6) == 8:
            for sec in queryIP_v6:
                if not len(sec):
                    return "Neither"
                for c in sec.upper():
                    if c not in "0123456789ABCDEF":
                        return "Neither"
                    if len(sec) > 4:
                        return "Neither"
            return "IPv6"

        return "Neither"

        

print(
    Solution.validIPAddress(
        None,
        "192.168.0.0"
    )
)
