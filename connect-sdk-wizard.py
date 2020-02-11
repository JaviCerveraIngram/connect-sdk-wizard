import os
from shutil import copyfile, copytree

CS = 'cs'
JAVA = 'java'
JS = 'js'
PHP = 'php'
PYTHON = 'python'
LANGUAGES = (
    CS,
    JAVA,
    # JS,
    # PHP,
    PYTHON
)


def main(name: str, lang: str):
    try:
        name = enter_name(name)
        lang = enter_language(lang)
        if ask_ok(name, lang):
            create_project(name, lang)
        else:
            main(name, lang)
    except KeyboardInterrupt:
        print('')
        print('Aborted')
    except Exception as ex:
        print('[ERROR] {}'.format(ex))


def enter_name(def_name: str) -> str:
    if def_name:
        name = input('Enter project name (Default: {})> '.format(def_name)) or def_name
    else:
        name = input('Enter project name> ')
    if not name:
        raise Exception('A name must be entered')
    return name


def enter_language(def_lang: str) -> str:
    check_language(def_lang)
    prompt = 'Enter language: {}. (Default: {})> '.format(','.join(LANGUAGES), def_lang)
    lang = input(prompt) or def_lang
    check_language(lang)
    return lang


def ask_ok(name: str, lang: str) -> bool:
    print('Entered options:')
    print('- Project name: ' + name)
    print('- Programming language: ' + lang)
    ok = input('Is this ok? (Default: yes)> ').lower() or 'yes'
    if ok in ('y', 'yes'):
        return True
    elif ok in ('n', 'no'):
        return False
    else:
        print('Unrecognized answer "{}".'.format(ok))
        return ask_ok(name, lang)


def create_project(name: str, lang: str) -> None:
    if os.path.exists(name):
        raise Exception('"{}" already exists'.format(name))
    else:
        root = root_path()
        copytree(os.path.join(root, 'templates', lang), name)


def check_language(lang: str) -> None:
    if lang not in LANGUAGES:
        raise Exception('Wrong language "{}". Valid options are: {}' \
            .format(lang, ','.join(LANGUAGES)))


def root_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    print('*** Connect SDK Project Wizard ***')
    main('', PYTHON)
