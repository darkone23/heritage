{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  # env.GREET = "devenv";
  env.GIT_EXTERNAL_DIFF = "difft";

  # https://devenv.sh/packages/
  packages = [
    pkgs.git
    pkgs.black
    pkgs.sqlite
    pkgs.python3Packages.python-lsp-server
    pkgs.difftastic
  ];

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = ''
    pip>=19.2.3
    bump2version>=0.5.11
    wheel>=0.33.6
    watchdog>=0.9.0
    flake8>=3.7.8
    tox>=3.14.0
    coverage>=4.5.4
    Sphinx>=1.8.5
    twine>=1.14.0
    pytest>=6.2.4
    setuptools>=75.8.2

    sh>=2.2.2
    requests>=2.26.0
    beautifulsoup4>=4.10.0
  '';
  languages.c.enable = true;

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
  scripts.install.exec = ''
    make
  '';
  # scripts.hello.exec = ''
  #   echo hello from $GREET
  # '';

  # enterShell = ''
  #   hello
  #   git --version
  # '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  # enterTest = ''
  #   echo "Running tests"
  #   git --version | grep --color=auto "${pkgs.git.version}"
  # '';

  # https://devenv.sh/git-hooks/
  # git-hooks.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
