# -*- coding: utf-8 -*-

from setuptools import setup

def main():
    
    setup(
        name='simple-aws-lambda-deploy',
        version='0.1.1',
        zip_safe=False,
        entry_points={
            "console_scripts": [
                "simple-lambda-deploy=script.deploy:deploy",
                ],
            },
    )


if __name__ == '__main__':
    main()
