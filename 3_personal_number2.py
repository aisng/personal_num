def calculate_control_sum(personal_num, multiplier):
    # personal_num = [int(x) for x in str(personal_num)]
    control_sum = 0
    for num in personal_num[:10]:
        num = int(num)
        num *= multiplier
        control_sum += num
        multiplier += 1
        if multiplier == 10:
            multiplier = 1
    return control_sum


def generate_control_num(personal_num):
    # control num case 1
    control_sum = calculate_control_sum(personal_num, 1)
    control_num = control_sum % 11
    if control_num != 10:
        return control_num
    else:
        # control num case 2
        control_sum = calculate_control_sum(personal_num, 3)
        control_num = control_sum % 11
        if control_num != 10:
            return control_num
        else:
            return 0


def check_length(personal_num):
    if len(personal_num) == 11:
        return True
    return False


# TODO: fix return values for incorrect gender and year
# 1. check if given gender_and_century_num value is in gender_century_map
# 2. if value is there, return it
# 3. return the value by given year and gender.
# 4. if the given year and gender is not in map, return false
def check_gender_and_century(gender_and_century_num=None, year=None, gender=None):
    # correct_gender = bool()
    # correct_year = bool()
    century_gender_map = {
        (1800, "male"): 1,
        (1800, "female"): 2,
        (1900, "male"): 3,
        (1900, "female"): 4,
        (2000, "male"): 5,
        (2000, "female"): 6,
    }
    if year is None and gender is None:
        for value in century_gender_map.values():
            if gender_and_century_num == value:
                return value
    elif gender_and_century_num is None:
        year_century = year // 100 * 100
        keys = [x for x in century_gender_map.keys()]

        for item in keys:
            if item[0] == year_century and item[1] == gender:
                return century_gender_map.get((year_century, gender))
            else:
                return False


def check_queue_num(num):
    if len(str(num)) == 1:
        return "00" + str(num)
    elif len(str(num)) == 2:
        return "0" + str(num)
    elif len(str(num)) > 3:
        return False
    return num


def check_birth_month(given_month):
    if given_month in range(1, 13):
        return True
    return False


def check_birth_day(given_day):
    if given_day in range(1, 32) or given_day in range(1, 30):
        return True
    return False


def check_control_num(personal_num, given_control_num):
    if generate_control_num(personal_num) == given_control_num:
        return True
    return False


# function to check if given personal num is valid
def personal_number_check(number):
    personal_num = [int(x) for x in str(number)]
    given_gender_and_century = personal_num[0]
    given_control_num = personal_num[-1]
    given_year = int(str(personal_num[1]) + str(personal_num[2]))
    given_month = int(str(personal_num[3]) + str(personal_num[4]))
    given_day = int(str(personal_num[5]) + str(personal_num[6]))

    if not check_length(personal_num):
        return f"incorrect number length ({len(personal_num)})"
    if not (check_gender_and_century(given_gender_and_century, None, None) == given_gender_and_century):
        return f"incorrect first number ({personal_num[0]})"
    if not (check_birth_month(given_month) and check_birth_day(given_day)):
        match given_gender_and_century:
            case 1 | 2:
                return f"date 18{given_year}-{given_month}-{given_day} is incorrect."
            case 3 | 4:
                return f"date 19{given_year}-{given_month}-{given_day} is incorrect."
            case 5 | 6:
                return f"date 20{given_year}-{given_month}-{given_day} is incorrect."
    if not check_control_num(personal_num, given_control_num):
        return f"incorrect control number (has to be {generate_control_num(personal_num)})"
    return f"personal number {number} is valid"


# function to generate personal num from given gender, date and birth queue
def generate_personal_number(gender, date, queue):
    year = int(date.split("-")[0])
    month = date.split("-")[1]
    day = date.split("-")[2]

    if check_gender_and_century(None, year, gender):
        gender_and_century_digit = str(check_gender_and_century(None, year, gender))
    else:
        return f"invalid gender '{gender}' or year '{year}'"
    year_digits = str(year)[2] + str(year)[3]
    queue_digits = str(queue)
    if not check_queue_num(queue_digits):
        return f"incorrect queue number ({queue})"
    else:
        queue_digits = check_queue_num(queue_digits)

    ten_digits = gender_and_century_digit + year_digits + month + day + queue_digits
    generated_personal_num = int(ten_digits + str(generate_control_num(ten_digits)))

    return generated_personal_num


print(generate_personal_number("male", "3000-11-14", 23))
# print(personal_number_check(52311142230))
