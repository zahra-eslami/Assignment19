
# Password Generator

The Password Generator is a simple application built with Python using the PySide6 library. It allows users to generate random passwords with customizable options.

<center>
<img src="pics\Password_Generator.png" width="400" height="300" />
</center>

---

## Installation

Ensure you have Python installed on your system. You can install PySide6 using pip:

```
pip install PySide6
```
---

## Usage:

1. Run the program by executing the following command:
```
python PassGenerator_main.py
```
2. The application window will open with password generation options.
3. Customize your password by selecting the following options:
    - Length Slider: Adjust the length of the password using the slider.
    - Include Uppercase: Check this box to include uppercase letters in the password.
    - Include Lowercase: Check this box to include lowercase letters in the password.
    -  Include Numbers: Check this box to include numbers in the password.
    - Include Special Characters: Check this box to include special characters in the password.
4. As you make selections, a random password will be generated and displayed in the text field.
5. The strength of the generated password is indicated below the text field, based on the complexity of the password.
Click the "Copy" button to copy the generated password to the clipboard.

---
## Password Strength Criteria
- **Weak**: Passwords generated with only one type of character set (e.g., only lowercase letters, only numbers, etc.) or a combination of lowercase letters and numbers.

- **Average**: Passwords generated with a combination of two character sets (e.g., lowercase letters and numbers, uppercase letters and special characters, etc.).

- **Strong**: Passwords generated with a combination of at least three character sets (e.g., lowercase letters, uppercase letters, numbers, and special characters).
---

[Watch App Video](pics/Password_Generator.mp4)

---
### Credits

Designer: Zahra Eslami