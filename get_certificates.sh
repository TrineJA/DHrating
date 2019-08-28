#!/bin/bash
CERTIFICATE_IDS="35696

31783
35592
36052
7150
32166
10746
34654"

for i in $CERTIFICATE_IDS
do
    wget "https://websejler.dk/da/certifikat/$i" -P data/certificates/
done