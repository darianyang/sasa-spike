# open new molecule and select the glycan of interest
mol new {spike_closed/spike_closed.psf} type {psf} first 0 last -1 step 1 waitfor 1
mol addfile {spike_closed/spike_closed.pdb} type {pdb} first 0 last -1 step 1 waitfor 1 0
set G7 [atomselect top "serial 59922 to 60144"] 
set G31 [atomselect top "serial 64727 to 64970"] 
set G54 [atomselect top "serial 69455 to 69698"] 

# selection and file header
set protein [atomselect top "protein or lipid or glycan"]
set output [open "SASA_closed.dat" w]
puts $output "#SASA Calculations for N234 of SARS-COV2 spike_closed"
puts $output "#probe-radius\tG7\tG31\tG54"

# use the default water probe radius of 1.4A
set sasaG7 [measure sasa 1.4 $protein -restrict $G7]
set sasaG31 [measure sasa 1.4 $protein -restrict $G31]
set sasaG54 [measure sasa 1.4 $protein -restrict $G54]
puts $output "1.4\t$sasaG7\t$sasaG31\t$sasaG54"

# tcl loop of multiple probe radii (int only)
for {set i 2} {$i < 22} {incr i} {
    # sasa calculation for trimer N234A glycans
    set sasaG7 [measure sasa $i $protein -restrict $G7]
    set sasaG31 [measure sasa $i $protein -restrict $G31]
    set sasaG54 [measure sasa $i $protein -restrict $G54]
    puts $output "$i.0\t$sasaG7\t$sasaG31\t$sasaG54"
    puts "\tprogress: $i/21"
}

puts "Done."	
puts "output file: SASA_closed.dat"
close $output

quit
