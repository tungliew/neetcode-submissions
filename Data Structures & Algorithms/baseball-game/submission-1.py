class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op=="+":
                temp1 = record[-1]
                temp2 = record[-2]
                record.append(temp1+temp2)
            elif op=="C":
                record.pop()
            elif op=="D":
                temp = record[-1]*2
                record.append(temp)
            else :
                record.append(int(op))
        
        return sum(record)
        