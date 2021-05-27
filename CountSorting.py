def counting_sort(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)
    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        for time in range(count):
            sorted_scores.append(score)
    return sorted_scores


def ascending_counting_sort(unsorted, max_score):
    score_counts = [0] * max_score
    for score in unsorted:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(len(score_counts)):
        count = score_counts[score]

        for time in range(count):
            sorted_scores.append(score)
    return sorted_scores


scores = [37, 89, 41, 65, 91, 53, 98, 98]
print(ascending_counting_sort(scores, 100))
