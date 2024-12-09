:html_theme.sidebar_secondary.remove:

Update package
==============

.. note::

    You can get the same information by running the "template update check" action
    From your pypackage based repository.

Whenever the version of your pypackage template is outdate, you can update it by following these steps:

#.  create an "update-template" branch to avoid creating conflict.

#.  Run the following code in your project directory to update the template:

    .. code-block:: console

        copier update --trust --defaults --vcs-ref <latest pypackage version>


    .. note::

        You may need to reinstall ``copier`` and ``jinja2-time`` if they are not available in your environment.


#. After solving the merging issues you can push back the changes to your main branch.