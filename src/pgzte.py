# pgzte is a fork of Pygame Turbo, which is a more swiftly-evolving, 
# pygame-ce compliant fork of Pygame Zero, the zero-boilerplate games programming framework.

# pgzte is initially agnostic between Pygame Turbo and Zero, offering a preferential setting, 
# with fallback; and agnostic to the incorporation of additional Enodia features.

# pgzte lead: Brygg Ullmer, Clemson University
# Begun 2026-07-04

# This should probably evolve, but for starters:
preferPgxVariantPrimary   = "pgturbo"
preferPgxVariantSecondary = "pgzero"

try:
  if preferPgxVariantPrimary == "pgturbo": import pgturbo
  if preferPgxVariantPrimary == "pgzero":  import pgzero
  print("pgzte: preferred primary pgx variant import succeeds")
except:
  print("pgzte: preferred primary pgx variant", preferPgxVariantPrimary, "import fails; trying secondary")

  try:
    if preferPgxVariantSecondary == "pgturbo": import pgturbo
    if preferPgxVariantSecondary == "pgzero":  import pgzero
    print("pgzte: secondary primary pgx variant", preferPgxVariantSecondary, "import succeeds")
  except:
    print("pgzte: preferred secondary pgx variant", preferPgxVariantSecondary, "import fails.")

### end ###
