{ pkgs ? import <nixpkgs> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "02372d82b73670558e474062a7c111e4eb0c3a93";
    sha256 = "12amaq6msyg0v5ksr7jfi093swz046zp9xj04azdi04c56g7rhn3";
  };
};
[
  (import "${async_web_scrapper}/default.nix")
  (pkgs.python38.withPackages (p: with p; [
    trio
  ]))
]