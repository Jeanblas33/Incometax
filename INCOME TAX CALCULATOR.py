Deduction_Tax = 10000.0
Dependent_Tax= 3000.0
Rate_Tax= 0.20

grossincome = float(input('Please enter your gross income : '))
numberdependents = int(input('Please enter the number of dependents: '))

Taxableincome = grossincome - Deduction_Tax - Dependent_Tax * numberdependents
incometax =  Taxableincome * Rate_Tax

print('The income tax is $'+ str(incometax))