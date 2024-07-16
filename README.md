##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
**Higher-lower**  is a simple web-based number guessing game built using Flask, a lightweight web framework for Python. The game randomly selects a number between 0 and 9, and the user has to guess the number by entering it in the URL. The application provides feedback on whether the guess is too low, too high, or correct.

## 📝 How to Build
**Prerequisites**
  - Python 3.x
  - Flask

**To build the project follow these steps:**
  - **installation:**

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/Higher-lower.git
cd Higher-lower       

# Install the required package
pip install Flask 
```
  - **Running the application:**
      - The application will start running on http://127.0.0.1:5000/.
      - Open this URL in your web browser to start playing the game.
        
  - **Documentation:**
       - Flask: https://flask.palletsprojects.com/en/3.0.x/
       - Python: https://www.python.org/doc/
   
## 📄 Code Explanation
  - The root route (/) provides instructions to the user to guess a number within this range, accompanied by an image. A dynamic route ('/<int:guess>') is defined to check the user's guess, providing feedback on whether the guess is too low, too high, or correct, each with a corresponding image. Additionally, the code includes a decorator make_bold to bold the text returned by any function it wraps, although this decorator is not used in the current implementation.

## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Higher-Lower project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Higher-Lower project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
