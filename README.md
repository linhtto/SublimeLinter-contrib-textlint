SublimeLinter-contrib-textlint
================================

[![Build Status](https://travis-ci.org/joeybaker/SublimeLinter-textlint.svg?branch=master)](https://travis-ci.org/joeybaker/SublimeLinter-textlint)

This linter plugin for [SublimeLinter][docs] provides an interface to [textlint](__linter_homepage__). The following syntaxes are automatically linted:

* markdown
* text
* plain text
* Markdown GFM
* MarkdownEditing
* Markdown Extended
* Markdown
* MultiMarkdown syntaxes.

## Installation
Install SublimeLinter 3 to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure to install `textlint`:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `textlint` by typing the following in a terminal:
   ```
   npm install -g textlint
   ```
Or install `textlint` locally in your project folder (**you must have package.json file there**):
    ```
    npm init -f
    npm install textlint
    ```

Reopen your project next (or restart ST) to make sure local `textlint` is used.


1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

1. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plugin for `oh-my-zsh`.


**Note:** This plugin requires `textlint` 5.3.0 or later.

### Linter configuration
`textlint` must be in your `$PATH` for Sublimelinter to work. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `textlint`, you can install the SublimeLinter-contrib-textlint plugin if it is not yet installed.

### Plugin installation
To ensure the plugin is updated when new versions are available, please use install with [Package Control][pc]. If you want to install from source so you can change the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `textlint`. Among the entries you should see `SublimeLinter-contrib-textlint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure `textlint` options in the way you would from the command line, with `.textlintrc` files. For more information, see the [textlint docs](https://github.com/textlint/textlint).

## FAQ and Troubleshooting

##### I've got 'SublimeLinter: ERROR: textlint cannot locate 'textlint' in ST console when I try to use locally installed `textlint`.

You **must** have `package.json` file if install `textlint` locally. Also, restart project or ST itself after to make sure SublimeLinter uses correct `textlint` instance.

```
npm init -f
npm install textlint
```

##### Plugin still does not work or there are errors in ST console.

Update `textlint` instance, probably you use outdated version and SublimeLinter does not check it properly sometimes.

##### I want to use custom rules

You can specify **any** [CLI options](https://github.com/textlint/textlint#cli) of `textlint` with `args` key in SublimeLinter configs.

```
{
    "linters": {
        "textlint": {
            "args": [
                "--rulesdir", "~/rules"
            ]
        }
    }
}
```

##### Plugin does not lint files in symlinked folders.

It looks like ST/SublimeLinter/Textlint issue. Set the SublimeLinter option `--stdin-filename` to `@`.

```
{
    "linters": {
        "textlint": {
            "args": [
                "--stdin-filename", "@"
            ]
        }
    }
}
```


##### There is no `SublimeLinter-contrib-textlint` package to install in Package Control packages list.

Check if you already have it installed, please.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, so don’t be afraid to use it.
- Please use descriptive variable names, so no abbreviations unless they are very well known.

Thank you for helping out!

### Testing
For convenience this repo is setup with textlint. Just `npm i` in the repo and enable this plugin in SublimeText. This file will have errors in it.


[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
