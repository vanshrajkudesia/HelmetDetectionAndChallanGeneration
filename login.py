import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import smtplib, reportlab, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from email.mime.text import MIMEText
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer



def login():
    username = entry_username.get()
    password = entry_password.get()
    global email_org 
    email_org = entry_email.get()
    global rc
    rc = entry_rc.get()

    # Check if username, password, and email are valid (for demonstration purposes)
    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        
        show_image_upload()
        
    else:
        messagebox.showerror("Login Failed", "Invalid username, password, or email")

def send_email():
    recipient_email = email_org
    image_path = uploaded_image_path

    # Create a PDF file with the uploaded image
    pdf_path = "converted_image.pdf"
    convert_image_to_pdf(image_path, pdf_path)

    # Email configuration
    sender_email = 'vanshrajkudesia'
    
    
    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Vehicle Challan: Riding Without Helmet'

    # Attach the PDF file
    with open(pdf_path, 'rb') as file:
        custom_text ="#Helmet lagao mitro"
        attachment = MIMEApplication(file.read(), _subtype="pdf")
        attachment.add_header('Content-Disposition', f'attachment; filename={pdf_path}')
        message.attach(attachment)

        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Indian Traffic Rule: Helmet</title>
        </head>
        <body>
        <h1>Indian Traffic Rule: Helmet</h1>
        <p>In India, it is mandatory to wear a helmet while riding a two-wheeler. This is an essential traffic rule designed for the safety of the rider.</p>
        
        <h2>Key Points:</h2>
        <ul>
            <li><strong>Mandatory:</strong> Wearing a helmet is mandatory for both riders and pillion riders.</li>
            <li><strong>Safety:</strong> Helmets provide crucial protection in case of accidents, reducing the risk of head injuries.</li>
            <li><strong>Fine:</strong> Violating the helmet rule can result in fines imposed by traffic authorities.</li>
        </ul>

        <h2>Image: Helmet Usage</h2>
        <img src="https://www.motorbeam.com/wp-content/uploads/Motorcycle-Helmet-Comfort.jpg" alt="Helmet Usage" style="max-width: 100%; height: auto;">
        <img src="https://www.studds.com/Adminpanel/uploads/Kids-helmet-studds.jpg" alt="Helmet Usage" style="max-width: 100%; height: auto;">
        <p>Always adhere to traffic rules and prioritize safety on the road. Wearing a helmet is a simple yet effective measure to protect yourself while riding.</p>
        </body>
        </html>
        """

        message.attach(MIMEText(html_content, 'html'))
        message.attach(MIMEText(custom_text, 'plain'))


    # Connect to SMTP server and send email
    try:
        s= smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('vanshrajkudesia','sjlodqamniuvzhju')
        s.sendmail('vanshrajkudesia@gmail.com', recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Something went wrong while sending the mail", e)
    finally:
        s.quit()
    

def convert_image_to_pdf(image_path, pdf_path):
    r = random.randint(100000000,200000000)
    # Get the current date and time
    current_datetime = datetime.now()
    driver = email_org
    driver = driver.split('@')[0]
    
    title = "Vehicle Challan Report"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, title=title)

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    text=f'''
    Dear {driver},\n
        This notice is issued to bring to your attention a violation of traffic safety regulations observed on {formatted_datetime}. It has been noted that you were riding a bike without wearing a helmet, which is a serious violation of traffic rules.

        Challan Details:\t
            Date and Time: {formatted_datetime}
            Location: Earth
            Violation: Riding without a helmet
            Fine Amount: 1000
            RC Details: {rc}

        We emphasize the importance of wearing a helmet while riding a two-wheeler. Helmets are designed to protect you in case of accidents, significantly reducing the risk of head injuries.

        Action Required:
        To resolve this matter, please pay the specified fine amount within the next [Number of Days] days. Failure to comply may result in additional penalties or legal action.

        Payment Details:\t
            Payment Method: Online
            Payment Deadline: 3 Days
            Amount: 1000
            Reference Number: {r}

        If you have any questions or concerns, please contact the [Traffic Department/Authority] at [Contact Information].

        Thank you for your understanding and cooperation in maintaining road safety.

        Sincerely,
        Traffic Department

    '''

    # Create styles for text
    styles = getSampleStyleSheet()

    # Split the multiline text into lines
    lines = [line.strip() for line in text.strip().split('\n')]

    # Create a list of Paragraph objects for each line
    paragraphs = [Paragraph(line, styles["Normal"]) for line in lines]

    # Create a title paragraph
    title_paragraph = Paragraph(title, styles["Title"])

    # Add an image to the PDF
    img = reportlab.platypus.Image(image_path, width=200, height=200)

    # Add title, image, and paragraphs to the PDF document
    doc.build([title_paragraph, Spacer(1, 12)] + [img] + paragraphs)
  


# In your upload_image function, after saving the uploaded_image_path:
def upload_image():
    global uploaded_image_path
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        uploaded_image_path = file_path
        send_email()  # Automatically send the email when logged in
        open_image_window(uploaded_image_path)
def image_path():
    return uploaded_image_path
        

def show_image_upload():
    login_frame.destroy()  # Destroy the login frame

    # Create a frame for image upload
    global upload_frame  # Make upload_frame a global variable so it can be accessed later
    upload_frame = tk.Frame(root, bg=bg_color)
    upload_frame.pack(expand=True, padx=20, pady=20)

    # Create a button to upload an image
    upload_button = tk.Button(upload_frame, text="Upload Image", command=upload_image, bg=bg_color, fg=fg_color, font=("Arial", 16))
    upload_button.pack(pady=50)


def open_image_window(image_path):
    # Close the current window
    root.destroy()

    # Create a new window for displaying the image
    image_window = tk.Tk()
    image_window.title("Image Viewer")

    # Load and display the selected image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image_window, image=photo, bg=bg_color)
    image_label.photo = photo
    image_label.pack(pady=10)

    image_window.mainloop()


# Create the main application window
root = tk.Tk()
root.title("Login Page")

# Set the window size to 1080x720
window_width = 1080
window_height = 720
root.geometry(f"{window_width}x{window_height}")

# Load the transparent PNG image with rounded corners
image = Image.open("rounded_corners.png")
image = image.resize((window_width, window_height))  # Resize image

# Save the image to a temporary file and open it again to avoid a known issue with tkinter and PIL
temp_file_path = "temp_background_image.png"
image.save(temp_file_path)
bg_image = Image.open(temp_file_path)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the image as a background
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define dark mode colors
bg_color = "#121212"  # Dark background color
fg_color = "#FFFFFF"  # Light text color

# Configure the frame with dark mode colors
login_frame = tk.Frame(root, bg=bg_color)
login_frame.pack(expand=True, padx=50, pady=50)  # Increased padding for input area

# Create username label and entry
label_username = tk.Label(login_frame, text="Username:", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_username.grid(row=0, column=0, sticky=tk.W)
entry_username = tk.Entry(login_frame, bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Create email label and entry
label_email = tk.Label(login_frame, text="Email (challan to be sent):", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_email.grid(row=1, column=0, sticky=tk.W)
entry_email = tk.Entry(login_frame, bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Create password label and entry
label_password = tk.Label(login_frame, text="Password:", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_password.grid(row=2, column=0, sticky=tk.W)
entry_password = tk.Entry(login_frame, show="*", bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Create password label and entry
label_rc = tk.Label(login_frame, text="RC Details:", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_rc.grid(row=3, column=0, sticky=tk.W)
entry_rc = tk.Entry(login_frame, bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_rc.grid(row=3, column=1, padx=10, pady=10)

# Create login button with dark mode colors
login_button = tk.Button(login_frame, text="Login", command=login, bg=bg_color, fg=fg_color, font=("Arial", 16))
login_button.grid(row=4, column=0, columnspan=2, pady=20)

# Create a label to display the uploaded image
uploaded_image_label = tk.Label(login_frame, bg=bg_color)
uploaded_image_label.grid(row=5, column=0, columnspan=2, pady=10)



# Bind the "Enter" key to login
root.bind('<Return>', lambda event: login())

# Initialize the variable to store the uploaded image path
uploaded_image_path = None

# Run the main event loop
root.mainloop()



# 


