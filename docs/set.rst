Link Existing repository
========================

#. Create a new branch called "link-to-template".

#.  Clone your existing repository in a local machine and checkout the "link-to-template":

    .. code-block:: console

        git clone <your repostory>
        cd <your_repository>
        git checkout link-to-template

#.  Change the name of the folder to "<your_repository>_legacy"

    .. code-block:: console

        mv -r <your repository> <your repository>_legacy

#.  Create a local repository using copier as if it was the first you created your lib:

    .. code-block:: console

        copier copy --trust gh:12rambau/pypackage <python-project>

#.  Once done copy the `.git` folder from the legacy repository to the new one

    .. code-block:: console

        cp -r <your repository>_template/.git <your repository>/.git

#.  Now both repositories are synchronized.
    You can make a first commit called "build: linked to pypackage copier template" and check the diff with the existing state of your repository.
    This can be performed either locally or by pushing to your distant branch.

#.  Finally try as much as possible to restore all the component of your old lib into the new one and commit the result.
    It's a tedious effort that will be more complicated if the structure of your package is far away from the copier template.
    It's easier if your initial library was created using the previous cookiecutter based version of pypackage.
