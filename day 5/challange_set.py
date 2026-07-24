amazon={101,102,103,104,105,106}
flipkart={104,105,106,107,108,109}
##purchased from both ------------------

both=amazon & flipkart
print(f"purchased from both : {both}")
##only at amazon -------------------------

only_amazon = amazon - flipkart
print(f"purcahsed only at amazon :{only_amazon}")
#only at flipkart ---------------------

only_flipkart=flipkart - amazon 
print(f"purchased only at flipkart : {only_flipkart}")
##total---------------
total_unique =len( amazon | flipkart)
print(f"total unique customers : {total_unique}")
#either but not both -----------
not_both=amazon ^ flipkart
print(f"purchased either but not both  : {not_both}")
