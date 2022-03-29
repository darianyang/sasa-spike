#!/bin/bash

OPEN=../spike_open/spike_open.pdb 
CLOSED=../spike_closed/spike_closed.pdb

cat << EOF > cpptraj_open.in
parm $OPEN
trajin $OPEN
surf G31 @64727-64970 out G31_SASA_OPEN.dat 
surf G54 @69455-69698 out G54_SASA_OPEN.dat
surf G7  @59922-60144 out G7_SASA_OPEN.dat
EOF

cat << EOF > cpptraj_closed.in
parm $CLOSED
trajin $CLOSED
surf G31 @64727-64970 out G31_SASA_CLOSED.dat 
surf G54 @69455-69698 out G54_SASA_CLOSED.dat
surf G7  @59922-60144 out G7_SASA_CLOSED.dat
EOF

cpptraj -i cpptraj_open.in && cpptraj -i cpptraj_closed.in
