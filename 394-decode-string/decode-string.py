class Solution(object):
    def decodeString(self, s):
        stack = []
        current_str = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            elif s[i] == '[':
                stack.append(current_str)
                current_str = ""
                i += 1
            elif s[i].isalpha():
                current_str += s[i]
                i += 1
            elif s[i] == ']':
                prev_str = stack.pop()
                repeat_times = stack.pop()
                current_str = prev_str + current_str * repeat_times
                i += 1
        return current_str

