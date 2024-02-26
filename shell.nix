let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = { allowUnfree = true; }; overlays = []; };

  git = pkgs.git.overrideAttrs (oldAttrs: rec {
    version = "2.42.0";
  });

in

pkgs.mkShell {
  packages = with pkgs; [
    git
    python311
    python311Packages.pip
    pkgs.pdm
  ];
}