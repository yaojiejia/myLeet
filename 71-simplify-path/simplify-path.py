class Solution:
    def simplifyPath(self, path: str) -> str:
        dedupe_slash_path = ""

        consecutive_count = 0
        for char in path:
            if char == "/":
                consecutive_count += 1 
                if consecutive_count > 1:
                    continue
                dedupe_slash_path += char
            else:
                dedupe_slash_path += char
                consecutive_count = 0
        elements = list(filter(None, dedupe_slash_path.split("/")))
        stack = []

        for element in elements:
            if stack and element == "..":
                stack.pop()
            elif not stack and element == "..":
                continue
            elif element == ".":
                continue
            else:
                stack.append(element)
        result = "/"
        if not stack:
            return "/"
        for s in stack:
            result += s
            result += "/"
        result = result[:len(result)-1]
        return result