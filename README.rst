=======
powfile
=======


.. image:: https://img.shields.io/pypi/v/powfile.svg
        :target: https://pypi.python.org/pypi/powfile



A quick script to help you switch up powershell profile files, and reset them back to normal.

Why
---

- I use different $profile settings when I'm doing screencasts/live demos, and a different one for script and project development.
- Becomes too taxing to keep switching profile settings, especially when each project I use may come with it's own settings. 

Features
--------

- Incredibly Simple CLI script. Just specify the file (.ps1) you're looking to place in your profile folder, and the script would take care of the rest.
- Warns you before you overwrite an existing file.
- Let's you reset everything back to 'normal' (no profile files) if you'd like to have them go back to normal.
- Simply uses 'os', 'argparse', 'shutil' libraries.

How To Use
----------

- cd into your project directory.
- create a 'custom-profile.ps1' file with the required settings you're looking for.
- run 'powfile -replace true' to let the script work.

Options
--------

- `replace`: Replacement file that exists in current folder, to be copied into the powershell folder.
- `reset` : Reset file back to default. `true`
- `profile` : Custom powershell profile path, if you're using a path that's not %userprofile%/Documents/WindowsPowerShell.

Credits
-------

- This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage



