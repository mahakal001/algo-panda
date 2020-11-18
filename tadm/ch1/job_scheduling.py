def job_scheduling_1(I, n):
    # Problem: Job Scheduling Problem where each job has the same profit
    # Input: A set I of n intervals on the line.
    # Output: What is the largest subset of mutually non-overlapping intervals that can be selected from I?

    """

    :param I: A set of jobs (start,end) pairs
    :param n: number of jobs
    :return: A set of jobs that maximize the value
    """

    job_intervals = list(I)

    # Sort the list by the end time
    job_intervals.sort(key=lambda x: x[1])
    last_job_finished_time = -1  # since this minimum is not practically possible
    A = []

    for job in job_intervals:
        if job[0] >= last_job_finished_time:
            A.append(job)
            last_job_finished_time = job[1]
    return A


def job_scheduling_2(I, n):
    # Problem: Job Scheduling Problem where each job give different profit but can be completed in unit time
    # Input: A set I of n pairs (deadline, profit) on the line.
    # Output: What is subset of I which can give largest profit

    """

    :param I: A set of jobs (deadline, profit) pairs
    :param n: number of jobs
    :return: A set of jobs that maximize the profit
    """

    jobs = list(I)

    # Sort the list in non-increasing order of profit
    jobs.sort(key=lambda x: x[1], reverse=True)

    # ith bucket has the highest profit for deadline <= i
    # since we have 0 based indexing so we will ignore 0th bucket
    buckets = [0 for i in range(n + 1)]

    for job in jobs:
        deadline = job[0]
        profit = job[1]
        for i in range(deadline, 0, -1):
            if profit > buckets[i]:
                buckets[i] = profit
                break

    return buckets


I = ((1, 3), (2, 3), (3, 5), (4, 6), (5, 7), (3, 9)) #(start, end)
print("The jobs to pick for max return in version 1:", job_scheduling_1(I, len(I)))

I = {(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)} # (deadline, profit)
print("Jobs with following weight can be chosen for max return: ", job_scheduling_2(I, len(I))[1:])
