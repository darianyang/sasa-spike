#!/bin/bash
# run sasa on spike open and closed

# run spike open
sed "s/TYPE/open/g" vmd-sasa-tmp.tcl > vmd-sasa-open.tcl
#vmd -dispdev text -e vmd-sasa-open.tcl
