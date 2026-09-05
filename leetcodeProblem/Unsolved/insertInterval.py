class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        newArr = []
        sB = []
        smallest = 0
        biggest = 0
        i = 0
        if len(intervals) == 1 :
            if intervals[0][1] < newInterval[0]  :
                newArr.append(intervals[0])
                newArr.append(newInterval)
                return newArr
            elif intervals[0][0] > newInterval[1] :
                newArr.append(newInterval)
                newArr.append(intervals[0])
                return newArr
            else :
                newArr.append([min(intervals[0][0], newInterval[0]), max(intervals[0][1], newInterval[1])])
                return newArr
            

        while i < len(intervals)-1:
            if intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]  :
                newArr.append(intervals[i])
            else :
                if smallest == 0 :
                    if newInterval[0] >= intervals[i][0] :
                        smallest = intervals[i][0]
                    else :
                        smallest = newInterval[0]

            if intervals[i+1][0] >= newInterval[1] or intervals[i+1][1] > newInterval[1]  :
                if newInterval[1] == intervals [i+1][0] :
                    biggest = intervals[i+1][1]
                    sB = [smallest, biggest]
                    newArr.append(sB)
                    break
                elif intervals[i+1][0] > newInterval[1] :
                    biggest = max(newInterval[1], intervals[i][1])
                    sB = [smallest, biggest]
                    newArr.append(sB)
                    break
                
                elif  intervals[i+1][1] > newInterval[1] :
                    biggest = intervals[i+1][1]
                    sB = [smallest, biggest]
                    newArr.append(sB)
                    break
                       
                
            i += 1
        
        while i < len(intervals) :
            if intervals[i][0] < sB[1] :
                i += 1
            else :
                newArr.append(intervals[i])
                i += 1

        if newArr == [] :
            newArr.append(newInterval)        

        return newArr
    
p = Solution()
print(p.insert([[2,3],[5,7]],[0,6]))
            

                

                