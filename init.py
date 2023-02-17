import argparse
import sys
import os
import json


def _copy_with_insert(old_file, new_file, **placeholdervals):
    with open(old_file, 'r') as file_from, open(new_file, 'w+') as file_to:
        for line in file_from.readlines():
            content = line
            for placeholder, value in placeholdervals.items():
                content = content.replace(
                    f'{{%{placeholder.upper()}%}}', value)
            file_to.write(content)


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
    parser.add_argument(
        'name', help="The name of the project. This will be the name of the folder too.")
    # option that takes a value
    parser.add_argument(
        '-t', '--type', help="The type of the project (app, site).")
    parser.add_argument(
        '-m', '--mode', help="The mode of the project (SPA, SSR).")
    parser.add_argument(
        '-r', '--rootdir', help="The root directory where the project should be initiated.")
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


def initiate(args):
    os.chdir(args.rootdir)
    os.mkdir(args.name)
    os.chdir(args.script_dir)


def init_firebase(args):
    doPrint("Initializing firebase project, give your inputs when prompted.")
    os.chdir(args.rootdir + '/' + args.name)
    os.system("npx firebase init hosting")
    os.system("npx firebase init functions")
    fb_info_txt = '{' + '\n'.join(os.popen("firebase apps:sdkconfig").read().split('\n')[5:-3]) + '}'
    fb_info = json.loads(fb_info_txt)
    args.fb_info = fb_info

    firebase_json = {
        "functions": {"source": ".output/server"},
        "hosting": [
            {
                "site": fb_info['projectId'],
                "public": ".output/public",
                "cleanUrls": True,
                "rewrites": [{"source": "**", "function": "server"}]
            }
        ]
    }

    with open('firebase.json', 'w') as f:
        json.dump(firebase_json, f, indent=2)

    os.chdir(args.script_dir)

    return args


def create_nuxt_project(args):
    doPrint("Creating nuxt project")

    os.chdir(args.rootdir)
    # os.mkdir(args.name)
    os.system("npx nuxi init " + args.name + "> /dev/null 2>&1")
    os.chdir(args.rootdir + '/' + args.name)
    os.system("yarn > /dev/null 2>&1")
    os.chdir(args.script_dir)


def install_dependencies(args):
    doPrint("Installing dependencies")

    os.chdir(args.rootdir + '/' + args.name)

    # Defining needed dependencies
    dev_packages = {
        "common": ("@types/uuid", 'firebase-tools', 'firebase-admin', 'firebase-functions'),
        "site": (),
        "app": (),
        "ssr": (),
        "spa": (),
    }
    packages = {
        "common": ("@nuxtjs/tailwindcss", "@headlessui/vue", "@heroicons/vue", "@tiptap/core", "@tiptap/extension-underline", "@tiptap/pm", "@tiptap/starter-kit", "@tiptap/vue-3", "firebase", "pinia", "@pinia/nuxt", "uuid", "vue-heroicons", "@vueuse/core", "@tailwindcss/forms"),
        "site": (),
        "app": (),
        "ssr": (),
        "spa": (),
    }
    # Installing dependencies
    os.system("yarn add -D " +
              " ".join(dev_packages["common"]) + "> /dev/null 2>&1")
    os.system("yarn add -D " +
              " ".join(dev_packages[args.mode]) + "> /dev/null 2>&1")
    os.system("yarn add -D " +
              " ".join(dev_packages[args.type]) + "> /dev/null 2>&1")

    os.system("yarn add " + " ".join(packages["common"]) + "> /dev/null 2>&1")
    os.system("yarn add " + " ".join(packages[args.mode]) + "> /dev/null 2>&1")
    os.system("yarn add " + " ".join(packages[args.type]) + "> /dev/null 2>&1")

    os.chdir(args.script_dir)


def copy_resources(args):
    doPrint("Copying resources")
    os.chdir(args.script_dir)
    os.system(
        f"cp -rf {args.script_dir}/resources/nuxt/  {args.rootdir}/{args.name}")
    fb_config_string = json.dumps(args.fb_info)
    changes = {
        'firebase.ts': {"FBCONFIG": fb_config_string},
        'plugins/firebase.client.ts': {"FBCONFIG": fb_config_string}
    }
    for file, changes in changes.items():
        _copy_with_insert(
            f"{args.script_dir}/resources/nuxt/{file}", f"{args.rootdir}/{args.name}/{file}", **changes)


def change_package_json(args):
    doPrint("Changing package.json")
    package_file = args.rootdir + '/' + args.name + "/package.json"

    # reading the package.json file
    with open(package_file, 'r') as file:
        package_json = json.load(file)

    # changing it
    package_json['scripts']['newpage'] = "cd .scripts && python3 create_page.py"
    package_json['scripts']['deploy'] = "NITRO_PRESET=firebase yarn build && npx firebase deploy"

    # writing it back
    with open(package_file, 'w') as file:
        json.dump(package_json, file, indent=4)

    os.chdir(args.rootdir + '/' + args.name)
    os.system(".scripts >> .gitignore >/dev/null 2>&1")


args = prep_parser().parse_args()
args = validate_args(args)

print_welcome(args)
initiate(args)
create_nuxt_project(args)
args = init_firebase(args)
install_dependencies(args)
copy_resources(args)
change_package_json(args)
doPrint("Done!", icon='\u2705')

# args = fb_info_raw.split()

# '// Copy and paste this into your JavaScript code to initialize the Firebase SDK.',
# '// You will also need to load the Firebase SDK.',
# '// See https://firebase.google.com/docs/web/setup for more details.',
# 'firebase.initializeApp({',
# '  "projectId": "hitco-scaffold",',
# '  "appId": "1:448658195585:web:58131370b033ebf0383980",',
# '  "databaseURL": "https://hitco-scaffold-default-rtdb.europe-west1.firebasedatabase.app",',
# '  "storageBucket": "hitco-scaffold.appspot.com",',
# '  "locationId": "europe-west",',
# '  "apiKey": "AIzaSyD5dYIS2IThzWRC4a73erGk8_lLMCyn_C4",',
# '  "authDomain": "hitco-scaffold.firebaseapp.com",',
# '  "messagingSenderId": "448658195585",',
# '  "measurementId": "G-EV3X4CW9W9"',
# '});',


# x.plit()[5:-1]


# To make it work:
# - firebase init
# - replace firebase json with
# {
#   "functions": { "source": ".output/server" },
#   "hosting": [
#     {
#       "site": "hitco-scaffold",
#       "public": ".output/public",
#       "cleanUrls": true,
#       "rewrites": [{ "source": "**", "function": "server" }]
#     }
#   ]
# }
# - NITRO_PRESET=firebase yarn build

# # Should change stuff to rename function and add caching

# - npx firebase deploy
