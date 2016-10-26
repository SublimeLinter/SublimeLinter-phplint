SublimeLinter-phplint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phplint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phplint)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [phplint](http://www.icosaedro.it/phplint/index.html). It will be used with files that have the “PHP”, “HTML”, or “HTML 5” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `phplint` is installed on your system. To install `phplint`, download and run the appropriate installer from the [download page](http://www.icosaedro.it/phplint/download.html). On Mac OS X, the best option is to install [Homebrew](http://brew.sh) and then enter the following in a terminal:

```sh
brew install homebrew/php/phplint
```

If installation via `brew` fails, see [this page](http://georgemastro.com/gcc-4-8-error-unrecognized-command-line-option-fnested-functions/) for possible solutions.

**Note:** This plugin requires `phplint` 2.0 or later.

### Linter configuration
In order for `phplint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `phplint` is installed and configured, you can proceed to install the SublimeLinter-phplint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `phplint`. Among the entries you should see `SublimeLinter-phplint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

To specify your version of PHP you can set it in your **User** SublimeLinter.sublime-settings file with the following syntax:
```json
{
	"user": {
        "linters": {
            "php": {
                "php-version": 7,
            }
        }
    }
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
