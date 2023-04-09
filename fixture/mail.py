import poplib
import email
import time


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        # several times to try to connect
        for i in range(5):
            pop = poplib.POP3(self.app.config["james"]["host"])
            pop.user(username)
            pop.pass_(password)
            # get number of emails
            num = pop.stat()[0]
            if num > 0:
                # get emails one by one
                for n in range(num):
                    # we need 2nd element in the tuple returned by retr (it's list of lines)
                    msglines = pop.retr(n+1)[1]
                    # decode byte strings to string and join to text
                    msgtext = "\n".join(map(lambda x: x.decode("utf-8"), msglines))
                    # parse text as email
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        # mark to be deleted
                        pop.dele(n+1)
                        # close with save
                        pop.quit()
                        return msg.get_payload()
            pop.quit()
            time.sleep(3)
        return None

