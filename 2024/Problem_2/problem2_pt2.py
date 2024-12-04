
# determine n of safe reports
# safe when both are true
# 1) diff between adjacent levels greater than 0 and less than 4
# 2) all levels increasing or decreasing
import numpy as np

def check_diffs(levels):
    for x in range(1, len(levels)):
        diff = levels[x] - levels[x-1]
        if (abs(diff) < 1) or (abs(diff) > 3):
            return False
    return True


def check_slope(levels):
    diff = list(np.diff(levels))
    if diff.count(0) > 0:
        return False
    else:
        for i in range(1, len(diff)):
            if (diff[i] / diff[i - 1]) < 0:
                return False
    return True

#import broken calibration values from the file
input_file = open("input.txt")
reports = input_file.read().splitlines()

n_safe_reports = 0

for i, report in enumerate(reports):
    print("\nAnalyzing Report {}".format(i + 1))

    safe = False

    # initial check for rule 1 and rule 2
    levels = list(map(int, report.split(' ')))
    rule_one = check_diffs(levels)
    print("Rule 1 Check: {}, {}".format(rule_one, levels))
    rule_two = check_slope(levels)
    print("Rule 2 Check: {}, {}".format(rule_two, levels))

    if rule_one and rule_two:
        safe = True
    else:
        # drop one level and recheck rules
        index = 0
        while not safe:
            rmv = levels.pop(index)
            rule_one = check_diffs(levels)
            print("Rule 1 Check: {}, {}".format(rule_one, levels))
            rule_two = check_slope(levels)
            print("Rule 2 Check: {}, {}".format(rule_two, levels))

            if rule_one and rule_two:
                safe = True
            else:
                levels.insert(index, rmv)
                if index == len(levels) - 1:
                    break
                else:
                    index += 1

    if safe:
        n_safe_reports += 1

    print("SAFE REPORT: {}".format(safe))

print(n_safe_reports)








