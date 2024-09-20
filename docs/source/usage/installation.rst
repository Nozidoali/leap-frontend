.. _installation-guide:

==========================
Installation Instructions
==========================

This guide will help you install the required dependencies and set up the environment for your project.

.. contents:: Table of Contents
   :local:
   :depth: 2

System Requirements
--------------------

Before installing the package, ensure your system meets the following requirements:

- Python 3.7 or higher
- pip (Python package installer)

Installing with `pip`
----------------------

To install the package using `pip`, run the following command:

.. code-block:: bash

   pip install leap-frontend

This will install the latest version of the package from the Python Package Index (PyPI).

Installing from Source
----------------------

If you prefer to install the package from the source code, follow these steps:

1. Clone the repository from GitHub:

   .. code-block:: bash

      git clone https://github.com/nozidoali/leap-frontend.git

2. Navigate to the project directory:

   .. code-block:: bash

      cd leap-frontend

3. Install the package using `pip`:

   .. code-block:: bash

      pip install .

Alternatively, you can install it in "editable" mode for development:

.. code-block:: bash

   pip install -e .

Using a Virtual Environment (Recommended)
------------------------------------------

It is recommended to use a virtual environment to manage dependencies and isolate your project environment.

1. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv

2. Activate the virtual environment:

   - On macOS/Linux:

     .. code-block:: bash

        source venv/bin/activate

   - On Windows:

     .. code-block:: bash

        venv\Scripts\activate

3. Install the package and dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

Installing Development Dependencies
------------------------------------

If you're contributing to the project or need to run tests, you should install development dependencies:

.. code-block:: bash

   pip install -r requirements-dev.txt

You can now run the test suite with:

.. code-block:: bash

   pytest

Updating Dependencies
----------------------

To update the package to the latest version, use the following command:

.. code-block:: bash

   pip install --upgrade leap-frontend

