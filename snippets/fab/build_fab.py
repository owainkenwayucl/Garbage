# Python script that builds the project with the Met Office's "Fab" tool.

from fab.steps.analyse import Analyse
from fab.steps.compile_fortran import CompileFortran
from fab.build_config import BuildConfig
from fab.steps.find_source_files import FindSourceFiles,Include,Exclude
from fab.steps.grab import GrabFolder
from fab.steps.link import LinkExe
from fab.steps.preprocess import fortran_preprocessor
from pathlib import Path
import os
import sys

# Profiles for known compilers
compilers = {
	"nvfortran":{"compile_flag":"-c", "openmp_flag":"-mp", "opt_flags":["-O2"], "linker":"nvfortran"},
	"gfortran":{"compile_flag":"-c", "openmp_flag":"-fopenmp", "opt_flags":["-O2"], "linker":"gfortran"},
	"nagfor":{"compile_flag":"-c", "openmp_flag":"-openmp", "opt_flags":["-O2"], "linker":"nagfor"},
	"ifort":{"compile_flag":"-c", "openmp_flag":"-fopenmp", "opt_flags":["-O2"], "linker":"ifort"},
}

# Whereami
directory = os.path.dirname(os.path.realpath(__file__))

# Determine compiler from $FC.
try:
	my_compiler_name = os.environ["FC"].split()[0] # want first command
except:
	print("ERROR: Environment Variable FC not set.", file=sys.stderr)
	sys.exit(1)

if my_compiler_name not in compilers.keys():
	print("ERROR: Unknown compiler: " + my_compiler_name, file=sys.stderr)
	print("Known compilers: ", file=sys.stderr)
	for a in compilers.keys():
		print("                 " + a, file=sys.stderr)
	sys.exit(2)

my_compiler=compilers[my_compiler_name] 

# Assemble compiler flags.
my_compile_flags = [my_compiler["compile_flag"]]
my_compile_flags.append(my_compiler["openmp_flag"])
for a in my_compiler["opt_flags"]:
	my_compile_flags.append(a)

# Assemble linker options.
my_linker = my_compiler["linker"]
my_linker_flags = [my_compiler["openmp_flag"]]
for a in my_compiler["opt_flags"]:
	my_linker_flags.append(a)

my_fpp = os.path.join(directory,"shims","fpp_shim.sh")
my_workspace = Path(directory) / "fab"

# Build a Fab config.
config = BuildConfig(
	project_label="FortTest",
	fab_workspace=my_workspace, 
	steps=[
		GrabFolder(src="src/"),  # We want a subset of the source files in cwd.
		FindSourceFiles(),
		fortran_preprocessor(preprocessor=my_fpp),
		Analyse(root_symbol="forttest"),
		CompileFortran(compiler=my_compiler_name, common_flags=my_compile_flags),
		LinkExe(linker=my_linker,flags=my_linker_flags),
	]
)

# Do the build.
config.run()

