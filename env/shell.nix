with (import <nixpkgs> {}
#  { overlays = [
#    (self: super: {
#      python39Packages.praw = super.python39Packages.praw.overrideAttrs (old: {
#        src = super.fetchFromGitHub {
#          owner = "praw-dev";
#          repo = "asyncpraw";
#          rev = old.src.rev;
#          sha256 = "sha256-7tcWgFgEYuvmlWMRclGCbbxeQSd6l8rOXWRXM4Iewdw=";
#        };
#        propagatedBuildInputs = old.propagatedBuildInputs ++ self.python39Packages.aiofiles;
#      });
#    })
#  ];}
);
mkShell {
  buildInputs = with pkgs; [
    python39
  ];
  nativeBuildInputs = with pkgs.python39Packages; [
    discordpy
    requests
    praw
  ];
}
