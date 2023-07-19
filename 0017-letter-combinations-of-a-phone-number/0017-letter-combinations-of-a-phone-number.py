from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        digit_list=[mapping[d] for d in digits]
        combinations = list(product(*digit_list))
        return([''.join(x) for x in combinations])