from django.core.mail import send_mail send_mail( 
    'Subject here', 
    'Here is the message.', 
    'Krish Patel', 
    [20CE089@charusat.edu.in],     
    fail_silently=False, 
) 