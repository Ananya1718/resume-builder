# resume_builder.py

print("Welcome to Resume Builder!\n")

name = input("Enter your full name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
college = input("Enter your college name: ")
degree = input("Enter your degree (e.g., B.Tech CSE): ")
year = input("Enter your graduation year: ")
skills = input("List your skills (comma-separated): ")
certifications = input("List certifications (comma-separated): ")

# Resume format
resume = f"""
-------------------------------
        RESUME
-------------------------------

Name: {name}
Email: {email}
Phone: {phone}

Education:
{college}
Degree: {degree}
Graduation Year: {year}

Skills:
{skills}

Certifications:
{certifications}

Thank you for using Resume Builder!
"""

# Print resume
print(resume)

# Save to file
with open("resume_output.txt", "w") as file:
    file.write(resume)

print("Resume saved as 'resume_output.txt'")
