import argparse
import sys
import os
import json


def doPrint(*args, **kwargs):
    icon = kwargs.get('icon', '\u25B6')
    print(str(icon), *args, '\n', sep=' ')


def print_welcome(args):
    icon = '\u2BFB'
    text = f"Creating new project {args.name} as an {args.mode.upper()} {args.type}"
    print('\n')
    print(icon*20, text, icon*20, sep=' ', end='\n\n')


def prep_parser():
    parser = argparse.ArgumentParser(
        prog='Initiate a new typescript Vue project based on firebase',
        description='Scaffold a new typescript Vue project based on firebase',
        epilog='Text at the bottom of help')
    # positional argument
    parser.add_argument('name', help="The name of the project. This will be the name of the folder too.")
    # option that takes a value
    parser.add_argument('-t', '--type', help="The type of the project (app, site).")
    parser.add_argument('-m', '--mode', help="The mode of the project (SPA, SSR).")
    parser.add_argument('-r', '--rootdir', help="The root directory where the project should be initiated.")
    return parser


def validate_args(args):
    
    
    if args.rootdir:
        if not os.path.isdir(args.rootdir):
            print("Error: invalid root directory. The directory does not exist.")
            sys.exit(1)
        else:
            args.rootdir = os.path.realpath(args.rootdir)
    else:
        args.rootdir = os.getcwd()

    type_options = ('site', 'app')
    if args.type:
        if args.type not in type_options:
            print("Error: invalid type. Options for type are: " +
                  ", ".join(type_options) + ".")
            sys.exit(1)
    else:
        print('Setting type to default: site.')
        args.type = 'site'

    mode_options = ('ssr', 'spa')
    if args.mode:
        if args.mode not in mode_options:
            print("Error: invalid type. Options for type are: " +
                  ", ".join(mode_options) + ".")
            sys.exit(1)
    else:
        print('Setting type to default: spa.')
        args.mode = 'spa'

    args.script_dir = os.path.dirname(os.path.realpath(__file__))
    return args


def create_vite_project(args):
    doPrint("Creating vite project")

    os.chdir(args.rootdir)
    os.system("yarn create vite " + args.name +
              " --template vue-ts > /dev/null 2>&1")
    os.chdir(args.rootdir + '/' + args.name)
    os.system("yarn > /dev/null 2>&1")
    os.chdir(args.script_dir)


def install_dependencies(args):
    doPrint("Installing dependencies")

    os.chdir(args.rootdir + '/' + args.name)
    # Defining needed dependencies
    dev_packages = {
        "common": ("postcss@^8.1.0", "tailwindcss", "postcss", "autoprefixer", "@types/uuid"),
        "site":(),
        "app":(),
        "ssr": (),
        "spa": (),
    }
    packages = {
        "ssr": ("vite-ssr", "@vueuse/head", "@nuxt/devalue"),
        "site":(),
        "app":(),
        "spa": (),
        "common": ("vue@3", "vue-router@4", "@headlessui/vue", "@heroicons/vue", "@tiptap/core", "@tiptap/extension-underline", "@tiptap/pm", "@tiptap/starter-kit", "@tiptap/vue-3", "firebase", "pinia", "uuid", "vue-heroicons", "@vueuse/core", "@tailwindcss/forms")
    }
    # Installing dependencies
    os.system("yarn add -D " +" ".join(dev_packages["common"]) + "> /dev/null 2>&1")
    os.system("yarn add -D " +" ".join(dev_packages[args.mode]) + "> /dev/null 2>&1")
    os.system("yarn add -D " +" ".join(dev_packages[args.type]) + "> /dev/null 2>&1")

    os.system("yarn add " +" ".join(packages["common"]) + "> /dev/null 2>&1")
    os.system("yarn add " +" ".join(packages[args.mode]) + "> /dev/null 2>&1")
    os.system("yarn add " +" ".join(packages[args.type]) + "> /dev/null 2>&1")
    
    os.chdir(args.script_dir)


def init_tailwind(args):
    doPrint("Initializing tailwind")
    os.chdir(args.rootdir + '/' + args.name)
    os.system("npx tailwindcss init -p" + "> /dev/null")
    os.chdir(args.script_dir)


def copy_resources(args):
    doPrint("Copying resources")
    os.chdir(args.rootdir + '/' + args.name)
    os.system('rm -rf src/components')
    os.system('rm -rf src/assets')
    os.chdir(args.script_dir)
    os.system(f"cp -rf {args.script_dir}/resources/common/  {args.rootdir}/{args.name}")
    os.system(f"cp -rf {args.script_dir}/resources/mode/{args.mode}/  {args.rootdir}/{args.name}")
    os.system(f"cp -rf {args.script_dir}/resources/type/{args.type}/  {args.rootdir}/{args.name}")


def change_package_json(args):
    doPrint("Changing package.json")
    package_file = args.rootdir + '/' + args.name + "/package.json"

    # reading the package.json file
    with open(package_file, 'r') as file:
        package_json = json.load(file)

    # changing it
    package_json['scripts']['newpage'] = "cd .scripts && python3 create_page.py"
    if args.mode == 'ssr':
        package_json['scripts']['dev'] = "vite --port 8080"
    else:
        package_json['scripts']['dev'] = "vite-ssr --port 8080"


    # writing it back
    with open(package_file, 'w') as file:
        json.dump(package_json, file, indent=4)
    
    os.chdir(args.rootdir + '/' + args.name)
    os.system(".scripts >> .gitignore >/dev/null 2>&1")


args = prep_parser().parse_args()
args = validate_args(args)


print_welcome(args)
create_vite_project(args)
install_dependencies(args)
init_tailwind(args)
copy_resources(args)
change_package_json(args)
doPrint("Done!", icon='\u2705')
