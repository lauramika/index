def yodafy():
    # Complete the function here:
    '''
    "Strong enough to succeed my determination is. Overtake me failure never will." 
    '''
    input_quote = "Failure will never overtake me if my determination to succeed is strong enough."
    output_quote = ''
    output_quote = input_quote[65 : 78].capitalize() + input_quote[50 : 61] + input_quote[ 
    33 : 50] + input_quote[61 : 64] + input_quote[78 : 79] + input_quote[7 : 8] + input_quote[19 : 31].capitalize() + input_quote[0 : 7].lower() + input_quote[12 : 19] + input_quote[8 : 12] + input_quote[78 : 79]
    return output_quote
    
print(yodafy())