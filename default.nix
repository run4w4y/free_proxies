with import <nixos-unstable> {};
with pkgs.python3Packages;

buildPythonPackage rec {
  name = "free_proxies";
  src = ./.;
  propagatedBuildInputs = import ./deps.nix { inherit pkgs; };
}