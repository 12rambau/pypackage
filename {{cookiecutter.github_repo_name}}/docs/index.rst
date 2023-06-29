:html_theme.sidebar_secondary.remove:

{% set project_name_length = cookiecutter.project_name | length %}
{{ cookiecutter.project_name }}
{{ "=" * project_name_length }}

.. toctree::
   :hidden:

   usage
   contribute

Documentation contents
----------------------

The documentation contains 3 main sections:

.. grid:: 1 2 3 3

   .. grid-item::

      .. card:: Usage
         :link: usage.html

         Usage and installation

   .. grid-item::

      .. card:: Contribute
         :link: contribute.html

         Help us improve the lib.

   .. grid-item::

      .. card:: API
         :link: api/modules.html

         Discover the lib API.
