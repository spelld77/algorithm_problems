import collections
import re
from typing import List


def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned
             ]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


class MostCommonWord:

    para = "Bob hit a ball, the hit BALL flew far after it was hit"
    ban = ["hit"]

    print(most_common_word(para, ban))
