from django.core.mail import send_mail

subject = 'ITSP Reimbursement Status'
message = 'This is a system generated mail. Please do not reply to this. Contact T Sanjev Vishnu'

send_mail(
    'ITSP Reimbursement Status' ,
    'This is a system generated mail Do not reply Contact T Sanjev Vishnu',
    'vishnutsanjevofficial@gmail.com' ,
    ['180110090@iitb.ac.in'] ,
    fail_silently = False,
)
