# NestJS Project Template

This repository is a Cookiecutter template designed to quickly generate a base project structure for NestJS applications. It helps streamline the setup process by providing predefined configuration settings, folder structures, and boilerplate code.

## Overview

The template uses [Cookiecutter](https://cookiecutter.readthedocs.io/) to generate a project with a consistent structure and some initial defaults for rapid development with NestJS. The base configuration includes essential files like a custom `.gitignore`, project directory, and template hooks for additional automation.

## Features

- **Standardized Project Structure:** Automatically generate a well-organized NestJS project directory.
- **Customizable Options:** Easily set the project name, version, description, license, and more through Cookiecutter variables.
- **Hooks Support:** Includes hook scripts (if necessary) to run commands before or after project generation.
- **Out-of-the-box Configuration:** Predefined settings to help start your development immediately.

## Prerequisites

- **Python:** Make sure you have Python installed since Cookiecutter is a Python package.
- **Cookiecutter:** Install Cookiecutter globally using pip:

  ```bash
  pip install cookiecutter
  ```

## Getting Started

To create a new NestJS project using this template, run the following command in your terminal:

```bash
cookiecutter https://github.com/isma90/template-nestjs
```

After running the command, you will be prompted to enter some template variables. Below is a list of the available variables and their default values:

- **author_name:** "Ismael Leiva"
- **description:** "A NestJS project template"
- **license:** "MIT"
- **project_name:** "My NestJS Project"
- **project_slug:** This value is derived by converting the `project_name` to lowercase and replacing spaces with underscores.
- **version:** "0.1.0"

In addition, the template also specifies that files under the `deploy/definition.yaml` folder (or file) should be copied without rendering, preserving their original content.

## Template Folder Structure

Once generated, the structure of your new NestJS project will resemble the following:

```
.
├── .gitignore
├── hooks/                # Contains pre- or post-generation hooks (if defined)
├── <project_slug>/       # Main project directory (name derived from your project name)
│   ├── ...               # Your NestJS code and configuration files
└── cookiecutter.json     # Template configuration file
```

- **hooks/**  
  This folder may include scripts to be executed before or after the project is generated. They are useful for automating additional setup tasks.

- **<project_slug>/**  
  This folder is generated based on the input provided for `project_name` and includes the boilerplate code and configuration for your NestJS project.

- **.gitignore**  
  A template for ignoring files and directories that should not be tracked in your version control system.

- **cookiecutter.json**  
  The core configuration file that defines the default variables and options available for the template.

## Customization

Feel free to modify and extend the template to match your project’s best practices and specific requirements. Adjust the folder structure, add new variables, or include additional configuration files as needed.

## License

This template is distributed under the [MIT License](https://opensource.org/license/mit).

## About the Author

- **Ismael Leiva**  
  The template is authored by Ismael Leiva. For updates or to contribute, please check out the repository.

## Contributing

Contributions and improvements are welcome. If you have suggestions or find any issues, please open an issue or submit a pull request to help improve the template.

---

This README provides a detailed overview of the repository and instructs users on how to utilize the Cookiecutter template to generate a base NestJS project.