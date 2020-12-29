{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "4bef5d9a87ae3d12762f92fa13d29e1a3bd99605";
    sha256 = "1yxy5cg0fz986mx90jfla4dxyg69j5g75rdnaq9pcqkzkc8wpkx0";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]