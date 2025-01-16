from utils.logs.filehandler import logging
import mailparser
import email
import json

async def read_eml(file_path):
    try:
        mail = mailparser.parse_from_file(file_path)

        from_ = mail.from_
        to = mail.to
        subject = mail.subject
        date = mail.date
        #body = ''.join(mail.body)
        body = mail.text_plain if mail.text_plain else mail.text_html

        attachments = []
        for attachment in mail.attachments:
            attachments.append({
                'filename': attachment['filename'],
                'content_type': attachment['mail_content_type'],
                'payload': attachment['payload']
            })
    
        email_data = {
            'from': from_,
            'to': to,
            'subject': subject,
            'date': date,
            'body': body,
            'attachments': attachments
        }
        
        return email_data
    except Exception as e:
        return (f"Error al leer el archivo .eml {file_path}: {e}")
    
