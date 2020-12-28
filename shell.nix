{ pkgs ? import <nixos-unstable> {}, ...  }:

pkgs.mkShell {
  name = "free_proxies";
  
  buildInputs = import ./deps.nix { inherit pkgs; };

  shellHook = ''
    export TERM=xterm-256color
  '';
}