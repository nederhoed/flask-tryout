"""\
Experimental dataset
"""

data = [
    ('If you try too hard, you chase it away.',
    ['love:alone']),
    ('Some great founders realize their philanthropic visions by running a business.',
    ['business:startup', 'life:purpose', 'economy:idealism']),
    ('Do not wait until you have all the answers',
    ['life:purpose', 'personality:doubt', 'education:motivation']),
    ('Money is not going to solve all of your problems; but it’s going to solve all of your money problems.',
    ['business:funding', 'personality:greedy']),
    ('A long lifetime of learning, reading, and creating is going to compound.',
    ['education:motivation', 'finance:invest']),
    ('All millionairs share one habit: They spend less then they earn, consistently',
    ['finance:saving', 'personality:big_spender']),
#    ('', ['', '']),
#    ('', ['', '']),
#    ('', ['', '']),
]

if __name__ == "__main__":
    tag_cat_counter = {}
    for (quote, tags) in data:
        for (cat, tag) in [i.split(':') for i in tags]:
            tag_cat_counter.setdefault(cat, 0)
            tag_cat_counter[cat] += 1

    print(tag_cat_counter)