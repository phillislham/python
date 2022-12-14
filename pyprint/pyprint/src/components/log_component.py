import os
import socket
from datetime import datetime
import sys, pprint

class LogComponent:

    def __init__(self, subtype: str="", pathfolder:str=""):
        self.__subtype = subtype if subtype else "debug"
        self.__pathfolder = self.__get_pathfolder(pathfolder)
        today = self.__get_today()
        self.__filename = f"app_{today}.log"
        self.__fix_folder()

    def __get_pathfolder(self, pathfolder: str):
        if pathfolder:
            return pathfolder
        pathfolder = os.path.dirname(os.path.realpath(__file__))
        return pathfolder

    def __get_today(self):
        today = datetime.today()
        return today.strftime("%Y%m%d")

    def __get_now(self):
        now = datetime.today()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def __get_fix_folder(self):
        return f"{self.__pathfolder}/{self.__subtype}/"
    
    def __is_fix_folder(self):
        logfolder = self.__get_fix_folder()
        return os.path.isdir(logfolder)

    def __fix_folder(self):
        if not self.__is_fix_folder():
            try:
                os.mkdir(self.__get_fix_folder(), 0o777)
            except:
                e = sys.exc_info()[0]
                folder = self.__get_fix_folder()
                print(f"fix_folder error: {e} creating {folder}")
            

    def __var_export(self, obj, resource) :
        temp = sys.stdout             # store original stdout object for later
        sys.stdout = resource
        pprint.pprint(obj)
        sys.stdout.close()
        sys.stdout = temp             # restore print commands to interactive prompt
        #return open(pathfile, 'r').read()

    def __get_resource(self):
        pathfile = f"{self.__pathfolder}/{self.__subtype}/{self.__filename}"
        isfile = os.path.isfile(pathfile)
        if isfile:
            resource = open(pathfile, "a")
        else:
            resource = open(pathfile, "w")
        return resource

    def __get_remote_ip(self):
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

    def save(self, mxvar, title:str=""):
        if not self.__is_fix_folder():
            return False

        logresource = self.__get_resource()
        if not logresource:
            return False

        if logresource.mode == "a":
            logresource.write("\n\n")

        headline = f"-- [{self.__get_now()} - ip:{self.__get_remote_ip()}]\n"
        logresource.write(headline)
        if title:
            logresource.write(f"{title}:\n")

        if not isinstance(mxvar, str):
            self.__var_export(mxvar, logresource)
        else:
            logresource.write(mxvar)
        logresource.close()

        return True
