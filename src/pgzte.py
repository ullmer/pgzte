# pgzte is a fork of Pygame Turbo, which is a more swiftly-evolving, 
# pygame-ce compliant fork of Pygame Zero, the zero-boilerplate games programming framework.

# pgzte is initially agnostic between Pygame Turbo and Zero, offering a preferential setting, 
# with fallback; and agnostic to the incorporation of additional Enodia features.

# This should probably evolve, but for starters:
preferPgxVariantPrimary   = "pgturbo"
preferPgxVariantSecondary = "pgzero"

try:
  if preferPgxVariantPrimary is "pgturbo": import pgturbo
  if preferPgxVariantPrimary is "pgzero":  import pgzero
  print("pgzte: preferred primary pgx variant import succeeds")
except:
  print("pgzte: preferred primary pgx variant", preferPgxVariantPrimary, " import fails; trying secondary"

  try:
    if preferPgxVariantSecondary is "pgturbo": import pgturbo
    if preferPgxVariantSecondary is "pgzero":  import pgzero
    print("pgzte: secondary primary pgx variant import succeeds")
  except:
    print("pgzte: preferred secondary pgx variant", preferPgxVariantSecondary, " import fails.")

### end ###
