# Data Validation Script for Insurance Customer Data
import pandas as pd

# import required libraries
# function to check if a value is null or empty
def is_null_or_empty(value):
    if pd.isnull(value) or value == '':
        return True
    return False

# function to validate email format using regex
def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False

# function to validate date format YYYY-MM-DD
def is_valid_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
    # function to validate policy_id is exactly 10 digits
def is_valid_policy_id(policy_id):
    if isinstance(policy_id, str) and policy_id.isdigit() and len(policy_id) == 10:
        return True
    return False

# function to validate age is between 18 and 100
def is_valid_age(age):
    if isinstance(age, int) and 18 <= age <= 100:
        return True
    return False    


# function to run all validations on a customer record and return results
def validate_customer_record(record):
    validation_results = {
        'customer_id': record.get('customer_id'),
        'is_valid': True,
        'errors': []
    }
    
    # Validate customer_id
    if is_null_or_empty(record.get('customer_id')):
        validation_results['is_valid'] = False
        validation_results['errors'].append('customer_id is null or empty')
    
    # Validate email
    if not is_valid_email(record.get('email', '')):
        validation_results['is_valid'] = False
        validation_results['errors'].append('Invalid email format')
    
    # Validate date_of_birth
    if not is_valid_date(record.get('date_of_birth', '')):
        validation_results['is_valid'] = False
        validation_results['errors'].append('Invalid date format for date_of_birth')
    
    # Validate policy_id
    if not is_valid_policy_id(record.get('policy_id', '')):
        validation_results['is_valid'] = False
        validation_results['errors'].append('Invalid policy_id format')
    
    # Validate age
    if not is_valid_age(record.get('age', 0)):
        validation_results['is_valid'] = False
        validation_results['errors'].append('Age must be between 18 and 100')
    
    return validation_results

# test the validator with sample insurance customer data
# sample data: name, email, date_of_birth, policy_id, age
sample_data = [
    {
        'customer_id': 'CUST001',
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'date_of_birth': '1985-01-01',
        'policy_id': 'POLICY123456',
        'age': 38
    }
]   