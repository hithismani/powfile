import os, argparse, shutil

def file_actions(function,file_source,file_dest,ps_file_name):
    if function.lower() == "copy":
        file_dest = os.path.join(file_dest, ps_file_name)
        if os.path.exists(file_dest):
            confirm_delete = input("Profile file already exists in destination directory. Should we still delete? [y/n]")
            if "y" in confirm_delete.lower():
                os.remove(file_dest)
                print("File Removed! Proceeding To Copy.")
        if not os.path.exists(file_dest):    
            shutil.copy(file_source,file_dest)
            print("File Copied. Please restart powershell!")
            print("If you get an error saying '{} cannot be loaded because running scripts is disabled on this system.' Please run the 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser' in an elevated powershell window".format(file_dest))
    elif function.lower() == "remove":
        os.remove(file_dest)
        print("File Removed!")



def run(args):
    ps_file_name = "Microsoft.PowerShell_profile.ps1"
    current_path = os.getcwd()
    if args.replace and args.replace.lower() and args.reset.lower() == "false":
        file_name = "custom-profile.ps1"
        if args.replace.lower() != "true":
            file_name = args.replace
        if os.path.exists(os.path.join(current_path,file_name)):
            print("Custom Profile File Found! Pushing Into Powershell profile folder.")
            if args.profile:
                if os.path.exists(args.profile):
                    print("Custom Profile Path Exists!")
                    file_source = os.path.join(current_path,file_name)
                    file_dest = args.profile
                    file_actions("copy",file_source,file_dest,ps_file_name)
            else:
                if os.path.exists(os.path.join(os.environ['USERPROFILE'],"Documents","WindowsPowerShell")):
                    print("Found %userprofile% path! Copying File.")
                    file_source = os.path.join(current_path,file_name)
                    file_dest = args.profile
                    file_actions("copy",file_source,os.path.join(os.environ['USERPROFILE'],"Documents","WindowsPowerShell"),ps_file_name)

                else:
                    print("Neither custom profile path, nor %userprofile% path exist. Skipping Tasks.")
                    
        else:
            print("Custom Profile File Not Found.")
    if args.reset and args.reset.lower() and args.reset.lower() == "true":
        if args.profile:
            if os.path.exists(os.path.join(args.profile,ps_file_name)):
                file_dest = os.path.join(args.profile,ps_file_name)
                file_actions("remove","",file_dest,"")
        else:
            if os.path.exists(os.path.join(os.environ['USERPROFILE'],"Documents","WindowsPowerShell", ps_file_name)):
                print("Found .ps1 file in powershell path folder.")
                file_dest = os.path.join(os.environ['USERPROFILE'],"Documents","WindowsPowerShell", ps_file_name)
                file_actions("remove","",file_dest,"")

            else:
                print("Cannot find custom profile file to reset. Please confirm paths again.")
        
def main():
    parser=argparse.ArgumentParser(description="powfile")
    parser.add_argument("-replace",help="Enter Custom Profile File Name. Use 'true' if using filename 'custom-profile.ps1'" ,dest="replace", type=str, required=False)
    parser.add_argument("-reset",help="Reset To Normal. (Set to 'True') " ,dest="reset", default="false" ,type=str, required=False)
    parser.add_argument("-profile",help="Enter Custom Location Of Profile Folder. Skip if default location applies.",dest="profile", type=str, required=False)

    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()