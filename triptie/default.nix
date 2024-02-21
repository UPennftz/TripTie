{ pkgs ? import <nixpkgs> {} }:

pkgs.python38.withPackages (pythonPackages: [
  pythonPackages.Django
  pythonPackages.djangorestframework
])

