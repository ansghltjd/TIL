def solution(word):
    alp = ['A', 'E', 'I', 'O', 'U']
    count = 0
    found = [False]

    def dfs(current):
        nonlocal count
        if found[0]:
            return
        
        if current == word:
            found[0] = True
            return
        
        if len(current) == 5:
            return
        
        for v in alp:
            count += 1
            dfs(current + v)
            if found[0]:
                return

    dfs('')
    return count