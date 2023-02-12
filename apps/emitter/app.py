from datetime import datetime

def get_database():
    pass
    
if __name__ == '__main__':    
    test_db = get_database()
    from time import sleep
    errors = 0
    i = 0
    while True:
        sleep(0.1)
        i += 1
        try:
            print(datetime.now().strftime('%Y-%M-%d %H:%m:%S'), ' Inserted, errors: ', str(errors))
        except Exception as e:
            print('******** Exception:')
            print(e)
            errors += 1
            test_db = get_database()
