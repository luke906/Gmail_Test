from Gmail_Manager_Class import Gmail_Manager
from Schedule_Manager_Class import Schedule_Manager

sched = None
_REQUEST_TOKEN_VALUE = None

scheduler = Schedule_Manager()

def get_airbit_token_value(secret_json_file):

    print("get_airbit_token_value JOB START!")

    global sched
    global _REQUEST_TOKEN_VALUE

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
        # 가장 최신의 첫번째 메일의 메세지 간략 보기 내용을 스페이스로 구분하여 모두 검사한다.
        for sub in message_list[0]['Snippet'].split(' '):
            #수신 메일의 제목에 "Token"이 들어가 있는지 검사, 전송자가 에어비트이고 메세지 본문중 32자리 토큰 이라면
            if message_list[0]['Subject'][0:5] == "Token" and \
                     message_list[0]['Sender'] == "<servers@bitbackoffice.com>" and \
                                      len(sub) == 32:
                _REQUEST_TOKEN_VALUE = sub
                scheduler.kill_scheduler("token_job")
                print("Request Token is : %s" % _REQUEST_TOKEN_VALUE)
                print("get_airbit_token_value JOB STOP!")
                break


def main():

    scheduler.start_scheduler(get_airbit_token_value, 'interval', "token_job", 3, "gmail-python-chargerunit01.json")


if __name__ == '__main__':
    main()
