# add new molecule and select the glycans of interest
mol new {../spike_closed/spike_closed.psf} type {psf} first 0 last -1 step 1 waitfor 1
mol addfile {../spike_closed/spike_closed.pdb} type {pdb} first 0 last -1 step 1 waitfor 1 0
set G14 [atomselect top "serial 61272 to 61452"] 
set G38 [atomselect top "serial 66206 to 66365"] 
set G61 [atomselect top "serial 70941 to 71100"] 

# selection and file header
set protein [atomselect top "protein or lipid or glycan"]
set output [open "SASA_closed.dat" w]
puts $output "#SASA Calculations for N709 of SARS-COV2 spike_closed"
puts $output "#probe-radius\tG14\tG38\tG61"

# use the default water probe radius of 1.4A
set sasaG14 [measure sasa 1.4 $protein -restrict $G14]
set sasaG38 [measure sasa 1.4 $protein -restrict $G38]
set sasaG61 [measure sasa 1.4 $protein -restrict $G61]
puts $output "1.4\t$sasaG14\t$sasaG38\t$sasaG61"

# tcl loop of multiple probe radii (int only)
for {set i 2} {$i < 22} {incr i} {
    # sasa calculation for trimer N234A glycans
    set sasaG14 [measure sasa $i $protein -restrict $G14]
    set sasaG38 [measure sasa $i $protein -restrict $G38]
    set sasaG61 [measure sasa $i $protein -restrict $G61]
    puts $output "$i.0\t$sasaG14\t$sasaG38\t$sasaG61"
    puts "\tprogress: $i/21"
}

puts "Done."	
puts "output file: SASA_closed.dat"
close $output

quit
