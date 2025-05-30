# 📧 Automatic Mailing Client V2

Automatic Mailing Client V2 is a Python GUI application that allows you to send bulk emails with or without customized subjects and bodies, using a CSV file. The app is designed for ease of use, reliability, and personalization. It also remembers your last used signature between runs.

---

## 📂 Project Structure

```

Automatic-Mailing-Client-V2/
│
├── Samples CSV files/
│   ├── emails\_only.csv                 # Contains email addresses only
│   └── emails\_subject\_body.csv        # Contains emails, subjects, and body texts
│
├── Screenshots/
│   └── gui.png
│
├── src/
│   ├── gui.py                         # Main GUI application
│   ├── emailer.py                     # Core logic for sending emails
│   ├── main.py                        # Main function "The file you run"
│
├── last\_signature.txt                # Stores the last used signature for auto-loading
│
└── README.md                          # Project documentation

````

---

## 🚀 Features

- 📬 Bulk email sending with Gmail
- 🧠 Remembers the last signature used
- 📎 Attaches a common CV (PDF) file to each email
- ✅ Email validation before sending
- 🧾 Two modes:
  - **Common Subject/Body Mode** (uses a shared subject and message for all recipients)
  - **Custom Subject/Body Mode** (CSV provides per-recipient subjects and messages)

---

## 🛠️ Setup Instructions

### 1. ✅ Requirements

Make sure you have Python 3 installed. Then install the required libraries:

```bash
pip install customtkinter
```

---

### 2. 📁 Prepare Your Files

#### ✅ `emails_only.csv`

CSV file with only emails (for shared subject/body mode):

```csv
email
example1@gmail.com
example2@gmail.com
```

#### ✅ `emails_subject_body.csv`

CSV file with email, subject, and body per recipient:

```csv
email,subject,body
example1@gmail.com,Hello,This is a custom message.
example2@gmail.com,Greetings,This is another message.
```

#### ✅ CV Attachment

Ensure you have a `CV.pdf` file to attach, or specify its path in the GUI.

---

## 🧑‍💻 How to Use

1. **Run the app:**

```bash
cd src
python main.py
```

2. **GUI Overview:**

* 🔐 **Sender Gmail & Password**: Required to authenticate (use App Passwords).
* 📁 **Select CSV File**: Choose either `emails_only.csv` or `emails_subject_body.csv`.
* 📎 **Attach CV**: Browse and select a CV (PDF) to attach to all emails.
* 🧾 **Signature**: Customize your sign-off; it's saved automatically on app close.
* 🔘 **Mode**:

  * **Common Mode**: Provide one subject/body for all emails.
  * **Custom Mode**: Subject/body taken from each row in CSV.
* 🚀 **Send Emails**: Starts the bulk sending process with a delay between each to avoid spam flags.

---

## 🔐 Gmail Setup (Required!)

Since Gmail blocks less secure apps:

1. Enable **2-Step Verification**: [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Generate an **App Password**:

   * Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   * Choose **Mail** > **Windows Computer** (or any device name)
   * Copy the 16-character app password
3. Use this App Password instead of your Gmail login password in the app

---

## 📝 Signature Memory

Your last used signature is automatically saved to:

```
last_signature.txt
```

On each program launch, this file is read to pre-fill the signature box. You can manually edit the file if needed.

---

## ❗ Notes

* ⏳ A 2-second delay is added between emails to reduce the chance of being flagged as spam.
* ✅ Email addresses are validated before sending.
* 💥 Errors during sending (e.g., invalid emails) will be reported in the console.

---

## 📷 Screenshots

Here's what the Automatic Mailing Client V2 looks like in action:

![Mailing Client GUI](screenshots/gui.png)

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 🧾 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Ziad — [LinkedIn](https://www.linkedin.com/in/ziad-el-boshy/) • [GitHub](https://github.com/ZiadDyno)

```
