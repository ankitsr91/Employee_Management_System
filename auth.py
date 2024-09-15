import re
import dbs

# Email regex pattern
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def authenticate_user(email_id, employee_id):
    # Check if the email_id is valid
    if not re.fullmatch(regex, email_id):
        print("Invalid Email ID")
        return False
    
    sql = 'SELECT * FROM empdata WHERE Email_Id = %s AND Id = %s'
    data = (email_id, employee_id)
    c = dbs.con.cursor(buffered=True)
    c.execute(sql, data)
    
    if c.rowcount == 1:
        return True
    else:
        print("Invalid Employee ID or Email ID")
        return False