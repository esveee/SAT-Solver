#!/bin/bash

for filename in test/*.cnf
	do
	test_out="$(./solver < $filename)"
	echo "Testing $filename ...  $test_out"
done
