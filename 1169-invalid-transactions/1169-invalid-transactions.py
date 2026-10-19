class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]: 
        invalid = set()
        history = defaultdict(list)
        for idx, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                invalid.add(idx)
            if name in history:
                history[name].append([time, idx, city])
                i = len(history[name]) - 2                
                while i >= 0: 
                    if abs(int(time) - int(history[name][i][0])) <= 60 and city != history[name][i][2]:
                        invalid.add(idx)
                        invalid.add(history[name][i][1])
                    i -= 1
            else:
                history[name].append([time, idx, city])
        return [transactions[i] for i in range(len(transactions)) if i in invalid]