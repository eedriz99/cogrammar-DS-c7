class Email:
    def __init__(self, email_address: str, subject_line: str, email_content: str):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read: bool = False
    def mark_as_read(self):
        self.has_been_read = True

inbox: list[object] = []

def list_emails():
    for id, mail in enumerate(inbox):
        print(id, mail.subject_line)

def populate_inbox(address: str, subject: str, content: str):
    mail = Email(address, subject, content)
    inbox.append(mail)
    print(f"{mail.subject_line} has been added to inbox!")

def read_email(id: int):
    mail: obj = inbox[id]
    print(f"Address: {mail.email_address} \n Subject: {mail.subject_line} \n Content: {mail.email_content}")
    mail.mark_as_read()

def view_unread():
    for id, mail in enumerate(inbox):
        if mail.has_been_read == False:
            print(id, mail.subject_line)
        else:
            continue


def delete_email(id: int):
    deleted = inbox.pop(id)
    print(f"{deleted.subject_line} has been deleted from your inbox")

addresses: list[str] = ['service@tmail.com', 'security@tmail.com', 'service@tmail.com']
subjects: list[str] = ['Welcome to TMail', 'Safeguard your account', 'User onboarding']
for i in range(len(subjects)):
    populate_inbox(addresses[i], subjects[i], '')

action: str = input("Welcome to TMail, your favourite email on terminal service.\n What action will you like to perform? Enter\n>inbox - to check your inbox\n>send - to send email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
while action != 'quit':
    if action == 'inbox':
        list_emails()
        action: str = input("\n>inbox - to check your inbox\n>send - to se>nd email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
    elif action == 'send':
        address: str = input("Enter recipient email address\n")
        subject: str = input("Enter email subject\n")
        content: str = input("Enter your email content\n")
        populate_inbox(address, subject, content)
        action: str = input("\n>inbox - to check your inbox\n>send - to se>nd email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
    elif action == 'read':
        id: int = int(input("Enter the ID of the email you will like to read\n"))
        read_email(id)
        action: str = input("\n>inbox - to check your inbox\n>send - to se>nd email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
    elif action == 'view':
        view_unread()
        action: str = input("\n>inbox - to check your inbox\n>send - to se>nd email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
    elif action == 'delete':
        id: int = int(input("Enter the id of the email you will like to delete\n"))
        delete_email(id)
        action: str = input("\n>inbox - to check your inbox\n>send - to send email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
    else:
        print("Invalid input, check and try again!")
        action: str = input("Enter\n>inbox - to check your inbox\n>send - to send email\n>read - to read a mail\n>delete - to delete a mail\n>view - to see unread mails\n>quit - to quit\n").lower()
