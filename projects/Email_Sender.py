import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, file_path):
    
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach body
    message.attach(MIMEText(body, 'plain'))

    # Attach file
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename=Mayank_Khatri_Resume.pdf",
    )

    message.attach(part)

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Update with your SMTP server details
        server.ehlo()
        server.starttls()
        #print('trying to login..')
        server.login(sender_email, sender_password)
        #print('logged in successfully')
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        #print("Email sent successfully!")
    except Exception as e:
        print("Email could not be sent:", str(e))
    finally:
        server.quit()

# Example usage
sender_email = "sender email"
sender_password = "sender email sender_password"
receiver_email = "receiver email"
subject = "subject for application"

body = "Dear Hiring Manager, \
\n\
\nI am writing to express my interest in the Software Developer Backend position at Flipkart.With hands-on experience in backend development, I am eager to contribute to your team.\
\n\
\nDuring my recent internship at ITech Solutions, I developed microservices for an accounting application, honing my skills in client-facing requests and server-side logic implementation. My self-initiated projects, such as the ToDo App Backend and Library Management Portal, further demonstrate my proficiency in Python-Flask,Django MySQL, and backend development methodologies.\
\nAdditionally, coursework in Fundamental Algorithms, Python programming, and Java development has equipped me with a strong foundation in data structures, algorithms, and programming languages.\
\n\
\nI am genuinely excited about the opportunity to join Flipkart and contribute to innovative projects. Thank you for considering my application. I look forward to discussing how my skills and enthusiasm can benefit your team.Please find my resume attached.\
\nThank you for your time and consideration.\
\n\
\nSincerely,\
\n\
\nMayank Khatri [7999208011]"\

file_path = "C:\\Users\\Khatri\\Desktop\\Mayank_Khatri_Resume.pdf" 

send_email(sender_email, sender_password, receiver_email, subject, body, file_path)



"""
smtplib is a Python library that provides an SMTP (Simple Mail Transfer Protocol) used to send email messages , 
directly from your Python script or application.

MIME (Multipurpose Internet Mail Extensions) is an extension of the original Simple Mail Transport Protocol (SMTP) email protocol. 
MIME is a kind of add-on or a supplementary protocol that allows non-ASCII data to be sent through SMTP. 
It lets users exchange different kinds of data files, including audio, video, images and application programs, pdfs over email.

MIMEMultipart:
---------------
MIMEMultipart is used to represent a multipart email message. It allows you to construct an email with multiple parts, such as plain text, HTML, and attachments.
Explanation: When you want to send an email with both text and attachments, you need to create a multipart message. 
MIMEMultipart provides methods to add various parts to the message, such as text and attachments, and handles the organization of these parts within the email structure.

MIMEText:
----------
MIMEText is used to represent the text part of an email message.
Explanation: When you want to include text content in an email, you use MIMEText. 
It allows you to specify the text content of the email message, whether it's plain text or HTML-formatted text. 
You can then attach this text part to a MIMEMultipart message.

MIMEBase:
---------
Use: MIMEBase is used to represent the base MIME type for attachments in an email message.
Explanation: When you want to attach files (such as PDFs, images, etc.) to an email, you use MIMEBase. 
It provides a base class for creating MIME objects representing various types of attachments. 
You can create a MIMEBase object, set its payload to the content of the file, and then attach it to a MIMEMultipart message.

encoders:
----------
Use: encoders provides functions to encode and decode MIME objects for transmission over email.
Explanation: When attaching files to an email, you need to encode them properly for transmission. 
encoders module provides functions like encode_base64() to encode binary data (such as file contents) into a base64-encoded string, 
which is suitable for email transmission. This encoding ensures that the file attachments are properly formatted for sending via email.

In summary, these modules work together to construct email messages with text content and attachments. 
MIMEMultipart manages the overall structure of the email, MIMEText handles the text content, MIMEBase represents attachments, and encoders ensures proper encoding of attachment data for transmission.

message = MIMEMultipart(): This line creates a new MIMEMultipart object named message. MIMEMultipart is a subclass of email.message.Message and represents a multipart email message, which can contain multiple parts such as text, attachments, or other MIME types.
message['From'] = sender_email: This line sets the "From" header of the email message to the value specified in the sender_email variable. The "From" header typically contains the email address of the sender.
message['To'] = receiver_email: This line sets the "To" header of the email message to the value specified in the receiver_email variable. The "To" header contains the email address of the primary recipient of the email.
message['Subject'] = subject: This line sets the "Subject" header of the email message to the value specified in the subject variable. The "Subject" header contains the subject or title of the email message.
Overall, this code initializes a MIMEMultipart object for composing an email message, sets the sender, recipient, and subject headers, and prepares the object to be further populated with additional content such as text or attachments before sending the email.

message.attach(MIMEText(body, 'plain'))
-----------------------------------------
MIMEText(body, 'plain'): This creates a MIMEText object representing the plain text content of the email message. The body variable contains the text content of the message. The second argument 'plain' specifies that the content type of the message is plain text. This means that the content will be displayed as plain text when the recipient receives the email.
message.attach(...): This method attaches the MIMEText object to the MIMEMultipart object message. Attaching the text part to the multipart message allows you to include both text and other types of content (such as attachments) within the same email message.

with open(file_path, "rb") as attachment:: This line opens the file located at file_path in binary read mode ("rb"), creating a file object named attachment. The with statement ensures that the file is properly closed after its suite finishes executing.
part = MIMEBase("application", "octet-stream"): This line creates a MIMEBase object named part. MIMEBase is a base class for MIME email messages that represent generic binary data. The first argument "application" specifies the primary content type of the data, and the second argument "octet-stream" specifies the specific subtype, indicating that the data is arbitrary binary data.
part.set_payload(attachment.read()): This line reads the contents of the file using attachment.read() and sets it as the payload (content) of the MIMEBase object part. The payload is the actual data being attached to the email message.

part.add_header("Content-Disposition", f"attachment; filename= {file_path}"): This line adds a header to the MIMEBase object part. The "Content-Disposition" header specifies the disposition type of the content, in this case, attachment, indicating that the data is an attachment rather than inline content. The filename parameter within the header specifies the name of the attached file. The file_path variable is used to specify the filename. The f"attachment; filename= {file_path}" format string is used to dynamically include the filename in the header.
message.attach(part): This line attaches the MIMEBase object part to the MIMEMultipart object message. By attaching part to message, you include the attachment as part of the multipart email message, allowing it to be sent along with the email.
"""