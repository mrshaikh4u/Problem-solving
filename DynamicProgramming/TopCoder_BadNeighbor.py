from typing import List
from functools import lru_cache


class BadNeighbors:
    idx_tracker = []
    donations = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
                 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    
    @lru_cache(maxsize= 10**6)
    def calculateDonationRec(self,idx:int,)->int:
        # print(idx)
        if idx < 0 :
            maxDonation = 0
        else:
            take_current = BadNeighbors.donations[idx] + self.calculateDonationRec(idx-2)
            dontTake_current = self.calculateDonationRec(idx-1)
            if take_current > dontTake_current and len(BadNeighbors.donations)>2:
                if idx == len(BadNeighbors.donations)-1 and 0 in BadNeighbors.idx_tracker:
                    take_current-= BadNeighbors.donations[0] if BadNeighbors.donations[idx] > BadNeighbors.donations[0] else BadNeighbors.donations[idx]
                BadNeighbors.idx_tracker.append(idx)
            maxDonation = max(dontTake_current,take_current)
            # print('took: ',maxDonation )
        return maxDonation


obj = BadNeighbors()
print(obj.calculateDonationRec(len(BadNeighbors.donations)-1))
