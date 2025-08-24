class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, loss = [],[]
        for w,l in matches:
            win.append(w)
            loss.append(l)
        win_cnt = Counter(win)
        loss_cnt = Counter(loss)

        res1 = []
        for player, wins in win_cnt.items():
            if player not in loss_cnt:
                res1.append(player)
        res2 = []
        for player, losses in loss_cnt.items():
            if losses == 1:
                res2.append(player)
        res1.sort()
        res2.sort()
        return [res1,res2]
