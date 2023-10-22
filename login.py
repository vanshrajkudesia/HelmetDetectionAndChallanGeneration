import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import smtplib
# wiet lcuh wkpg kvns 
def login():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    # Check if username, password, and email are valid (for demonstration purposes)
    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        send_email()  # Automatically send the email when logged in
        show_image_upload()
    else:
        messagebox.showerror("Login Failed", "Invalid username, password, or email")

def send_email():
    recipient_email = entry_email.get()
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('vanshrajkudesia','fwazxphukmzlucsu')

    try:
        s.sendmail('vanshrajkudesia@gmail.com'
                , recipient_email,'hello bhai! mail gen. by application')
    except Exception as e:
        print("Something went wrong while sending the mail", e)
        
    s.quit()






def show_image_upload():
    login_frame.destroy()  # Destroy the login frame

    # Create a frame for image upload
    global upload_frame  # Make upload_frame a global variable so it can be accessed later
    upload_frame = tk.Frame(root, bg=bg_color)
    upload_frame.pack(expand=True, padx=20, pady=20)

    # Create a button to upload an image
    upload_button = tk.Button(upload_frame, text="Upload Image", command=upload_image, bg=bg_color, fg=fg_color, font=("Arial", 16))
    upload_button.pack(pady=50)

# Function to handle image upload
def upload_image():
    global uploaded_image_path
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        # Save the uploaded image path for later use
        uploaded_image_path = file_path
        open_image_window(uploaded_image_path)

    

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
label_email = tk.Label(login_frame, text="Email:", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_email.grid(row=1, column=0, sticky=tk.W)
entry_email = tk.Entry(login_frame, bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Create password label and entry
label_password = tk.Label(login_frame, text="Password:", bg=bg_color, fg=fg_color, font=("Arial", 16))
label_password.grid(row=2, column=0, sticky=tk.W)
entry_password = tk.Entry(login_frame, show="*", bg=bg_color, fg=fg_color, font=("Arial", 16))
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Create login button with dark mode colors
login_button = tk.Button(login_frame, text="Login", command=login, bg=bg_color, fg=fg_color, font=("Arial", 16))
login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Create a label to display the uploaded image
uploaded_image_label = tk.Label(login_frame, bg=bg_color)
uploaded_image_label.grid(row=4, column=0, columnspan=2, pady=10)



# Bind the "Enter" key to login
root.bind('<Return>', lambda event: login())

# Initialize the variable to store the uploaded image path
uploaded_image_path = None

# Run the main event loop
root.mainloop()



# 

