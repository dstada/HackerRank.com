import itertools

def minimumAbsoluteDifference(arr):
    combs = list(itertools.combinations(arr, 2))
    # aantal coms is (len(arr)^2 - len(arr))/2
    mins = []
    for i in range(len(combs)):
        mins .append(abs(combs[i][0]-combs[i][1]))
    return min(mins)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)


"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

5
1 -3 71 68 17

Output:
3

"""