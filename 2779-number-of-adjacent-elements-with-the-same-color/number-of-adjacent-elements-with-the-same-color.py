class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0] * len(queries)
        res = []
        arr = [0] * n
        temp = 0

        for i in range(len(queries)):
            if queries[i][0] > 0 and queries[i][0] < n-1:
                if (arr[queries[i][0]-1] == arr[queries[i][0]]) and (arr[queries[i][0]-1] != 0) and (arr[queries[i][0]] != 0):
                    temp -= 1
                if (arr[queries[i][0]+1] == arr[queries[i][0]]) and (arr[queries[i][0]+1] != 0) and (arr[queries[i][0]] != 0):
                    temp -= 1
            elif queries[i][0] == 0:
                if (arr[queries[i][0]+1] == arr[queries[i][0]]) and (arr[queries[i][0]+1] != 0) and (arr[queries[i][0]] != 0):
                    temp -= 1
            else:
                if (arr[queries[i][0]-1] == arr[queries[i][0]]) and (arr[queries[i][0]-1] != 0) and (arr[queries[i][0]] != 0):
                    temp -= 1

            arr[queries[i][0]] = queries[i][1]

            if queries[i][0] > 0 and queries[i][0] < n-1:
                if (arr[queries[i][0]-1] == arr[queries[i][0]]) and (arr[queries[i][0]-1] != 0) and (arr[queries[i][0]] != 0):
                    temp += 1
                if (arr[queries[i][0]+1] == arr[queries[i][0]]) and (arr[queries[i][0]+1] != 0) and (arr[queries[i][0]] != 0):
                    temp += 1
            elif queries[i][0] == 0:
                if (arr[queries[i][0]+1] == arr[queries[i][0]]) and (arr[queries[i][0]+1] != 0) and (arr[queries[i][0]] != 0):
                    temp += 1
            else:
                if (arr[queries[i][0]-1] == arr[queries[i][0]]) and (arr[queries[i][0]-1] != 0) and (arr[queries[i][0]] != 0):
                    temp += 1
            res.append(temp)
        return res