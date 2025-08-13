import taxation
import employee
choice=input("are under 87A rebate yes or no: ")
if choice == 'yes'and taxation.taxable_income <= 700000:
    print("the taxable income is:", taxation.taxable_income)
elif taxation.taxable_income <=300000:
    print("the taxable income is:", taxation.taxable_income)
elif taxation.taxable_income <= 600000:
    taxation.taxable_income =(5/100)*taxation.taxable_income
    print("the taxable income is:", taxation.taxable_income)
elif taxation.taxable_income <= 900000:
    taxation.taxable_income =(10/100)*taxation.taxable_income
    print("the taxable income is:", taxation.taxable_income)
elif taxation.taxable_income <= 1200000:
    taxation.taxable_income =(15/100)*taxation.taxable_income
    print("the taxable income is:", taxation.taxable_income)
elif taxation.taxable_income <= 1500000:
    taxation.taxable_income =(20/100)*taxation.taxable_income
    print("the taxable income is:", taxation.taxable_income)
else:
    taxation.taxable_income =(30/100)*taxation.taxable_income
    print("the taxable income is:", taxation.taxable_income)

health_insurance =taxation.taxable_income + (4/100)*taxation.taxable_income
taxation.taxable_income =taxation.taxable_income + health_insurance
print("the total taxable income is:", taxation.taxable_income)
print("the total health insurance is:", health_insurance)


    
