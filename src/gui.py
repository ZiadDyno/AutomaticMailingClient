import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import emailer
import os

class EmailGUI:
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.title("Automatic Mailing Client")
        self.root.geometry("500x1000")

        # Variables
        self.mode = ctk.StringVar(value="bulk")
        self.csv_path = None
        self.cv_path = None

        # --- Frames ---
        file_frame = ctk.CTkFrame(self.root)
        file_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        mode_frame = ctk.CTkFrame(self.root)
        mode_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        sender_frame = ctk.CTkFrame(self.root)
        sender_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        subject_body_frame = ctk.CTkFrame(self.root)
        subject_body_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        action_frame = ctk.CTkFrame(self.root)
        action_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # --- File Picker and Labels (side by side) ---
        self.csv_label = ctk.CTkLabel(file_frame, text="")
        self.csv_label.grid(row=0, column=0, padx=5, sticky="w")
        self.csv_button = ctk.CTkButton(file_frame, text="Choose CSV", command=self.choose_csv)
        self.csv_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.cv_label = ctk.CTkLabel(file_frame, text="")
        self.cv_label.grid(row=0, column=1, padx=5, sticky="w")
        self.cv_button = ctk.CTkButton(file_frame, text="Choose CV", command=self.choose_cv)
        self.cv_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        file_frame.columnconfigure(0, weight=1)
        file_frame.columnconfigure(1, weight=1)

        # --- Mode Radio Buttons (side by side) ---
        self.custom_radio = ctk.CTkRadioButton(mode_frame, text="Send Custom Emails", variable=self.mode, value="custom", command=self.toggle_fields)
        self.custom_radio.grid(row=0, column=0, padx=10, pady=5)
        self.bulk_radio = ctk.CTkRadioButton(mode_frame, text="Send Bulk Emails", variable=self.mode, value="bulk", command=self.toggle_fields)
        self.bulk_radio.grid(row=0, column=1, padx=10, pady=5)

        # --- Sender Email and Password ---
        self.email_entry = ctk.CTkEntry(sender_frame, placeholder_text="Sender Email \"Currently only Gmails work\"")
        self.email_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.password_entry = ctk.CTkEntry(sender_frame, placeholder_text="Sender Password \"Notice: use App Password for Guaranteed Functionality\"", show="*")
        self.password_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        subject_body_sig_frame = ctk.CTkFrame(self.root)
        subject_body_sig_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        # Allow full-width stretching
        sender_frame.columnconfigure(0, weight=1)

        #Subject stays full width at top
        self.subject_entry = ctk.CTkEntry(subject_body_sig_frame, placeholder_text="Enter Subject")
        self.subject_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Body Label and Textbox (left)
        self.body_label = ctk.CTkLabel(subject_body_sig_frame, text="Body:")
        self.body_label.grid(row=1, column=0, padx=5, pady=(10,0), sticky="w")
        self.body_textbox = ctk.CTkTextbox(subject_body_sig_frame, height=150)
        self.body_textbox.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Signature Label and Textbox (right)
        self.signature_label = ctk.CTkLabel(subject_body_sig_frame, text="Signature:")
        self.signature_label.grid(row=1, column=1, padx=5, pady=(10,0), sticky="w")
        self.signature_textbox = ctk.CTkTextbox(subject_body_sig_frame, height=150)
        self.signature_textbox.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        subject_body_sig_frame.columnconfigure(0, weight=3)
        subject_body_sig_frame.columnconfigure(1, weight=1)
        subject_body_sig_frame.rowconfigure(2, weight=1)

        subject_body_frame.columnconfigure(0, weight=1)

        # --- Send Button ---
        self.send_button = ctk.CTkButton(action_frame, text="Send Emails", command=self.send_emails)
        self.send_button.grid(row=0, column=0, pady=10)

        # --- Status Log ---
        self.status_log = ctk.CTkTextbox(self.root, height=100)
        self.status_log.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        self.status_log.configure(state="disabled")  # <-- Make it read-only initially
        
        self.root.columnconfigure(0, weight=1)
        
        if os.path.exists("last_signature.txt"):
            try:
                with open("last_signature.txt", "r", encoding="utf-8") as f:
                    signature = f.read()
                    self.signature_textbox.insert("1.0", signature)
            except Exception as e:
                print(f"Failed to load signature: {e}")
                
        
        # Initialize fields visibility
        self.toggle_fields()
        self.root.mainloop()

    def is_gmail_address(self, email: str) -> bool:
        return email.lower().endswith("@gmail.com") or email.lower().endswith("@googlemail.com")

    def choose_csv(self):
        self.csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.csv_path:
            self.csv_label.configure(text=f"📄 {self.csv_path.split('/')[-1]}")

    def choose_cv(self):
        self.cv_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.cv_path:
            self.cv_label.configure(text=f"📎 {self.cv_path.split('/')[-1]}")

    def toggle_fields(self):
        if self.mode.get() == "custom":
            self.subject_entry.grid_remove()
            self.body_label.grid_remove()
            self.body_textbox.grid_remove()
            self.subject_entry.configure(state="disable")
            self.body_textbox.configure(state="disable")
        else:
            self.subject_entry.grid()
            self.body_label.grid()
            self.body_textbox.grid()
            self.subject_entry.configure(state="normal")
            self.body_textbox.configure(state="normal")

    def send_emails(self):
        if self.csv_path and self.cv_path:
            sender_email = self.email_entry.get().strip()
            
            #! Validating that the sender email is a google mail
            if not self.is_gmail_address(sender_email):
                messagebox.showerror("Invalid Email", "Please enter a valid Gmail address as the sender.")
                self.log_status("❌ Sender email must be a Gmail address.\n")
                return
            
            sender_password = self.password_entry.get().strip()
            signature = self.signature_textbox.get("1.0", "end").strip()
            
            self.log_status(f"📤 Sending emails...\n")

            if self.mode.get() == "custom":
                if not all([sender_email, sender_password, self.csv_path, self.cv_path, signature]):
                    messagebox.showerror("Missing Fields", "❌ Please fill in all fields.")
                    self.log_status(f"❌ Missing Fields...\n")
                    return

                threading.Thread(target=self.run_send_custom, args=(sender_email, sender_password, signature), daemon=True).start()
            else:
                subject = self.subject_entry.get().strip()
                body = self.body_textbox.get("1.0", "end").strip()
                if not all([sender_email, sender_password, self.csv_path, self.cv_path, signature, subject, body]):
                    messagebox.showerror("Missing Fields", "❌ Please fill in all fields.")
                    self.log_status(f"❌ Missing Fields...\n")
                    return

                threading.Thread(target=self.run_send_bulk, args=(sender_email, sender_password, signature, subject, body), daemon=True).start()
        else:
            messagebox.showerror("Missing Files", "❌ Please select the required files.")

    def run_send_custom(self, sender_email, sender_password, signature):
        try:
            self.send_button.configure(state="disabled")
            self.csv_button.configure(state="disabled")
            self.cv_button.configure(state="disabled")
            results = emailer.send_emails(
                mode="custom",
                csv_path=self.csv_path,
                cv_path=self.cv_path,
                sender_email=sender_email,
                sender_password=sender_password,
                signature=signature
            )

            for email, success in results:
                if success:
                    self.log_status(f"✅ Sent to {email}\n")
                else:
                    self.log_status(f"❌ Failed to send to {email}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.send_button.configure(state="normal")
            self.csv_button.configure(state="normal")
            self.cv_button.configure(state="normal")
            self.save_signature(signature)

    def run_send_bulk(self, sender_email, sender_password, signature, subject, body):
        try:
            self.send_button.configure(state="disabled")
            self.csv_button.configure(state="disabled")
            self.cv_button.configure(state="disabled")
            results = emailer.send_emails(
                mode="bulk",
                csv_path=self.csv_path,
                cv_path=self.cv_path,
                sender_email=sender_email,
                sender_password=sender_password,
                signature=signature,
                subject=subject,
                body=body
            )

            for email, success in results:
                if success:
                    self.log_status(f"✅ Sent to {email}\n")
                else:
                    self.log_status(f"❌ Failed to send to {email}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.send_button.configure(state="normal")
            self.csv_button.configure(state="normal")
            self.cv_button.configure(state="normal")
            self.save_signature(signature)

    def log_status(self, message):
        self.status_log.configure(state="normal")
        self.status_log.insert("end", message + "\n")
        self.status_log.see("end")
        self.status_log.configure(state="disabled")
        
    def save_signature(self, signature):
        try:
            with open("last_signature.txt", "w", encoding="utf-8") as f:
                f.write(signature)
        except Exception as e:
            print(f"Failed to save signature: {e}")



if __name__ == "__main__":
    EmailGUI()