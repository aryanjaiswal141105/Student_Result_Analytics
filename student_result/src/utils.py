# utils.py

def calculate_grade(average):
    """
    Return grade based on average marks.
    """

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def calculate_result(maths, science, english, computer):
    """
    Return Pass if every subject is >=35.
    """

    if maths >= 35 and science >= 35 and english >= 35 and computer >= 35:
        return "Pass"

    return "Fail"