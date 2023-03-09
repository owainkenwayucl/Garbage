using UnicodePlots
using DelimitedFiles

g20182msd = DelimitedFiles.readdlm("graviton_2018.2.ssv")
g20215msd = DelimitedFiles.readdlm("graviton_2021.5.ssv")

plt = lineplot(g20182msd[begin:end,1], g20182msd[begin:end,2], title="GROMACS 2021.5 vs 2018.2 MSD on ARM", name="GROMACS 2018.2", xlabel="Time (ps)", ylabel="MSD (nm\\S2\\N)", height=40, width=132); 
lineplot!(plt, g20215msd[begin:end,1], g20215msd[begin:end,2], color=:cyan, name="GROMACS 2021.5")

print(plt)

