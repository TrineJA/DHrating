#!/bin/bash
CERTIFICATE_IDS="35696
35319
30113
36028"

for i in $CERTIFICATE_IDS
do
    wget "https://websejler.dk/da/certifikat/$i" -P data/certificates/
done