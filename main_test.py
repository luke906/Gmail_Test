from Gmail_Manager_Class import Gmail_Manager


def main():

    Gmail = Gmail_Manager('gmail-python-chargerunit01.json')

    message_list = Gmail.get_unread_message()
    unread_message_count = Gmail.get_unread_message_count()

    # 읽지 않은 메세지가 존재 한다면
    if unread_message_count > 0:
        print(message_list[0]['Snippet'])
        print(message_list[0]['Sender'])

        # 32자리 토큰을 구한다.
        # 메세지 간략 보기 내용을 스페이스로 구분하여 모두 검사한다.
        for sub in message_list[0]['Snippet'].split(' '):
            # 전송자가 에어비트이고 메세지 본문중 32자리 토큰 이라면
            if len(sub) == 32 and message_list[0]['Sender'] == "<servers@bitbackoffice.com>":
                _REQUEST_TOKEN_VALUE = sub
                print("Request Token is : %s" % _REQUEST_TOKEN_VALUE)



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
