from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = defaultdict(list)

        # Build undirected graph
        q = deque([root])
        while q:
            curr_node = q.popleft()
            if curr_node.left:
                adj_list[curr_node.val].append(curr_node.left.val)
                adj_list[curr_node.left.val].append(curr_node.val)
                q.append(curr_node.left)
            if curr_node.right:
                adj_list[curr_node.val].append(curr_node.right.val)
                adj_list[curr_node.right.val].append(curr_node.val)
                q.append(curr_node.right)

        # BFS from target
        visited = {target.val}
        nq = deque([target.val])
        depth = 0

        while nq:
            if depth == k:
                return list(nq)   # all nodes at distance k
            for _ in range(len(nq)):   # process one level
                node = nq.popleft()
                for nei in adj_list[node]:
                    if nei not in visited:
                        visited.add(nei)
                        nq.append(nei)
            depth += 1

        return []
