# ! https://csacademy.com/ieeextreme-practice/task/lemons/
def lemons(N, M, S):
    medium = 1
    count = 0

    while medium <= N:
        medium = (medium + N) // 2
        medium += 1
        count += 1

    return count * S + (N - 1) * M

if __name__ == "__main__":
    input_str = input()
    N, M, S = map(int, input_str.split())
    print(lemons(N, M, S))
