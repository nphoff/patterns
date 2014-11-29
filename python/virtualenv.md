Virtualenv:
---

Everything I would like to remember about virtualenv. (hopefully.)
Installing:

    pip install virtualenv

Running:

    virtualenv ./venv

Use --no-site-packages to not include packages that are included globally (this is default in v 1.7+.  This should make this not an issue, because currently pip install virtualenv will get v 1.11+) 

Will start a virtualenv directory in ./venv.  You can specify a specific python to use with:

    virtualenv -p /path/to/python/python2.7 ./venv

To activate:

    source ./venv/bin/activate

To deactivate: (will get put in your $PATH)

    deactivate
    
To install requests:

    pip install requests

To delete a virtualenv, you can delete it's folder.

To get a list of requirements, do:

    pip freeze > reqs.txt

And to install from a file like that:

    pip install -r reqs.txt
