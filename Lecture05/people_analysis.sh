#!/bin/bash

## Question 1: Display an index counter and the country

## initialise the counter at zero
count=0

## read each line and assign the seven columns to variables
while read name email city birthday_day birthday_month birthday_year country
do
    ## increase the counter by 1 for each line
    count=$((count+1))

    ## display the index and country separated by a tab
    echo -e "${count}\t${country}"

## read the data from the input file
done < example_people_data.tsv

## seems like this still displays the birth years in certain cases? not rly sure why, will try to fix

## Question 2: display index counter, name,city and country without header and blank lines

count=0

while read name email city birthday_day birthday_month birthday_year country
do
    ## check that this isn't the header so it can be excluded
    if test "${name}" != "name"
    then
        ## heck that the name isn't empty to exclude blank entries
        if test "${name}" != ""
        then
            ## increase the counter
            count=$((count+1))

            ## display index, name, city and country
            echo -e "${count}\t${name}\t${city}\t${country}"
        fi
    fi

done < example_people_data.tsv

## Question 3: Create separate files for people from each country

## read each line and assign the columns to variables
while read name email city birthday_day birthday_month birthday_year country
do
    ## check that the current line isn't the header
    if test "${name}" != "name"
    then
        ## check that the current line isn't blank
        if test "${name}" != ""
        then
            ## move peoplen's name to their country's file
            echo "${name}" >> "${country}.txt"
        fi
    fi

## read from the input file
done < example_people_data.tsv

## Question 4: Count people born in October and display their names and countries

## initialise counter
count=0

## read each person from the file
while read name email city birthday_day birthday_month birthday_year country
do
    ## check whether the person's birth month is October
    if test "${birthday_month}" -eq 10
    then
        ## increase counter only for October birthdays
        count=$((count+1))

        ## display their name and country
        echo -e "${name}\t${country}"
    fi

done < example_people_data.tsv

## print total number of october birthdays

echo "total october birthdays: ${count}"

## still havent fixed issue with birthdays being in country columns so not rly accurate i guess and gives me "integer expected" errors


## Question 5: q4 but output as multiple lists
## set the counter to 0
count=0

## read each person from the file
while read name email city birthday_day birthday_month birthday_year country
do
    ## check whether the person's birth month is october
    if test "${birthday_month}" -eq 10
    then
        ## increase the counter only for october birthdays
        count=$((count+1))

        ## add the person's name and country to their country's file
        echo -e "${name}\t${country}" >> "october_${country}.txt"
    fi

done < example_people_data.tsv
