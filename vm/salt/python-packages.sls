packages:
    pkg.installed:
        - names:
            - python-pip
            - python3-pip


pip_packages:
    pip.installed:
        - bin_env: '/usr/bin/pip3'
        - requirements: salt://requirements.txt