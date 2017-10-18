#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import hashlib
import random
import subprocess
import shutil

def deploy() :

    print(len(sys.argv))

    if len(sys.argv) < 3:
        print('empty profile or lambda-function-name')
        raise Exception

    filename = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()

    target_dir =  "/usr/src/app"
    profile = sys.argv[1]
    lambda_function_name = sys.argv[2]


    for root,dirs,files in os.walk("{}/lambda-function/".format(target_dir)):

        for file in files:
            src_file = "{}/lambda-function/{}".format(target_dir,file)
            dst_file = "{}/{}".format(target_dir,file)
            results = subprocess.call("python -m py_compile {}".format(src_file), shell=True)
            if results :
                print(src_file)
                print(results)
                raise Exception
            shutil.rmtree("{}/lambda-function/__pycache__".format(target_dir))
            shutil.copyfile(src_file,dst_file)
            print("COPY {}".format(src_file))

        print("deploy? plz input 'y'")
        yes = input()

        if not yes == "y":
            raise Exception

        #compress
        print(subprocess.call("zip -r /tmp/{0}.zip ./* -x {1}/lambda-funciton {1}/script {1}/__pycache__".format(filename,target_dir), shell=True))

        #fire
        print(subprocess.call("aws lambda update-function-code --profile {} --function-name {} --zip-file fileb:///tmp/{}.zip --publish".format(profile,lambda_function_name,filename), shell=True))

        print("DONE :D")


if __name__ == "__main__" : deploy()


