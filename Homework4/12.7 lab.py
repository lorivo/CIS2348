# Lori Vo 1852113

def fat_burning_heart_rate(age_given):
    result = (220-age_given)*.7
    return result


def get_age():
    age_ = int(input())
    if age_ < 18 or age_ > 75:
        raise ValueError('Invalid age.')
    return age_


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, heart_rate))

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.')
        print()
