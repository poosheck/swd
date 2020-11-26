import random
import numpy as np


def randomize_intervals():
    intervals = []
    for i in range(10):
        a = round(random.random(), 2)
        b = round(random.random(), 2)
        while a == b:
            b = round(random.random(), 2)
        if a < b:
            intervals.append([a, b, i])
        else:
            intervals.append([b, a, i])
    return intervals


def probability_3(intervals):
    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        print(i)
        for j in range(len(intervals)):
            if intervals[j][1] < intervals[i][0]:
                P[i][j] = 1
            elif intervals[j][0] > intervals[i][1]:
                P[i][j] = 0
            else:
                P[i][j] = (intervals[i][1] - intervals[j][0]) \
                          / (intervals[i][1] - intervals[i][0] + intervals[j][1] - intervals[j][0])

    return (P)


def probability_4(intervals):
    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        for j in range(len(intervals)):
            t = (intervals[j][1] - intervals[i][0]) \
                / ((intervals[i][1] - intervals[i][0]) + (intervals[j][1] - intervals[j][0]))
            if t > 0:
                t = 1 - t
            else:
                t = 1
            if t > 0:
                P[i][j] = t
            else:
                P[i][j] = 0

    return (P)


def probability_5(intervals):
    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if intervals[j][1] <= intervals[i][0]:
                P[i][j] = 1
            elif intervals[j][0] >= intervals[i][1]:
                P[i][j] = 0
            else:
                P[i][j] = ((intervals[i][1] - intervals[j][0]) ** 2) \
                          / (((intervals[i][1] - intervals[j][0]) ** 2) +
                             ((intervals[j][1] - intervals[i][0]) ** 2))

    return (P)


def probability_6(intervals):
    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if intervals[i][0] <= intervals[i][1] <= intervals[j][0] <= intervals[j][1]:
                l = 0
            elif intervals[i][0] <= intervals[j][0] <= intervals[i][1] <= intervals[j][1]:
                l = intervals[i][1] - intervals[j][0]
            elif intervals[i][0] <= intervals[j][0] <= intervals[j][1] <= intervals[i][1]:
                l = intervals[j][1] - intervals[j][0]
            elif intervals[j][0] <= intervals[j][1] <= intervals[i][0] <= intervals[i][1]:
                l = 0
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1] <= intervals[i][1]:
                l = intervals[j][1] - intervals[i][0]
            elif intervals[j][0] <= intervals[i][0] <= intervals[i][1] <= intervals[j][1]:
                l = intervals[i][1] - intervals[i][0]
            else:
                exit(1)

            P[i][j] = 0.5 * (1 + (
                    ((intervals[i][1] - intervals[j][1]) + (intervals[i][0] - intervals[j][0])) /
                    (abs(intervals[i][1] - intervals[j][1]) + abs(intervals[i][0] - intervals[j][0]) + l)
            ))

    return (P)


def probability_7(intervals):
    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if intervals[j][1] <= intervals[i][0]:
                P[i][j] = 1
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1] <= intervals[i][1]:
                P[i][j] = 1 - (
                        ((intervals[j][0] - intervals[i][1]) ** 2)
                        / (2 * (intervals[i][1] - intervals[i][0]) * (intervals[j][1] - intervals[j][0]))
                )
            elif intervals[j][0] <= intervals[i][0] <= intervals[i][1] <= intervals[j][1]:
                P[i][j] = 0.5 * (
                        (intervals[i][0] + intervals[i][1] - 2 * intervals[j][0])
                        / (intervals[j][1] - intervals[j][0])
                )
            elif intervals[i][0] <= intervals[j][0] <= intervals[j][1] <= intervals[i][1]:
                P[i][j] = 0.5 * (
                        (2 * intervals[i][1] - intervals[j][0] - intervals[j][1]) / (intervals[j][1] - intervals[j][0])
                )
            elif intervals[i][0] <= intervals[j][0] <= intervals[i][1] <= intervals[j][1]:
                P[i][j] = (intervals[i][1] - intervals[j][0]) ** 2 \
                          / (2 * (intervals[i][1] - intervals[i][0]) * (intervals[j][1] - intervals[j][0]))
            else:
                P[i][j] = 0

    return (P)


def priority_1(intervals):
    eps = 0.001

    P = np.zeros([10, 10])

    for i in range(len(intervals)):
        print(i)
        for j in range(len(intervals)):
            if intervals[j][1] < intervals[i][0]:
                P[i][j] = 1
            elif intervals[j][0] > intervals[i][1]:
                P[i][j] = 0
            else:
                P[i][j] = 0.5 + (intervals[i][1] - intervals[j][0] + intervals[i][0] - intervals[j][1]) \
                          / (2 * (intervals[i][1] - intervals[i][0] + intervals[j][1] - intervals[j][0]) + eps)

    return (P)


def sort_by_min(intervals):
    ranking = []
    r = sorted(intervals, key=lambda tup: tup[0], reverse=True)
    print("Sorted by minimum interval value")
    for i in r:
        print("Index: {} ... value {}".format(i[2], i[0]))
        ranking.append(i[2])
    return(ranking)


def sort_by_max(intervals):
    ranking = []
    r = sorted(intervals, key=lambda tup: tup[1], reverse=True)
    print("Sorted by maximum interval value")
    for i in r:
        print("Index: {} ... value {}".format(i[2], i[1]))
        ranking.append(i[2])
    return(ranking)


def sort_by_ave(intervals):
    ranking = []
    r = sorted(intervals, key=lambda tup: ((tup[1] + tup[0]) / 2), reverse=True)
    print("Sorted by average interval value")
    for i in r:
        print("Index: {} ... value {}".format(i[2], ((i[1] + i[0]) / 2)))
        ranking.append(i[2])
    return(ranking)


def sort_by_sum(P, intervals):
    ranking = []
    x = 0
    for i in P[:]:
        intervals[x].append(sum(i))
        x += 1
    r = sorted(intervals, key=lambda tup: tup[3], reverse=True)
    print("Sorted by sum of P column")
    for i in r:
        print("Index: {} ... value {}".format(i[2], i[3]))
        ranking.append(i[2])
    return(ranking)

def RW_correlation(rankings):
    RW = np.zeros([len(rankings),len(rankings)])
    N = len(rankings)
    for i in range(len(rankings)):
        for j in range(len(rankings)):
            RW[i][j] = 1 - ((6 * sum([((x - y) ** 2) * ((N - x + 1) + (N - y - 1)) for x, y in zip(rankings[i], rankings[j])]))
                                / (N ** 4 + N ** 3 - N ** 2 - N))

    return(RW)

def WS_correlation(rankings):
    WS = np.zeros([len(rankings), len(rankings)])
    N = len(rankings)
    for i in range(len(rankings)):
        for j in range(len(rankings)):
            WS[i][j] = 1 - (sum([(2 ** ((-1) * x) * ((abs(x - y)) / (max([abs(x-1), abs(x-N)]))))  for x, y in zip(rankings[i], rankings[j])]))

    return(WS)

def main():
    RW = []
    WS = []
    for i in range(3):
        rankings = []
        intervals = randomize_intervals()
        print(intervals)
        P2 = probability_3(intervals)
        P3 = probability_4(intervals)
        P4 = probability_5(intervals)
        P5 = probability_6(intervals)
        P6 = probability_7(intervals)
        P1 = priority_1(intervals)

        rankings.append(sort_by_min(intervals))
        rankings.append(sort_by_max(intervals))
        rankings.append(sort_by_ave(intervals))
        rankings.append(sort_by_sum(P2, intervals))
        rankings.append(sort_by_sum(P3, intervals))
        rankings.append(sort_by_sum(P4, intervals))
        rankings.append(sort_by_sum(P5, intervals))
        rankings.append(sort_by_sum(P6, intervals))
        rankings.append(sort_by_sum(P1, intervals))

        RW.append(RW_correlation(rankings))
        print(RW[i])
        WS.append(WS_correlation(rankings))
        print(WS[i])

    RW_mean = np.mean(RW, axis=0)
    WS_mean = np.mean(WS, axis=0)

    print(np.array(RW_mean))
    print(np.array(WS_mean))

if __name__ == '__main__':
    main()
