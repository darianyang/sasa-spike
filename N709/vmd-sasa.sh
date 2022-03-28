#!/bin/bash
# run sasa on spike open and closed

# run spike open
#sed "s/TYPE/open/g" vmd-sasa-tmp.tcl > vmd-sasa-open.tcl
#vmd -dispdev text -e vmd-sasa-open.tcl &&

# run spike closed
sed "s/TYPE/closed/g" vmd-sasa-tmp.tcl > vmd-sasa-closed.tcl
vmd -dispdev text -e vmd-sasa-closed.tcl
