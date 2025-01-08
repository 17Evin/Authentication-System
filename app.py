# from flask import Flask, request, render_template
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     to_address = request.form.get('to_address')

#     # Your Gmail credentials
#     gmail_user = 'cache3988@gmail.com'  # Replace with your Gmail address
#     app_password = 'wizm phmi ajec sody'  # Replace with your App Password

#     # Create the email content
#     subject = 'Verification Team'
#     body = """<html>
#                 <body>
#                     <p>Hello,</p>
#                     <p>Your verification details:</p>
#                     <table border="1">
#                         <tr>
#                             <td style="background-color: #FF0000;">Red</td>
#                             <td style="background-color: #00FF00;">Green</td>
#                             <td style="background-color: #0000FF;">Blue</td>
#                             <td style="background-color: #FFFF00;">Yellow</td>
#                             <td style="background-color: #FF00FF;">Magenta</td>
#                         </tr>
#                     </table>
#                     <p>Thank you for using our service.</p>
#                 </body>
#             </html>
#             """

#     # Set up the MIME
#     message = MIMEMultipart()
#     message['From'] = gmail_user
#     message['To'] = to_address
#     message['Subject'] = subject

#     # Attach the body to the email
#     message.attach(MIMEText(body, 'html'))

#     try:
#         # Set up the SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()

#             # Log in to the server using App Password
#             server.login(gmail_user, app_password)

#             # Send the email
#             server.sendmail(gmail_user, to_address, message.as_string())

#         print(f"Email sent successfully to {to_address}")
#     except Exception as e:
#         print(f"Error sending email: {e}")

#     return render_template('verific.html')

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, request, render_template
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import random

# app = Flask(__name__)

# def generate_colors():
#     return ["Red", "Green", "Blue", "Yellow", "Magenta", "Gray", "Maroon", "Navy", "Purple", "Black"]

# def generate_unique_random_numbers(count, min_value, max_value):
#     numbers = list(range(min_value, max_value + 1))
#     random.shuffle(numbers)
#     return numbers[:count]

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     to_address = request.form.get('to_address')

#     # Your Gmail credentials
#     gmail_user = 'cache3988@gmail.com'  # Replace with your Gmail address
#     app_password = 'wizm phmi ajec sody'  # Replace with your App Password

#     # Generate dynamic content for the email
#     colors = generate_colors()
#     numbers = generate_unique_random_numbers(10, 1, 30)

#     table_html = '<table border="1" style="width: 200px;"><tr><th>Color</th><th>Random Number</th></tr>'
#     for i in range(10):
#         table_html += '<tr><td style="color:{}; text-align: center;">{}</td><td style="text-align: center;">{}</td></tr>'.format(colors[i], colors[i], numbers[i])
#     table_html += '</table>'

#     # Create the email content
#     subject = 'OTP - Verification Team'
#     body = f"""<html>
#                 <body>
#                     <p>Hi,</p>
#                     <p>Please select the number for your colour:</p>
#                     {table_html}
#                     <p>Thank you for using our service.</p>
#                     <p>Regards </P>
#                     <p>Verification team</p>
#                 </body>
#             </html>
#             """

#     # Set up the MIME
#     message = MIMEMultipart()
#     message['From'] = gmail_user
#     message['To'] = to_address
#     message['Subject'] = subject

#     # Attach the body to the email
#     message.attach(MIMEText(body, 'html'))

#     try:
#         # Set up the SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()

#             # Log in to the server using App Password
#             server.login(gmail_user, app_password)

#             # Send the email
#             server.sendmail(gmail_user, to_address, message.as_string())

#         print(f"Email sent successfully to {to_address}")
#     except Exception as e:
#         print(f"Error sending email: {e}")

#     return render_template('verific.html')

# if __name__ == '__main__':
#     app.run(debug=True)






from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

app = Flask(__name__)

def generate_colors():
    return ["Red", "Green", "Blue", "Yellow", "Magenta", "Gray", "Maroon", "Navy", "Purple", "Black"]

def generate_unique_random_numbers(count, min_value, max_value):
    numbers = list(range(min_value, max_value + 1))
    random.shuffle(numbers)
    return numbers[:count]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    to_address = request.form.get('to_address')

    # Your Gmail credentials
    gmail_user = 'cache3988@gmail.com'  # Replace with your Gmail address
    app_password = 'wizm phmi ajec sody'  # Replace with your App Password

    # Generate dynamic content for the email
    colors = generate_colors()
    numbers = generate_unique_random_numbers(10, 1, 30)

    table_html = '<table border="1" style="width: 200px;"><tr><th>Color</th><th>Random Number</th></tr>'
    for i in range(10):
        table_html += '<tr><td style="color:{}; text-align: center;">{}</td><td style="text-align: center;">{}</td></tr>'.format(colors[i], colors[i], numbers[i])
    table_html += '</table>'

    # Create the email content
    subject = 'OTP - Verification Team'
    body = f"""<html>
                <body>
                    <p>Hi,</p>
                    <p>Please select the number for your colour:</p>
                    {table_html}
                    <p>Thank you for using our service.</p>
                    <p>Regards </P>
                    <p>Verification team</p>
                </body>
            </html>
            """

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = gmail_user
    message['To'] = to_address
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'html'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()

            # Log in to the server using App Password
            server.login(gmail_user, app_password)

            # Send the email
            server.sendmail(gmail_user, to_address, message.as_string())

        print(f"Email sent successfully to {to_address}")

        # If email is sent successfully, render verific.html
        return render_template('verific.html')
    except Exception as e:
        print(f"Error sending email: {e}")

    # If there is an error in sending email, render some error page or the same verific.html
    return render_template('verific.html')

@app.route('/submit_hello', methods=['POST'])
def submit_hello():
    # Process the form data from hello.html if needed
    # ...

    # After processing, render hello.html
    return render_template('hello.html')

@app.route('/hello')
def welcome():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
