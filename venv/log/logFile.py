# log file

import datetime


def write_log(data):
    with open('log.txt', 'a') as f:
        f.write(format_time())
        f.write('  DEBUG\t')
        f.write(data)
        f.write('\n')


def update_log(data):
    write_log(data)


def update_log_start():
    write_log('\n*********************************************************************************************')
    write_log('************* Starting dummyTest on App: Games ******************')
    write_log('Opened Application: Games')


def update_log_exit():
    write_log('*************End Of Test on: Games***************')
    write_log('*********************************************************************************************\n')


def format_time():
    today = datetime.datetime.now()
    return f'{today.day}-{today.month}-{today.year} {today.hour}:{today.minute}'