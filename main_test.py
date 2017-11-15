from Gmail_Manager_Class import Gmail_Manager
from apscheduler.schedulers.blocking import BlockingScheduler

sched = None
token_value = None

def get_airbit_token_value(secret_json_file):

    global sched

    print("get_airbit_token_value JOB START!")
    _REQUEST_TOKEN_VALUE = None
    Gmail = Gmail_Manager()
    Gmail.get_credentials(secret_json_file)

    unread_message_count = Gmail.get_unread_message_count()

    # 읽지 않은 메세지가 존재 한다면
    if unread_message_count > 0:
        #print(message_list[0]['Snippet'])
        #print(message_list[0]['Sender'])

        message_list = Gmail.get_unread_message()
        # 32자리 토큰을 구한다.
        # 메세지 간략 보기 내용을 스페이스로 구분하여 모두 검사한다.
        for sub in message_list[0]['Snippet'].split(' '):
            # 전송자가 에어비트이고 메세지 본문중 32자리 토큰 이라면
            if len(sub) == 32 and message_list[0]['Sender'] == "<servers@bitbackoffice.com>":
                _REQUEST_TOKEN_VALUE = sub
                print("Request Token is : %s" % _REQUEST_TOKEN_VALUE)
                print("get_airbit_token_value JOB STOP!")
                sched.remove_job("token_job")

    return _REQUEST_TOKEN_VALUE

def get_token(json_file_name):

    global token_value
    token_value = get_airbit_token_value(json_file_name)
    #token_value = get_airbit_token_value("gmail-python-chargerunit03.json")

def main():

    global sched
    global token_value

    get_token('gmail-python-chargerunit03.json')

    sched = BlockingScheduler()

    sched.add_job(get_token, "interval", seconds=5, id="token_job", args=(json_file_name))
    sched.start()

    print("job finished!")
    print("Request Token is : %s" % token_value)








    """
    
    
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

    lable_id = ['INBOX']
    messages_list = ListMessagesWithLabels(service, 'me', lable_id)
    print(messages_list)

    message = GetMessage(service, 'me', '15ef61246bfe2e4f')
    # print(message['parts'])
    """


if __name__ == '__main__':
    main()
