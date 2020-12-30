{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "e19e8157b9e065532bee32490e45b681f50edfae";
    sha256 = "17m6bq53kh355l11ljjl2lzcyw7hji0x0cysa2dj3fl1d4drrj9d";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]