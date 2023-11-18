import imaplib
import email
import os
from database import Database
from scan import Scan


class Parse:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.database = Database("database.db")
	
	def parse_messages(self, label):
		host = "imap.mail.ru"

		username = self.username
		password = self.password

		mail = imaplib.IMAP4_SSL(host)
		mail.login(username, password)

		resp, folders = mail.list()
		clear_folders = []
		clear_folders.append("inbox")

		for folder in folders:
			ff = folder.decode('utf-8')
			if ff.split(' "/" ')[0] == "()" and "INBOX" not in ff.split(' "/" ')[-1] and "Archive" not in ff.split(' "/" ')[-1]:
				gg = ff.split(' "/" ')[-1]
				clear_folders.append(gg)
		
		for i in clear_folders:
			mail.select(i)

			typ, data = mail.search(None, label)
			for num in data[0].split():
				typ, msg_data = mail.fetch(num, '(RFC822)')
				mail.store(num, "+FLAGS", "\Seen")
				raw_email = msg_data[0][1]
				email_message = email.message_from_bytes(raw_email)
				email_from = email_message["from"]
				name, email_addr = email.utils.parseaddr(email_from)
				name = email.header.decode_header(name)[0][0]
				name = name if isinstance(name, str) else name.decode("utf-8")
				self.database.create_user(email_addr, name)
				num = num.decode('utf-8').strip()

				folder_text = f'Messages/{email_addr}/texts'
				folder_files = f'Messages/{email_addr}/files'

				try:
					os.makedirs(folder_text)
					os.makedirs(folder_files)
				except:
					pass
				for part in email_message.walk():
					if part.get_content_type() == 'text/plain':
						body = part.get_payload(decode=True).decode('utf-8')
						with open(os.path.join(os.getcwd(), folder_text + f'/{num}.txt'), 'w', encoding='utf-8') as f:
							f.write(body)
					if part.get_content_disposition() == 'attachment':
						filename = part.get_filename()
						filename = email.header.decode_header(filename)[0][0]
						if isinstance(filename, bytes):
							filename = filename.decode('utf-8')
						filename = os.path.normpath(filename)
						with open(os.path.join(os.getcwd(), folder_files + f'/{filename}'), 'wb') as f:
							f.write(part.get_payload(decode=True))
						Scan(folder_files + f'/{filename}', email_addr).scan()
				
		mail.close()
		mail.logout()
