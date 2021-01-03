{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "516669989502ccc80a54910162a9854dbf09829e";
    sha256 = "1b4qvc5zwimcfpkhsb20z0lalgrvjsaq283mc8r8kiz2baz7lwgf";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]