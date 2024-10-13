def find_lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def min_deletions_insertions(s1, s2):
    lcs_len = find_lcs_length(s1, s2)
    deletions = len(s1) - lcs_len
    insertions = len(s2) - lcs_len
    return deletions, insertions

str1 = "heap"
str2 = "pea"
del_count, ins_count = min_deletions_insertions(str1, str2)

print(f"Minimum Deletions = {del_count}, Minimum Insertions = {ins_count}")
