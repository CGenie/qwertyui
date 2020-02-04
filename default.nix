with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv {
    name = name;
    paths = buildInputs;
  };
  buildInputs = [
    python3Packages.ipython
  ];
  builder = builtins.toFile "builder.sh" ''
    source $stdenv/setup
    touch $out
  '';
}

