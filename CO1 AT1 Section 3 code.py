import re

# Get input from user
register_number = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course_code = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

# Regular Expression Patterns
register_pattern = r"^\d{9}$"                              # Example: 192472138
email_pattern = r"^\d{9}\.simats@saveetha\.com$"           # Example: 192472138.simats@saveetha.com
course_pattern = r"^(CSE|ECE|EEE|IT)\d{3}$"               # Example: CSE101
semester_pattern = r"^(Semester|Sem)[ -]?[1-8]$"          # Example: Semester 4
mobile_pattern = r"^(?:\+91[- ]?)?[6-9]\d{9}$"            # Example: 9876543210

# Validation
register_valid = bool(re.fullmatch(register_pattern, register_number))
email_valid = bool(re.fullmatch(email_pattern, email, re.IGNORECASE))
course_valid = bool(re.fullmatch(course_pattern, course_code, re.IGNORECASE))
semester_valid = bool(re.fullmatch(semester_pattern, semester, re.IGNORECASE))
mobile_valid = bool(re.fullmatch(mobile_pattern, mobile))

# Display Validation Report
print("\nValidation Report")
print("----------------------------")
print("Register Number:", "Valid" if register_valid else "Invalid")
print("Email:", "Valid" if email_valid else "Invalid")
print("Course Code:", "Valid" if course_valid else "Invalid")
print("Semester:", "Valid" if semester_valid else "Invalid")
print("Mobile Number:", "Valid" if mobile_valid else "Invalid")

# Final Registration Status
if (register_valid and email_valid and course_valid
        and semester_valid and mobile_valid):
    print("\nFinal Status: Registration Successful")
else:
    print("\nFinal Status: Registration Failed")
