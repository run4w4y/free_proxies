{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "8c9d85736417076aaa8ec5d7abe2b5452b1cafe0";
    sha256 = "0ns0vrb8pmvdfaqzahprs283laf6nl7zm0vrz7fm10sfy79z9vr6";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]