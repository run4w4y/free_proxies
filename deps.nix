{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "47d2b8b5c6e2bfe4b8cedacb32f4964b71995041";
    sha256 = "1043vv7fxscm6d6ijkciznibklh4yk8ls2291c6vgm46639cjqli";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]