# Contributing

`Thank you for your interest in contributing to this project!` Your help is greatly appreciated. By participating in this project, you agree to abide by our code of conduct.

## 🙏 Special Thanks to Scapy Project 🙏

This project stands on the shoulders of dedicated work and collaborative spirit. A heartfelt **thank to** to the scapy library that is fundamental to our ICMP reachability checks. 

## How to Contribute

Your contributions are essential! Here are several ways you can help:

### 🐛 Reporting Bugs

If you find a bug or unexpected behavior, please let us know!
1.  **Check existing issues**: Before creating a new issue, please check the project's issue tracker to see if the bug has already been reported.
2.  **Open a new issue**: If it's a new bug, create a new issue and include:
    * A clear and concise description of the bug.
    * Steps to reproduce the behavior.
    * Expected behavior vs. actual behavior.
    * Any relevant error messages or logs.
    * Your operating system and Python version.

### ✨ Suggesting Enhancements

Have an idea for a new feature or an improvement to existing functionality?
1.  **Check existing issues/feature requests**: See if your idea has already been discussed.
2.  **Open a new issue**: Describe your suggestion clearly, explaining:
    * The problem it solves or the benefit it provides.
    * How you envision the feature working.
    * Any potential challenges or considerations.

### 💻 Code Contributions

We encourage code contributions! If you'd like to submit code, please follow these steps:

1.  **Fork the repository**: Create a fork of this project on GitLab.
2.  **Create a new branch**: Always work on a new branch for your changes. Use a descriptive branch name (e.g., `feature/add-new-alert-type`, `fix/email-sending-issue`).
3.  **Implement your changes**:
    * Ensure your code adheres to Python's [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).
    * Add comments where necessary, especially for complex logic.
    * Ensure your changes align with the existing code structure and practices.
4.  **Test your changes**: Before submitting, thoroughly test your code to ensure it works as expected and doesn't introduce new bugs. Include details on how you tested your changes in your merge request description.
5.  **Write clear commit messages**:
    * Start with a brief summary (under 50 characters) of the change.
    * Follow with a more detailed explanation if needed, describing *why* the change was made and *how* it addresses the issue/feature.
    * Reference the relevant issue number (e.g., `Fix #123`, `Closes #456`, `Resolves #789`).
6.  **Push your branch**: Push your new branch to your forked repository.
7.  **Create a Merge Request (MR)**: Open a Merge Request from your branch to the `main` branch of the original repository.
    * Provide a clear and concise description of your changes in the MR description.
    * Reference any related issues.
    * Request reviews from relevant team members.

## Code Style and Best Practices

* **Pythonic Code**: Strive for clean, readable, and Pythonic code.
* **Error Handling**: Implement robust `try-except` blocks for file operations, API calls, and other potentially problematic areas.
* **Logging**: Use Python's `logging` module for debug, info, warning, and error messages, rather than just `print()`, for better operational visibility. (Consider this for future improvements if not fully implemented).
* **Security**: Be mindful of security best practices, especially when handling credentials (ensure they are managed securely and not hardcoded).

## Contact

1. Author
Jose Rafael Guerra - joserafaelguerra85@gmail.com

---

Thank you for helping make this project better!
