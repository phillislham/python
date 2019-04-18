import os
from pprint import pprint
from datetime import datetime

class ComponentLog():
    """
    theframework/components/component_log.py
    """
    DS = os.sep
    DIR = os.getcwd()

    strnow = datetime.now().strftime("%Y%m%d")
    pathfolder = ""
    strsubtype = ""
    strfilename = ""

    path_ofthis = os.path.realpath(__file__)
    path_thisdir = os.path.dirname(path_ofthis)
    path_json = os.path.join(path_thisdir,"dsources.json")
    data = {}

    def __init__(self, strsubtype = "", pathfolder = ""):
        self.pathfolder = pathfolder
        self.strsubtype = strsubtype
        self.strfilename = "app_"+self.strnow+".log"

        if not pathfolder:
            self.pathfolder = self.DIR

        if not strsubtype:
            self.strsubtype = "debug"

        self.__fix_folder()
    
    
    def __fix_folder(self):
        pathlogfolder = os.path.join(self.pathfolder,self.strsubtype)
        if not os.path.isdir(pathlogfolder):
            os.mkdir(pathlogfolder)    

    
    def __get_now(self):
        strnow = (datetime.now()).strftime("%Y%m%d-%H%M%S")
        # strnow = datetime.datetime.strptime(data[4]+data[5],"%H:%M:%S")
        return strnow
    
    def __obj_tostr(self,obj):
        if str(type(obj)) == "<type 'classobj'>":
            import inspect
            return 
            
        
        #for name, val in vars(obj):
            #print '  .%s: %r' % (name, val)

    def save(self, mxvar, strtitle=""):
        pathfile = os.path.join(
                        self.pathfolder,
                        self.strsubtype,
                        self.strfilename)
        strnow = self.__get_now()
        #pprint( type(mxvar))
        #print(dir(mxvar))
        ##pprint(mxvar.__type__)
        
        strcontent = "-- [{}]\n".format(strnow)
        if strtitle:
            strcontent += strtitle+":\n"
        
        if isinstance(mxvar,str):
            strcontent += mxvar+"\n\n"
        else:
            from inspect import getmembers
            strcontent += str(getmembers(mxvar)).replace("), (","),\n(")+"\n\n"
            
#        if type(mxvar) in (str, int, float, bool, None):
#            strcontent += str(mxvar)+"\n\n"
#        
#        if str(type(mxvar)) == "<type 'classobj'>":
#            strcontent += type(mxvar)+"->"+str(vars(mxvar))+"\n\n"
            
        f = open(pathfile,"a")
        f.write(strcontent)
        f.close()


if __name__ == "__main__":
    o = ComponentLog()
    o.write()