# determine n of safe reports
# safe when both are true
# 1) diff between adjacent levels greater than 0 and less than 4
# 2) all levels increasing or decreasing
import numpy as np

n_safe_reports = 0

# import broken calibration values from the file
input_file = open("input.txt")
reports = input_file.read().splitlines()

for report in reports:
    violations = 0

    levels = list(map(int, report.split(' ')))
    diff = np.diff(levels)

    for d in diff:
        if (abs(d) < 1) or (abs(d) > 3):
            violations += 1

    if violations == 0:  # next check will fail if diff = 0
        for i in range(0, len(diff) - 1):
            if (diff[i + 1] / diff[i]) < 0:
                violations += 1

    if violations == 0:
        n_safe_reports += 1

print(n_safe_reports)