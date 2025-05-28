```
# 📧 AutomaticMailingClient

A simple and effective Python script for sending personalized emails with attachments to multiple recipients using Gmail’s SMTP server.

## 🚀 Features

- ✅ Sends to multiple recipients from a text file
- ✅ Reads subject and message body from external files
- ✅ Appends a custom signature to every email
- ✅ Attaches a file (e.g., resume or PDF)
- ✅ Uses secure SMTP (TLS)
- ✅ Adds a delay between emails to avoid spam detection

## 📂 Project Structure

```

AutomaticMailingClient/
├── main.py                # Main script
├── sender\_email.txt       # Your email address
├── sender\_password.txt    # Your email password or app-specific password
├── receiver\_email.txt     # List of recipient email addresses (one per line)
├── subject\_file.txt       # Email subject
├── email\_body.txt         # Email body content
└── cv.pdf                 # The file to attach (e.g., your resume)

````

## 📄 Requirements

- Python 3.x
- An active Gmail account
- `Allow less secure apps` enabled **OR** use an [App Password](https://support.google.com/accounts/answer/185833) if using 2FA

## ⚙️ How It Works

1. Reads sender credentials and recipients from `.txt` files.
2. Reads the subject and body content from separate files.
3. Appends a predefined signature.
4. Attaches a file (PDF or otherwise).
5. Sends the email to each recipient with a delay to avoid triggering spam filters.

## ✏️ Usage

1. Clone the repository or download the script.

2. Fill the following files:

- `sender_email.txt` – your Gmail address  
- `sender_password.txt` – your Gmail password or App Password  
- `receiver_email.txt` – one email per line  
- `subject_file.txt` – your email subject  
- `email_body.txt` – the body of your email  
- Replace `cv.pdf` with the file you want to attach

3. Run the script:
```bash
python main.py
````

4. Monitor the output for delivery status:

```
✅ Sent to example@example.com
```

## 📌 Important Notes

* Emails are sent in plain text format.
* Each recipient gets a unique email.
* `time.sleep(5)` is added between sends to avoid spam detection.

## 📬 Example

An example `receiver_email.txt`:

```
example1@gmail.com
example2@yahoo.com
example3@outlook.com
```

## 🛡️ Security Tip

Never commit `sender_email.txt` or `sender_password.txt` to a public repository. Use `.gitignore` to exclude them:

```gitignore
sender_email.txt
sender_password.txt
```

## 🧑‍💻 Author

**Ziad Osama**
📧 [ziad.elboshy2001@gmail.com](mailto:ziad.elboshy2001@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/ziad-el-boshy/) | [GitHub](https://github.com/ZiadDyno)

---

Feel free to modify and customize this tool to suit your emailing needs.
