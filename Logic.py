from exceptions import CreditTypeError, CollegeEnrollmentError, SemestersError


medium_term_credit_interest_rate_30 = 0.0115 #1,15% mes vencido
medium_term_credit_interest_rate_60 = 0.099 #0,99% mes vencido
short_term_credit_interest_rate_100 = 0.099 #0,99% mes vencido


def ask_information():
    while True:
        credit_type = input("Enter the type of credit you want \n 1 for 30%\n 2 for 60%\n 3 for 100%\n")
        
        if credit_type in {"1", "2", "3"}:
            credit_type = int(credit_type)  # Convertimos a entero después de validar
            break
        print("Invalid option. Please enter 1, 2, or 3.")

    while True:
        try:
            college_enrollment = float(input("Enter the amount of college enrollment per semester: "))
            if college_enrollment > 0:  # Aseguramos que sea un número positivo
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid option. Please enter a valid number.")

    while True:
        try:
            semesters = int(input("Enter the number of semesters you want to calculate for: "))
            if semesters > 0:  # Aseguramos que el número de semestres sea positivo
                break
            else:
                print("Invalid number of semesters. Please enter a positive integer.")
        except ValueError:
            print("Invalid option. Please enter a valid integer.")

    return credit_type, college_enrollment, semesters


def payment_fee_calc_while_studying(credit_type, college_enrollment, semesters):
    if credit_type == 1:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError("Invalid college enrollment")
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError("Invalid number of semesters")
        payment_fee =  (0.3 * college_enrollment * semesters* medium_term_credit_interest_rate_30) / (1 - (1 + medium_term_credit_interest_rate_30)**(-1 * (semesters/2) * 12))
    elif credit_type == 2:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError("Invalid college enrollment")
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError("Invalid number of semesters")
        payment_fee =  (0.6 * college_enrollment * semesters * medium_term_credit_interest_rate_60) / (1 - (1 + medium_term_credit_interest_rate_60)**(-1 * (semesters/2) * 12))
    elif credit_type == 3:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError("Invalid college enrollment")
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError("Invalid number of semesters")
        payment_fee = (college_enrollment * semesters * short_term_credit_interest_rate_100) / (1 - (1 + short_term_credit_interest_rate_100)**(-1 * (semesters/2) * 12))
    else:
        raise CreditTypeError("Invalid credit type")
    return payment_fee

def payment_fee_calc_after_studying(credit_type, college_enrollment, semesters):
    if credit_type == 1:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError("Invalid college enrollment")
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError("Invalid number of semesters")
        payment_fee =  (0.7 * college_enrollment * semesters* medium_term_credit_interest_rate_30) / (1 - (1 + medium_term_credit_interest_rate_30)**(-1.5 * (semesters/2) * 12))
    elif credit_type == 2:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError("Invalid college enrollment")
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError("Invalid number of semesters")
        payment_fee =  (0.4 * college_enrollment * semesters * medium_term_credit_interest_rate_60) / (1 - (1 + medium_term_credit_interest_rate_60)**(-1.5 * (semesters/2) * 12))
    elif credit_type == 3:
        return None
    else:
        raise CreditTypeError("Invalid credit type")
    return payment_fee