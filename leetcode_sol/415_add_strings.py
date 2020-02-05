class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1,num2 = num1[::-1],num2[::-1]
        leng = len(num1)-len(num2)
        if leng<0:
            num1 +="0"*(abs(leng))
        else:
            num2+="0"*abs(leng)
        res,carry = [],0
        for d1,d2 in zip(num1,num2):
            carry,digit = divmod(int(d1)+int(d2)+carry,10)
            res.append(str(digit))
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])
