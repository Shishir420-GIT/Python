import re

str2 = "passw7yyhe"

def validate(Password):
  validate = False
  count = 0
  i = 0
  try:
    if len(Password) < 9:
      raise Exception("Password should be min 8 characters")
    elif not Password.isalnum:
      raise Exception("Password must have numbers")
    elif re.search("[,.@;'-+_']", Password):
      raise Exception("Password must not special characters")
    else:
      for i in range(len(Password)):
        if count < 2 and Password[i].isupper() or Password[i].islower():
            count += 1
        if count > 2:
            validate = True
            break
    if validate == True:
        return True, f"Password Validation Succeeded"
    else:
        return False, f"Password Validation Failed"
  except Exception as e:
    return False, f"Failed: {str(e)}"


print(validate(str2))
