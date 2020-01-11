

'''
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".'''



def decodeString(self, s: str) -> str:
        stack =[]
        repeats = 0
        dig = set("0123456789")
        for c in s:
            if c==']':
                item = stack.pop()
                curr = []
                while not isinstance(item,int):
                    curr.append(item)
                    item = stack.pop()
                stack+=(curr[::-1]*item)
            elif c in dig:
                repeats = repeats*10 + int(c)
            elif c=='[':
                stack.append(repeats)
                repeats = 0
            else:
                stack.append(c)
        return "".join(stack)
