# Contributing to [Project Name]

Welcome to `Support Ticket System !!` We're excited to have you contribute to our project.

Before you get started, please take a moment to read through this guide to understand how you can contribute effectively.

## Table of Contents

- [About](#about)

- [Getting Started](#getting-started)

  - [Forking the Repository](#forking-the-repository)

  - [Setting Up Your Environment](#setting-up-your-environment)

- [Contributing Guidelines](#contributing-guidelines)

  - [Branching Strategy](#branching-strategy)

  - [Submitting Pull Requests](#submitting-pull-requests)
  - [Code Review Guidelines](#code-review-guidelines)
  - [Documentation](#documentation)
  - [Testing](#testing)
  - [Issues](#issues)
  - [Commit Message Template](#commit-message-template)
    - [Prefixes for Commit Messages](#prefixes-for-commit-messages)
    - [Committing Jira Issue Solutions](#commit-jira-issue-solution)

- [License](#license)


## About

This is our team's starting point for our git commit messages.

You can edit this template as you like, to customize it.

## Getting Started

### Forking the Repository

1. Navigate to the [Project Repository](https://github.com/ansh-goyal-23/soft-engg-project-jan-2024-se-jan-28).

2. Click on the "Fork" button in the upper right corner to create a copy of the repository in your GitHub account.

### Setting Up Your Environment

1. Clone the forked repository to your local machine:

   ```bash
   git clone https://github.com/ansh-goyal-23/soft-engg-project-jan-2024-se-jan-28.git
   ```

2. Install the dependencies.

   In the terminal, change the directory to `Backend` run the following command :

   ```
   sh local_setup.sh
   ```

3. Follow the setup instructions in the `README.md` file to set up the development environment.

## Contributing Guidelines

### Branching Strategy

We follow a branching strategy based on GitFlow:

- **`main`**: Represents the production-ready code. All changes merged into main are considered stable and ready for release.

- **`develop`**: Represents the ongoing development work. Feature branches are created from develop, and once the feature is complete, it's merged back into develop.

- **`feature`**: Feature branches are created from develop for developing new features. Once a feature is complete, it's merged back into develop.

- **`bugfix`**: Bugfix branches are created from develop to fix bugs found in the development environment. Once the bug is fixed, the branch is merged back into develop.

- **`release`**: Release branches are created from develop when preparing for a new release. Once the release is finalized, it's merged into both main and develop.

- **`hotfix`**: Hotfix branches are created from main to fix critical bugs in the production environment. Once the hotfix is complete, it's merged into both main and develop.

For detailed information on branch naming conventions and usage, refer to the Branching Strategy section.

---

### Submitting Pull Requests

When submitting a pull request, please follow these guidelines:

- Fork the repository and create a new branch based on the branch you want to contribute to.

- Make your changes and ensure the code passes all tests.

- Write clear and descriptive commit messages using the provided `Commit Message Template`.

- Submit a pull request with a `clear title and description` explaining your changes.

---

### Code Review Guidelines

All code changes will undergo code review before merging. Please ensure the following:

- Your code follows the project's coding standards and style guidelines.

- Your code is well-documented, including comments where necessary.

- Your changes do not introduce any new bugs or regressions.

- You have addressed any feedback provided during code review promptly.

---

### Documentation

Contributions to project documentation are highly encouraged.

If you notice any gaps or inaccuracies in the documentation, please `submit a pull request` to improve it.

---

### Testing

All new features and bug fixes should include appropriate tests to ensure they function as intended and do not introduce regressions.

Test coverage is an essential aspect of maintaining code quality.

----

### Issues

If you encounter any bugs, issues, or have feature requests, please submit them via the `Issues` page.

Be sure to provide detailed information to help us understand and address the problem.

----

### Commit Message Template

We use the following commit message template:

```
<prefix>: Summarize the change in less than 50 characters.

Because:
- Explain the reasons you made this change
- Make a new bullet for each reason
- Each line should be under 72 characters

Explain exactly what was done in this commit with more depth than the
50 character subject line. Remember to wrap at 72 characters!

Include any additional notes, relevant links, or co-authors.
```

example instance :

```
refactor: coupon UI

Because:
- The old UI code is fairly slow
- There were a few unused dependencies
- The old UI has aged poorly

I thought it was necessary to remove some of the old coupon UI code.
Unfortunately, it has aged pretty poorly, and I think this refactor makes
the code much easier to support in the long-run. Primarily, this commit
improves the performance of the coupon component. It also removes some
unused dependencies.

These changes should resolve issue #1337.

This commit removed the left-pad dependency, so please stop using it!
```

#### Committing Jira Issue Solutions

When committing changes that resolve a specific issue tracked in Jira, follow this format:

```
[Jira Issue Key] <prefix>: <commit_subject>

<commit_body>

<commit_footer>
```

example instance: 

```
[STS-123] bugfix: Resolve issue with user login

Fixes a bug where users were unable to log in due to incorrect password hashing.

- Updated password hashing algorithm to use bcrypt for increased security
- Fixed issue with authentication middleware not properly validating credentials
```


#### Prefixes for Commit Messages.

- **[feature]**: Use when adding a new feature.

- **[bugfix]**: Use when fixing a bug.

- **[refactor]**: A change that MUST be just refactoring.

- **[reformat]**: A change that MUST be just format, e.g. indent line, trim space, etc.

- **[rephrase]**: A change that MUST be just textual, e.g. edit a comment, doc, etc.

- **[docs]**: Use when updating documentation.

- **[test]**: Use when adding or modifying tests.

- **[style]**: Use when making stylistic changes such as formatting or whitespace.

- **[chore]**: Use for miscellaneous tasks such as updating dependencies or configuration files.

- **[hotfix]**: Use when fixing critical bugs in the production environment.

- **[release]**: Use for version release commits.

----

## License

By contributing to this project, you agree that your contributions will be licensed under the Project License.

